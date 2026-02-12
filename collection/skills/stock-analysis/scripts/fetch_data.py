#!/usr/bin/env python3
"""
Stock Data Fetching Script for Stock Analysis

Fetches historical stock data from AkShare API and saves to CSV format.
Supports daily, weekly, and monthly data with forward adjustment.

Usage:
    python fetch_data.py --code 600519 --period 60 --adjust qfq
    python fetch_data.py --code 600519 --start 20240101 --end 20260204
"""

import argparse
import sys
from datetime import datetime, timedelta
import pandas as pd


def fetch_stock_data(code: str, period: int = 60, adjust: str = "qfq",
                   start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """
    Fetch stock data from AkShare.

    Args:
        code: Stock code (e.g., "600519")
        period: Number of trading days to fetch (default: 60)
        adjust: Price adjustment - "qfq" (forward), "hfq" (backward), "" (none)
        start_date: Start date in YYYYMMDD format (overrides period)
        end_date: End date in YYYYMMDD format (default: today)

    Returns:
        DataFrame with stock data
    """
    try:
        import akshare as ak
    except ImportError:
        print("❌ Error: AkShare not installed. Run: pip install akshare")
        sys.exit(1)

    # Calculate date range if not specified
    if end_date is None:
        end_date = datetime.now().strftime("%Y%m%d")
    else:
        end_date = end_date.replace("-", "")

    if start_date is None and period:
        # Calculate start date from period (roughly period * 1.5 for calendar days)
        start_date_obj = datetime.now() - timedelta(days=period * 1.5)
        start_date = start_date_obj.strftime("%Y%m%d")

    # Convert code format (AkShare expects leading 0 for Shanghai)
    if len(code) == 6:
        # Assume A-share, need to add prefix
        if code.startswith("6"):
            full_code = f"0.{code}"  # Shanghai
        elif code.startswith(("0", "3")):
            full_code = f"1.{code}"  # Shenzhen
        else:
            full_code = code
    else:
        full_code = code

    print(f"📥 Fetching stock data for {code}...")
    print(f"   Date range: {start_date} to {end_date}")
    print(f"   Adjustment: {adjust}")

    try:
        # Fetch data
        df = ak.stock_zh_a_hist(
            symbol=full_code,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )

        if df.empty:
            print(f"❌ Error: No data returned for stock {code}")
            return pd.DataFrame()

        # Rename columns for consistency
        column_mapping = {
            '日期': 'date',
            '开盘': 'open',
            '收盘': 'close',
            '最高': 'high',
            '最低': 'low',
            '成交量': 'volume',
            '成交额': 'amount',
            '振幅': 'amplitude',
            '涨跌幅': 'change_pct',
            '涨跌额': 'change_amount',
            '换手率': 'turnover'
        }

        df = df.rename(columns=column_mapping)

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Sort by date (ascending)
        df = df.sort_values('date').reset_index(drop=True)

        # Basic validation
        required_cols = ['date', 'open', 'high', 'low', 'close', 'volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"⚠️  Warning: Missing columns: {missing_cols}")
            return pd.DataFrame()

        # Remove rows with missing values in required columns
        df = df.dropna(subset=required_cols)

        print(f"✅ Successfully fetched {len(df)} records")
        print(f"   Date range: {df['date'].min()} to {df['date'].max()}")
        print(f"   Latest price: {df['close'].iloc[-1]:.2f}")

        return df

    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return pd.DataFrame()


def save_to_csv(df: pd.DataFrame, code: str, output_dir: str = "."):
    """Save DataFrame to CSV file."""
    if df.empty:
        print("❌ No data to save")
        return

    # Create output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_data_{code}_{timestamp}.csv"
    filepath = f"{output_dir}/{filename}"

    try:
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        print(f"✅ Data saved to: {filepath}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")


def print_summary(df: pd.DataFrame):
    """Print summary of fetched data."""
    if df.empty:
        return

    print("\n" + "="*50)
    print("📊 DATA SUMMARY")
    print("="*50)

    print(f"\nStock Code: {df.iloc[-1]['close']:.2f} (latest)")
    print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
    print(f"Total Records: {len(df)}")

    print(f"\n{'Date':<12} {'Open':>10} {'High':>10} {'Low':>10} {'Close':>10} {'Volume':>12}")
    print("-" * 74)

    # Show last 10 records
    for _, row in df.tail(10).iterrows():
        print(f"{row['date'].strftime('%Y-%m-%d'):<12} "
              f"{row['open']:>10.2f} {row['high']:>10.2f} "
              f"{row['low']:>10.2f} {row['close']:>10.2f} "
              f"{row['volume']:>12,.0f}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch stock data from AkShare",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--code',
        type=str,
        required=True,
        help='Stock code (e.g., 600519)'
    )

    parser.add_argument(
        '--period',
        type=int,
        default=60,
        help='Number of trading days to fetch (default: 60)'
    )

    parser.add_argument(
        '--adjust',
        type=str,
        default='qfq',
        choices=['qfq', 'hfq', ''],
        help='Price adjustment (default: qfq)'
    )

    parser.add_argument(
        '--start',
        type=str,
        help='Start date in YYYYMMDD format'
    )

    parser.add_argument(
        '--end',
        type=str,
        help='End date in YYYYMMDD format'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='.',
        help='Output directory for CSV file (default: current directory)'
    )

    parser.add_argument(
        '--summary',
        action='store_true',
        help='Print data summary'
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress output (for scripting)'
    )

    args = parser.parse_args()

    # Validate arguments
    if args.start and not args.start.isdigit() or len(args.start) != 8:
        print("❌ Error: Start date must be in YYYYMMDD format")
        sys.exit(1)

    if args.end and not args.end.isdigit() or len(args.end) != 8:
        print("❌ Error: End date must be in YYYYMMDD format")
        sys.exit(1)

    # Fetch data
    df = fetch_stock_data(
        code=args.code,
        period=args.period,
        adjust=args.adjust,
        start_date=args.start,
        end_date=args.end
    )

    # Save to CSV
    save_to_csv(df, code=args.code, output_dir=args.output)

    # Print summary if requested
    if args.summary and not args.quiet:
        print_summary(df)

    return 0


if __name__ == "__main__":
    sys.exit(main())
