#!/usr/bin/env python3
"""
Stock Scoring Model Script for Stock Analysis

Calculates comprehensive stock score from 4 dimensions:
- Trend (40%)
- Momentum (30%)
- Money Flow (20%)
- Sentiment (10%)

Usage:
    python scoring.py --input indicators.csv --output scores.csv
    python scoring.py --input indicators.csv --weights trend=0.5,momentum=0.3
"""

import argparse
import sys
import pandas as pd
import numpy as np


class StockScorer:
    """Stock analysis scoring model."""

    def __init__(self, trend_weight=0.4, momentum_weight=0.3,
                 money_flow_weight=0.2, sentiment_weight=0.1):
        """Initialize scorer with custom weights."""
        self.trend_weight = trend_weight
        self.momentum_weight = momentum_weight
        self.money_flow_weight = money_flow_weight
        self.sentiment_weight = sentiment_weight

        # Validate weights
        total = trend_weight + momentum_weight + money_flow_weight + sentiment_weight
        if abs(total - 1.0) > 0.01:
            print(f"⚠️  Warning: Weights don't sum to 1.0 (sum={total:.2f})")

    def calculate_trend_score(self, df: pd.DataFrame, lookback: int = 60) -> float:
        """
        Calculate trend score based on MA alignment, MACD, BOLL.

        Returns: Score 0-100
        """
        if len(df) < lookback:
            return 50.0

        recent = df.tail(lookback)

        # 1. MA Alignment Score (40 points)
        ma_score = 0.0
        try:
            # Check if MA5 > MA10 > MA20 > MA60 (bullish)
            ma5 = recent['MA5'].iloc[-1]
            ma10 = recent['MA10'].iloc[-1]
            ma20 = recent['MA20'].iloc[-1]
            ma60 = recent['MA60'].iloc[-1]

            if ma5 > ma10 > ma20 > ma60:
                ma_score = 40  # Perfect bullish alignment
            elif ma5 > ma10 > ma20:
                ma_score = 30  # Medium bullish
            elif ma5 > ma10:
                ma_score = 20  # Slight bullish
            elif ma5 < ma10 < ma20 < ma60:
                ma_score = 0   # Perfect bearish alignment
            elif ma5 < ma10 < ma20:
                ma_score = 10  # Medium bearish
            elif ma5 < ma10:
                ma_score = 20  # Slight bearish
            else:
                ma_score = 25  # Mixed/sideways
        except (KeyError, ValueError):
            ma_score = 20.0

        # 2. MACD Score (30 points)
        macd_score = 0.0
        try:
            dif = recent['MACD_DIF'].iloc[-1]
            dea = recent['MACD_DEA'].iloc[-1]
            macd_bar = recent['MACD_BAR'].iloc[-1]

            if dif > dea and macd_bar > 0:
                # Golden cross or bullish
                macd_score = 30
            elif dif < dea and macd_bar < 0:
                # Death cross or bearish
                macd_score = 5
            elif dif > dea:
                # Above signal but bearish momentum
                macd_score = 20
            elif dif < dea:
                # Below signal but bullish momentum
                macd_score = 15
            else:
                macd_score = 20  # Neutral
        except (KeyError, ValueError):
            macd_score = 20.0

        # 3. BOLL Position Score (30 points)
        boll_score = 0.0
        try:
            close = recent['close'].iloc[-1]
            boll_upper = recent['BOLL_UPPER'].iloc[-1]
            boll_mid = recent['BOLL_MID'].iloc[-1]
            boll_lower = recent['BOLL_LOWER'].iloc[-1]

            # Calculate position within bands (0-100)
            band_width = boll_upper - boll_lower
            position = (close - boll_lower) / band_width * 100

            if position > 80:
                boll_score = 30  # Near upper band - bullish
            elif position > 60:
                boll_score = 25  # Upper region
            elif position > 40:
                boll_score = 20  # Middle region
            elif position > 20:
                boll_score = 15  # Lower region
            else:
                boll_score = 10  # Near lower band - bearish
        except (KeyError, ValueError):
            boll_score = 20.0

        trend_score = ma_score + macd_score + boll_score
        return min(max(trend_score, 0), 100)

    def calculate_momentum_score(self, df: pd.DataFrame, lookback: int = 30) -> float:
        """
        Calculate momentum score based on RSI, KDJ, MOM, ROC.

        Returns: Score 0-100
        """
        if len(df) < lookback:
            return 50.0

        recent = df.tail(lookback)

        # 1. RSI Score (40 points)
        rsi_score = 0.0
        try:
            rsi12 = recent['RSI12'].iloc[-1]

            # Convert RSI to 0-100 score
            # RSI 50 = neutral (50 points)
            # RSI > 70 = overbought (reduce points)
            # RSI < 30 = oversold (reduce points slightly)
            # RSI 50-70 = strong (more points)
            if rsi12 > 70:
                # Overbought - reduce score
                rsi_score = 40 - (rsi12 - 70) * 1.5
            elif rsi12 < 30:
                # Oversold - slightly reduce
                rsi_score = 40 - (30 - rsi12) * 0.5
            elif rsi12 >= 50 and rsi12 <= 70:
                # Strong zone - increase score
                rsi_score = 40 + (rsi12 - 50) * 1.0
            elif rsi12 >= 40 and rsi12 < 50:
                # Slightly bullish
                rsi_score = 35 + (rsi12 - 40) * 0.5
            else:
                # Neutral to weak
                rsi_score = rsi12 * 0.7
        except (KeyError, ValueError):
            rsi_score = 20.0

        rsi_score = min(max(rsi_score, 0), 40)

        # 2. KDJ Score (30 points)
        kdj_score = 0.0
        try:
            kdj_j = recent['KDJ_J'].iloc[-1]

            # J-value analysis
            if kdj_j > 100:
                kdj_score = 10  # Overheated - bearish
            elif kdj_j > 80:
                kdj_score = 25  # Strong momentum - good
            elif kdj_j > 50:
                kdj_score = 30  # Strong - very good
            elif kdj_j > 20:
                kdj_score = 25  # Moderate
            elif kdj_j > 0:
                kdj_score = 15  # Weak
            else:
                kdj_score = 5   # Very weak - bearish
        except (KeyError, ValueError):
            kdj_score = 20.0

        kdj_score = min(max(kdj_score, 0), 30)

        # 3. MOM/ROC Score (30 points)
        mom_score = 0.0
        try:
            mom = recent['MOM'].iloc[-1]
            roc12 = recent['ROC12'].iloc[-1]

            # Normalize MOM and ROC
            mom_score_adj = np.clip(mom / 10.0 * 15, -10, 15) + 10
            roc_score_adj = np.clip(roc12 / 2.0 * 15, -10, 15) + 10

            mom_score = (mom_score_adj + roc_score_adj) / 2
        except (KeyError, ValueError):
            mom_score = 15.0

        momentum_score = rsi_score + kdj_score + mom_score
        return min(max(momentum_score, 0), 100)

    def calculate_money_flow_score(self, df: pd.DataFrame, lookback: int = 20) -> float:
        """
        Calculate money flow score based on OBV, VR, volume.

        Returns: Score 0-100
        """
        if len(df) < lookback:
            return 50.0

        recent = df.tail(lookback)

        # 1. OBV Trend Score (50 points)
        obv_score = 0.0
        try:
            obv_start = recent['OBV'].iloc[0]
            obv_end = recent['OBV'].iloc[-1]
            obv_change = obv_end - obv_start

            # Normalize OBV change
            # Significant inflow = high score
            # Significant outflow = low score
            avg_volume = recent['volume'].mean()
            normalized_change = obv_change / (avg_volume * 100)  # Normalize by volume

            if normalized_change > 2.0:
                obv_score = 50  # Strong inflow
            elif normalized_change > 1.0:
                obv_score = 40  # Moderate inflow
            elif normalized_change > 0:
                obv_score = 30  # Slight inflow
            elif normalized_change > -1.0:
                obv_score = 20  # Slight outflow
            elif normalized_change > -2.0:
                obv_score = 10  # Moderate outflow
            else:
                obv_score = 0   # Strong outflow
        except (KeyError, ValueError):
            obv_score = 25.0

        # 2. VR Score (30 points)
        vr_score = 0.0
        try:
            vr = recent['VR'].iloc[-1]

            if vr > 150:
                vr_score = 30  # High VR - strong inflow
            elif vr > 100:
                vr_score = 25  # Moderate
            elif vr > 70:
                vr_score = 20  # Neutral
            elif vr > 50:
                vr_score = 15  # Slight outflow
            else:
                vr_score = 10  # Strong outflow
        except (KeyError, ValueError):
            vr_score = 20.0

        # 3. Volume Change Score (20 points)
        volume_score = 0.0
        try:
            recent_volume = recent['volume'].iloc[-1]
            avg_volume = recent['volume'].iloc[:-1].mean()

            volume_ratio = recent_volume / avg_volume

            if volume_ratio > 2.0:
                volume_score = 20  # High volume spike
            elif volume_ratio > 1.5:
                volume_score = 18  # Elevated volume
            elif volume_ratio > 1.2:
                volume_score = 15  # Slightly elevated
            elif volume_ratio > 0.8:
                volume_score = 10  # Normal
            else:
                volume_score = 5   # Low volume
        except (KeyError, ValueError):
            volume_score = 10.0

        money_flow_score = obv_score + vr_score + volume_score
        return min(max(money_flow_score, 0), 100)

    def calculate_sentiment_score(self, df: pd.DataFrame, lookback: int = 10) -> float:
        """
        Calculate sentiment score based on consecutive days, amplitude.

        Returns: Score 0-100
        """
        if len(df) < lookback:
            return 50.0

        recent = df.tail(lookback)

        # 1. Consecutive Up/Down Days Score (50 points)
        consecutive_score = 0.0
        try:
            # Count consecutive up/down days
            changes = df['close'].diff().tail(lookback - 1)

            consecutive_up = 0
            consecutive_down = 0

            # Count from most recent
            for change in reversed(changes):
                if change > 0:
                    consecutive_up += 1
                    if consecutive_down > 0:
                        break
                elif change < 0:
                    consecutive_down += 1
                    if consecutive_up > 0:
                        break

            # Score based on consecutive movement
            if consecutive_up >= 3:
                consecutive_score = 50  # Strong bullish sentiment
            elif consecutive_up >= 2:
                consecutive_score = 40
            elif consecutive_up == 1:
                consecutive_score = 30
            elif consecutive_down >= 3:
                consecutive_score = 0   # Strong bearish sentiment
            elif consecutive_down >= 2:
                consecutive_score = 10
            elif consecutive_down == 1:
                consecutive_score = 20
            else:
                consecutive_score = 25  # Mixed/sideways
        except (KeyError, ValueError):
            consecutive_score = 25.0

        # 2. Amplitude Score (30 points)
        amplitude_score = 0.0
        try:
            high = recent['high'].max()
            low = recent['low'].min()
            amplitude = (high - low) / recent['close'].iloc[0] * 100

            # High amplitude means volatile
            if amplitude > 10:
                amplitude_score = 30  # High volatility - high risk
            elif amplitude > 7:
                amplitude_score = 25
            elif amplitude > 5:
                amplitude_score = 20
            elif amplitude > 3:
                amplitude_score = 15
            else:
                amplitude_score = 10  # Low volatility - stable
        except (KeyError, ValueError):
            amplitude_score = 20.0

        # 3. Recent Performance Score (20 points)
        performance_score = 0.0
        try:
            start_price = recent['close'].iloc[0]
            end_price = recent['close'].iloc[-1]
            return_pct = (end_price - start_price) / start_price * 100

            if return_pct > 10:
                performance_score = 20  # Strong recent performance
            elif return_pct > 5:
                performance_score = 18
            elif return_pct > 0:
                performance_score = 15
            elif return_pct > -5:
                performance_score = 10
            elif return_pct > -10:
                performance_score = 5
            else:
                performance_score = 0   # Very poor performance
        except (KeyError, ValueError):
            performance_score = 10.0

        sentiment_score = consecutive_score + amplitude_score + performance_score
        return min(max(sentiment_score, 0), 100)

    def calculate_total_score(self, df: pd.DataFrame) -> dict:
        """
        Calculate comprehensive stock score.

        Returns: Dictionary with all scores
        """
        print("\n" + "="*50)
        print("📊 CALCULATING STOCK SCORE")
        print("="*50)

        # Calculate individual dimension scores
        trend = self.calculate_trend_score(df)
        momentum = self.calculate_momentum_score(df)
        money_flow = self.calculate_money_flow_score(df)
        sentiment = self.calculate_sentiment_score(df)

        # Calculate weighted total
        total = (
            trend * self.trend_weight +
            momentum * self.momentum_weight +
            money_flow * self.money_flow_weight +
            sentiment * self.sentiment_weight
        )

        # Determine level
        if total >= 90:
            level = "强烈买入"
            level_emoji = "🟢🟢"
        elif total >= 80:
            level = "买入"
            level_emoji = "🟢"
        elif total >= 60:
            level = "持有可能"
            level_emoji = "🟡"
        elif total >= 40:
            level = "观望"
            level_emoji = "🟡"
        else:
            level = "卖出"
            level_emoji = "🔴"

        result = {
            'total_score': total,
            'trend_score': trend,
            'momentum_score': momentum,
            'money_flow_score': money_flow,
            'sentiment_score': sentiment,
            'level': level,
            'level_emoji': level_emoji,
            'weights': {
                'trend': self.trend_weight,
                'momentum': self.momentum_weight,
                'money_flow': self.money_flow_weight,
                'sentiment': self.sentiment_weight
            }
        }

        return result


def load_data(input_file: str) -> pd.DataFrame:
    """Load indicators data from CSV file."""
    print(f"📥 Loading data from {input_file}")

    try:
        df = pd.read_csv(input_file)

        # Check required columns
        required_cols = ['date', 'close', 'volume']
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"❌ Error: Missing required columns: {missing_cols}")
            return pd.DataFrame()

        print(f"✅ Loaded {len(df)} records")
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()


def save_scores(result: dict, df: pd.DataFrame, output_file: str):
    """Save scores to CSV file."""
    try:
        # Create scores DataFrame
        scores_data = {
            'date': df['date'].iloc[-1],
            'close': df['close'].iloc[-1],
            'total_score': result['total_score'],
            'trend_score': result['trend_score'],
            'momentum_score': result['momentum_score'],
            'money_flow_score': result['money_flow_score'],
            'sentiment_score': result['sentiment_score'],
            'trend_weight': result['weights']['trend'],
            'momentum_weight': result['weights']['momentum'],
            'money_flow_weight': result['weights']['money_flow'],
            'sentiment_weight': result['weights']['sentiment'],
            'level': result['level'],
            'level_emoji': result['level_emoji']
        }

        scores_df = pd.DataFrame([scores_data])
        scores_df.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"\n✅ Scores saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error saving scores: {e}")


def print_score_report(result: dict, df: pd.DataFrame):
    """Print detailed score report."""
    print("\n" + "="*50)
    print("📊 STOCK SCORE REPORT")
    print("="*50)

    # Print individual scores
    print("\n📋 Dimension Scores:")
    print(f"\n   趋势 (Trend)      | Score: {result['trend_score']:>6.1f}/100 | "
          f"Weight: {result['weights']['trend']*100:>4.0f}% | "
          f"Contribution: {result['trend_score']*result['weights']['trend']:>5.1f}")

    print(f"   动量 (Momentum)   | Score: {result['momentum_score']:>6.1f}/100 | "
          f"Weight: {result['weights']['momentum']*100:>4.0f}% | "
          f"Contribution: {result['momentum_score']*result['weights']['momentum']:>5.1f}")

    print(f"   资金 (Money Flow) | Score: {result['money_flow_score']:>6.1f}/100 | "
          f"Weight: {result['weights']['money_flow']*100:>4.0f}% | "
          f"Contribution: {result['money_flow_score']*result['weights']['money_flow']:>5.1f}")

    print(f"   情绪 (Sentiment)  | Score: {result['sentiment_score']:>6.1f}/100 | "
          f"Weight: {result['weights']['sentiment']*100:>4.0f}% | "
          f"Contribution: {result['sentiment_score']*result['weights']['sentiment']:>5.1f}")

    # Print total score
    print("\n" + "-"*50)
    print(f"\n   综合评分 (Total Score): {result['total_score']:>6.1f}/100")
    print(f"   等级 (Level): {result['level_emoji']} {result['level']}")
    print(f"   当前价格: {df['close'].iloc[-1]:.2f}元")
    print(f"   分析日期: {df['date'].iloc[-1]}")


def parse_weights(weights_str: str) -> dict:
    """Parse custom weights from string."""
    weights = {
        'trend': 0.4,
        'momentum': 0.3,
        'money_flow': 0.2,
        'sentiment': 0.1
    }

    if not weights_str:
        return weights

    try:
        for item in weights_str.split(','):
            key, value = item.split('=')
            key = key.strip().lower()
            value = float(value.strip())

            if key in weights:
                weights[key] = value
    except:
        print("⚠️  Warning: Invalid weights format, using defaults")

    return weights


def main():
    parser = argparse.ArgumentParser(
        description="Calculate comprehensive stock score",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Input CSV file with indicators'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='scores.csv',
        help='Output CSV file for scores (default: scores.csv)'
    )

    parser.add_argument(
        '--weights',
        type=str,
        default=None,
        help='Custom weights (format: trend=0.4,momentum=0.3,...)'
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

    # Parse custom weights if provided
    weights = parse_weights(args.weights)

    # Initialize scorer
    scorer = StockScorer(
        trend_weight=weights['trend'],
        momentum_weight=weights['momentum'],
        money_flow_weight=weights['money_flow'],
        sentiment_weight=weights['sentiment']
    )

    # Calculate scores
    result = scorer.calculate_total_score(df)

    # Save scores
    save_scores(result, df, args.output)

    # Print report
    if not args.quiet:
        print_score_report(result, df)

    return 0


if __name__ == '__main__':
    sys.exit(main())
