#!/usr/bin/env python3
"""
Technical Indicators Calculation Script for Stock Analysis

Calculates comprehensive technical indicators including trend, oscillator,
volume, and momentum indicators from stock price data.

Usage:
    python indicators.py --input stock_data.csv --output indicators.csv
    python indicators.py --input stock_data.csv --indicators ma,macd,kdj,rsi
"""

import argparse
import sys
import pandas as pd
import numpy as np


def calculate_ma(df: pd.DataFrame, periods: list = [5, 10, 20, 30, 60, 120]) -> pd.DataFrame:
    """Calculate Moving Averages."""
    print(f"📥 Calculating MA for periods: {periods}")
    for period in periods:
        if len(df) >= period:
            df[f'MA{period}'] = df['close'].rolling(window=period).mean()
        else:
            df[f'MA{period}'] = np.nan
    return df


def calculate_ema(df: pd.DataFrame, periods: list = [12, 26]) -> pd.DataFrame:
    """Calculate Exponential Moving Averages."""
    print(f"📥 Calculating EMA for periods: {periods}")
    for period in periods:
        if len(df) >= period:
            df[f'EMA{period}'] = df['close'].ewm(span=period, adjust=False).mean()
        else:
            df[f'EMA{period}'] = np.nan
    return df


def calculate_boll(df: pd.DataFrame, n: int = 20, m: int = 2) -> pd.DataFrame:
    """Calculate Bollinger Bands."""
    print(f"📥 Calculating Bollinger Bands (N={n}, M={m})")
    if len(df) >= n:
        # Middle band = MA(n)
        df['BOLL_MID'] = df['close'].rolling(window=n).mean()

        # Standard deviation
        df['BOLL_STD'] = df['close'].rolling(window=n).std()

        # Upper and lower bands
        df['BOLL_UPPER'] = df['BOLL_MID'] + (df['BOLL_STD'] * m)
        df['BOLL_LOWER'] = df['BOLL_MID'] - (df['BOLL_STD'] * m)
    else:
        df['BOLL_MID'] = np.nan
        df['BOLL_STD'] = np.nan
        df['BOLL_UPPER'] = np.nan
        df['BOLL_LOWER'] = np.nan

    return df


def calculate_macd(df: pd.DataFrame, fast: int = 12, slow: int = 26,
                  signal: int = 9) -> pd.DataFrame:
    """Calculate MACD (Moving Average Convergence Divergence)."""
    print(f"📥 Calculating MACD (fast={fast}, slow={slow}, signal={signal})")

    # Calculate EMAs
    df['EMA_FAST'] = df['close'].ewm(span=fast, adjust=False).mean()
    df['EMA_SLOW'] = df['close'].ewm(span=slow, adjust=False).mean()

    # MACD line = EMA(fast) - EMA(slow)
    df['MACD_DIF'] = df['EMA_FAST'] - df['EMA_SLOW']

    # Signal line = EMA of MACD
    df['MACD_DEA'] = df['MACD_DIF'].ewm(span=signal, adjust=False).mean()

    # Histogram = MACD - Signal
    df['MACD_BAR'] = df['MACD_DIF'] - df['MACD_DEA']

    return df


def calculate_rsi(df: pd.DataFrame, periods: list = [6, 12, 24]) -> pd.DataFrame:
    """Calculate Relative Strength Index."""
    print(f"📥 Calculating RSI for periods: {periods}")

    for period in periods:
        if len(df) >= period + 1:
            # Calculate price change
            delta = df['close'].diff()

            # Separate gains and losses
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

            # Calculate RS and RSI
            rs = gain / loss
            df[f'RSI{period}'] = 100 - (100 / (1 + rs))
        else:
            df[f'RSI{period}'] = np.nan

    return df


def calculate_kdj(df: pd.DataFrame, n: int = 9, m1: int = 3,
                  m2: int = 3) -> pd.DataFrame:
    """Calculate KDJ (Stochastic Oscillator)."""
    print(f"📥 Calculating KDJ (N={n}, M1={m1}, M2={m2})")

    if len(df) >= n:
        # Calculate RSV (Raw Stochastic Value)
        low_min = df['low'].rolling(window=n).min()
        high_max = df['high'].rolling(window=n).max()
        rsv = (df['close'] - low_min) / (high_max - low_min) * 100

        # Calculate K, D, J
        df['KDJ_K'] = rsv.ewm(com=m1, adjust=False).mean()
        df['KDJ_D'] = df['KDJ_K'].ewm(com=m2, adjust=False).mean()
        df['KDJ_J'] = 3 * df['KDJ_K'] - 2 * df['KDJ_D']
    else:
        df['KDJ_K'] = np.nan
        df['KDJ_D'] = np.nan
        df['KDJ_J'] = np.nan

    return df


def calculate_cci(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """Calculate Commodity Channel Index."""
    print(f"📥 Calculating CCI (period={period})")

    if len(df) >= period:
        # Typical price (TP)
        tp = (df['high'] + df['low'] + df['close']) / 3
        df['CCI_TP'] = tp

        # MA of TP
        ma_tp = tp.rolling(window=period).mean()
        df['CCI_MA'] = ma_tp

        # Mean absolute deviation
        mad = tp.rolling(window=period).apply(
            lambda x: np.abs(x - x.mean()).mean()
        )

        # CCI = (TP - MA(TP)) / (0.015 * MAD)
        df['CCI'] = (tp - ma_tp) / (0.015 * mad)
    else:
        df['CCI_TP'] = np.nan
        df['CCI_MA'] = np.nan
        df['CCI'] = np.nan

    return df


def calculate_bias(df: pd.DataFrame, periods: list = [6, 12, 24]) -> pd.DataFrame:
    """Calculate Deviation Rate (BIAS)."""
    print(f"📥 Calculating BIAS for periods: {periods}")

    for period in periods:
        if len(df) >= period:
            ma = df['close'].rolling(window=period).mean()
            df[f'BIAS{period}'] = (df['close'] - ma) / ma * 100
        else:
            df[f'BIAS{period}'] = np.nan

    return df


def calculate_wr(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """Calculate Williams %R."""
    print(f"📥 Calculating WR (period={period})")

    if len(df) >= period:
        high_max = df['high'].rolling(window=period).max()
        low_min = df['low'].rolling(window=period).min()
        df['WR'] = (high_max - df['close']) / (high_max - low_min) * -100
    else:
        df['WR'] = np.nan

    return df


def calculate_obv(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate On-Balance Volume (OBV)."""
    print("📥 Calculating OBV")

    # Calculate price change
    price_change = df['close'].diff()

    # OBV = OBV_prev + volume if price > price_prev else -volume
    obv_value = np.where(price_change > 0, df['volume'], -df['volume'])

    # Cumulative OBV
    df['OBV'] = obv_value.cumsum()

    return df


def calculate_vr(df: pd.DataFrame, period: int = 24) -> pd.DataFrame:
    """Calculate Volume Ratio (VR)."""
    print(f"📥 Calculating VR (period={period})")

    if len(df) >= period:
        # Calculate price change
        price_change = df['close'].diff()

        # Separate volume for up and down days
        up_volume = df['volume'].where(price_change > 0, 0)
        down_volume = df['volume'].where(price_change < 0, 0)

        # Sum over period
        up_volume_sum = up_volume.rolling(window=period).sum()
        down_volume_sum = down_volume.rolling(window=period).sum()

        # VR = (up_volume_sum / down_volume_sum) * 100
        df['VR'] = (up_volume_sum / down_volume_sum).replace([np.inf, -np.inf], 0) * 100
    else:
        df['VR'] = np.nan

    return df


def calculate_mom(df: pd.DataFrame, period: int = 10) -> pd.DataFrame:
    """Calculate Momentum."""
    print(f"📥 Calculating MOM (period={period})")

    if len(df) >= period:
        df['MOM'] = df['close'] - df['close'].shift(period)
    else:
        df['MOM'] = np.nan

    return df


def calculate_roc(df: pd.DataFrame, period: int = 12) -> pd.DataFrame:
    """Calculate Rate of Change."""
    print(f"📥 Calculating ROC (period={period})")

    if len(df) >= period:
        df['ROC'] = (df['close'] - df['close'].shift(period)) / df['close'].shift(period) * 100
    else:
        df['ROC'] = np.nan

    return df


def calculate_arbr(df: pd.DataFrame, n: int = 26) -> pd.DataFrame:
    """Calculate Altitude Ratio (ARBR)."""
    print(f"📥 Calculating ARBR (N={n})")

    if len(df) >= n:
        # Calculate high-low and close-open
        hl = df['high'] - df['low']
        co = df['close'] - df['open']

        # Sum over N days
        ar = (co.where(co > 0, 0)).rolling(window=n).sum()
        br = (co.where(co < 0, 0)).rolling(window=n).sum()
        hl_sum = hl.rolling(window=n).sum()

        # AR and BR
        df['AR'] = ar / hl_sum * 100
        df['BR'] = br / hl_sum * 100
    else:
        df['AR'] = np.nan
        df['BR'] = np.nan

    return df


def calculate_cr(df: pd.DataFrame, period: int = 26) -> pd.DataFrame:
    """Calculate Capability Ratio (CR)."""
    print(f"📥 Calculating CR (period={period})")

    if len(df) >= period:
        # Calculate mid-point
        mid_point = (df['high'] + df['low']) / 2

        # Compare close to mid-point over N days
        up_days = (df['close'] > mid_point).rolling(window=period).sum()

        # CR = (up_days / N) * 100
        df['CR'] = up_days / period * 100
    else:
        df['CR'] = np.nan

    return df


def calculate_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate all technical indicators."""
    print("\n" + "="*50)
    print("📊 CALCULATING ALL TECHNICAL INDICATORS")
    print("="*50 + "\n")

    # Trend indicators
    df = calculate_ma(df)
    df = calculate_ema(df)
    df = calculate_boll(df)
    df = calculate_macd(df)

    # Oscillators
    df = calculate_rsi(df)
    df = calculate_kdj(df)
    df = calculate_cci(df)
    df = calculate_bias(df)
    df = calculate_wr(df)

    # Volume indicators
    df = calculate_obv(df)
    df = calculate_vr(df)

    # Momentum indicators
    df = calculate_mom(df)
    df = calculate_roc(df)
    df = calculate_arbr(df)
    df = calculate_cr(df)

    print("\n✅ All indicators calculated!")
    print(f"   Total indicators: {len(df.columns) - len(df.columns[:7])}")  # Subtract basic columns

    return df


def load_data(input_file: str) -> pd.DataFrame:
    """Load stock data from CSV file."""
    print(f"📥 Loading data from {input_file}")

    try:
        df = pd.read_csv(input_file)

        # Check required columns
        required_cols = ['date', 'open', 'high', 'low', 'close', 'volume']
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"❌ Error: Missing required columns: {missing_cols}")
            print(f"   Required columns: {required_cols}")
            return pd.DataFrame()

        print(f"✅ Loaded {len(df)} records")
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()


def save_data(df: pd.DataFrame, output_file: str):
    """Save indicators data to CSV file."""
    if df.empty:
        print("❌ No data to save")
        return

    try:
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"✅ Indicators saved to: {output_file}")
        print(f"   Total columns: {len(df.columns)}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")


def print_summary(df: pd.DataFrame):
    """Print summary of calculated indicators."""
    if df.empty:
        return

    print("\n" + "="*50)
    print("📊 INDICATORS SUMMARY")
    print("="*50)

    # Get last non-NaN row
    last_row = df.dropna(subset=['MA5', 'MACD_DIF', 'RSI12']).iloc[-1]

    print(f"\n📅 Latest Date: {last_row['date']}")
    print(f"💰 Close Price: {last_row['close']:.2f}\n")

    # Trend indicators
    print("📈 Trend Indicators:")
    print(f"   MA5: {last_row.get('MA5', 'N/A'):.2f}")
    print(f"   MA10: {last_row.get('MA10', 'N/A'):.2f}")
    print(f"   MA20: {last_row.get('MA20', 'N/A'):.2f}")
    print(f"   MA60: {last_row.get('MA60', 'N/A'):.2f}")
    print(f"   MACD DIF: {last_row.get('MACD_DIF', 'N/A'):.2f}")
    print(f"   MACD DEA: {last_row.get('MACD_DEA', 'N/A'):.2f}")
    print(f"   MACD BAR: {last_row.get('MACD_BAR', 'N/A'):.2f}")

    # Oscillators
    print("\n📊 Oscillators:")
    print(f"   RSI6: {last_row.get('RSI6', 'N/A'):.2f}")
    print(f"   RSI12: {last_row.get('RSI12', 'N/A'):.2f}")
    print(f"   KDJ K: {last_row.get('KDJ_K', 'N/A'):.2f}")
    print(f"   KDJ D: {last_row.get('KDJ_D', 'N/A'):.2f}")
    print(f"   KDJ J: {last_row.get('KDJ_J', 'N/A'):.2f}")
    print(f"   CCI: {last_row.get('CCI', 'N/A'):.2f}")
    print(f"   BIAS6: {last_row.get('BIAS6', 'N/A'):.2f}")
    print(f"   WR14: {last_row.get('WR14', 'N/A'):.2f}")

    # Volume indicators
    print("\n📦 Volume Indicators:")
    print(f"   OBV: {last_row.get('OBV', 'N/A'):,.0f}")
    print(f"   VR: {last_row.get('VR', 'N/A'):.2f}")

    # Momentum indicators
    print("\n🚀 Momentum Indicators:")
    print(f"   MOM10: {last_row.get('MOM', 'N/A'):.2f}")
    print(f"   ROC12: {last_row.get('ROC12', 'N/A'):.2f}")
    print(f"   AR: {last_row.get('AR', 'N/A'):.2f}")
    print(f"   BR: {last_row.get('BR', 'N/A'):.2f}")
    print(f"   CR: {last_row.get('CR', 'N/A'):.2f}")


def main():
    parser = argparse.ArgumentParser(
        description="Calculate technical indicators from stock data",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Input CSV file with stock data'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='indicators.csv',
        help='Output CSV file for indicators (default: indicators.csv)'
    )

    parser.add_argument(
        '--indicators',
        type=str,
        default='all',
        help='Comma-separated list of indicators (default: all)'
    )

    parser.add_argument(
        '--summary',
        action='store_true',
        help='Print indicators summary'
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress output (for scripting)'
    )

    args = parser.parse_args()

    # Validate input file
    try:
        open(args.input, 'r')
    except FileNotFoundError:
        print(f"❌ Error: Input file not found: {args.input}")
        sys.exit(1)

    # Load data
    df = load_data(args.input)

    if df.empty:
        sys.exit(1)

    # Calculate indicators
    if args.indicators == 'all':
        df = calculate_all_indicators(df)
    else:
        # Calculate specific indicators only
        indicators_list = args.indicators.split(',')

        for indicator in indicators_list:
            indicator = indicator.strip().lower()

            if indicator == 'ma':
                df = calculate_ma(df)
            elif indicator == 'ema':
                df = calculate_ema(df)
            elif indicator == 'boll':
                df = calculate_boll(df)
            elif indicator == 'macd':
                df = calculate_macd(df)
            elif indicator == 'rsi':
                df = calculate_rsi(df)
            elif indicator == 'kdj':
                df = calculate_kdj(df)
            elif indicator == 'cci':
                df = calculate_cci(df)
            elif indicator == 'bias':
                df = calculate_bias(df)
            elif indicator == 'wr':
                df = calculate_wr(df)
            elif indicator == 'obv':
                df = calculate_obv(df)
            elif indicator == 'vr':
                df = calculate_vr(df)
            elif indicator == 'mom':
                df = calculate_mom(df)
            elif indicator == 'roc':
                df = calculate_roc(df)
            elif indicator == 'arbr':
                df = calculate_arbr(df)
            elif indicator == 'cr':
                df = calculate_cr(df)
            else:
                print(f"⚠️  Unknown indicator: {indicator}")

    # Save data
    save_data(df, args.output)

    # Print summary if requested
    if args.summary and not args.quiet:
        print_summary(df)

    return 0


if __name__ == '__main__':
    sys.exit(main())
