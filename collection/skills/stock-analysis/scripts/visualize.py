#!/usr/bin/env python3
"""
Stock Visualization Script for Stock Analysis

Generates various charts including K-line, indicators, and composite dashboards.

Usage:
    python visualize.py --input indicators.csv --charts kline,macd,kdj
    python visualize.py --input indicators.csv --output charts/ --theme light
"""

import argparse
import sys
import os
from datetime import datetime

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.font_manager import FontProperties

    # Set Chinese font
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
except ImportError as e:
    print(f"❌ Error: Required library not installed: {e}")
    print("   Run: pip install pandas matplotlib")
    sys.exit(1)


class StockVisualizer:
    """Stock data visualization."""

    def __init__(self, theme='light', width=1200, height=600):
        """Initialize visualizer."""
        self.theme = theme
        self.width = width
        self.height = height

        # Set theme colors
        if theme == 'dark':
            self.bg_color = '#1e1e1e'
            self.grid_color = '#333333'
            self.text_color = '#ffffff'
            self.up_color = '#00cc44'
            self.down_color = '#ff3333'
        else:  # light theme
            self.bg_color = '#ffffff'
            self.grid_color = '#e0e0e0'
            self.text_color = '#333333'
            self.up_color = '#00aa00'
            self.down_color = '#cc0000'

    def plot_kline_with_ma(self, df: pd.DataFrame, output_path: str):
        """Plot K-line with moving averages."""
        print(f"📊 Generating K-line with MA chart...")

        if len(df) < 10:
            print("⚠️  Warning: Insufficient data for K-line chart")
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(self.width/100, self.height/100*2),
                                          gridspec_kw={'height_ratios': [3, 1]})
        fig.patch.set_facecolor(self.bg_color)

        # Plot K-line (candlestick)
        for i in range(len(df)):
            if pd.isna(df.iloc[i]['open']):
                continue

            date = pd.to_datetime(df.iloc[i]['date'])
            open_price = df.iloc[i]['open']
            close_price = df.iloc[i]['close']
            high_price = df.iloc[i]['high']
            low_price = df.iloc[i]['low']

            color = self.up_color if close_price >= open_price else self.down_color

            # Draw candlestick
            ax1.vlines(x=date, ymin=low_price, ymax=high_price,
                        colors=color, linewidth=1)
            ax1.bar(x=date, height=abs(close_price - open_price),
                     bottom=min(open_price, close_price),
                     width=1, color=color, alpha=0.8)

        # Plot MA lines
        ax1.plot(df['date'], df['MA5'], label='MA5', color='#ff6b6b',
                 linewidth=1.5, alpha=0.8)
        ax1.plot(df['date'], df['MA10'], label='MA10', color='#4ecdc4',
                 linewidth=1.5, alpha=0.8)
        ax1.plot(df['date'], df['MA20'], label='MA20', color='#f1c40f',
                 linewidth=1.5, alpha=0.8)
        ax1.plot(df['date'], df['MA60'], label='MA60', color='#3498db',
                 linewidth=1.5, alpha=0.8)

        ax1.set_ylabel('Price', color=self.text_color)
        ax1.set_title('K-Line with Moving Averages', color=self.text_color)
        ax1.legend(loc='upper left')
        ax1.grid(True, color=self.grid_color, alpha=0.3)
        ax1.tick_params(colors=self.text_color)

        # Plot volume
        ax2.bar(df['date'], df['volume'], color=self.up_color, alpha=0.5)
        ax2.set_ylabel('Volume', color=self.text_color)
        ax2.grid(True, color=self.grid_color, alpha=0.3)
        ax2.tick_params(colors=self.text_color)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ K-line chart saved: {output_path}")

    def plot_macd(self, df: pd.DataFrame, output_path: str):
        """Plot MACD indicator."""
        print(f"📊 Generating MACD chart...")

        if len(df) < 12:
            print("⚠️  Warning: Insufficient data for MACD")
            return

        fig, ax = plt.subplots(figsize=(self.width/100, self.height/100))
        fig.patch.set_facecolor(self.bg_color)

        # Plot MACD lines
        ax.plot(df['date'], df['MACD_DIF'], label='DIF',
                 color='#ff6b6b', linewidth=1.5)
        ax.plot(df['date'], df['MACD_DEA'], label='DEA',
                 color='#4ecdc4', linewidth=1.5)

        # Plot histogram
        colors = [self.up_color if x >= 0 else self.down_color
                  for x in df['MACD_BAR']]
        ax.bar(df['date'], df['MACD_BAR'], color=colors, alpha=0.5)

        ax.set_ylabel('MACD', color=self.text_color)
        ax.set_title('MACD (12, 26, 9)', color=self.text_color)
        ax.legend(loc='upper left')
        ax.axhline(y=0, color=self.grid_color, linestyle='--', alpha=0.5)
        ax.grid(True, color=self.grid_color, alpha=0.3)
        ax.tick_params(colors=self.text_color)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ MACD chart saved: {output_path}")

    def plot_kdj(self, df: pd.DataFrame, output_path: str):
        """Plot KDJ indicator."""
        print(f"📊 Generating KDJ chart...")

        if len(df) < 9:
            print("⚠️  Warning: Insufficient data for KDJ")
            return

        fig, ax = plt.subplots(figsize=(self.width/100, self.height/100))
        fig.patch.set_facecolor(self.bg_color)

        # Plot KDJ lines
        ax.plot(df['date'], df['KDJ_K'], label='K',
                 color='#f1c40f', linewidth=1.5)
        ax.plot(df['date'], df['KDJ_D'], label='D',
                 color='#3498db', linewidth=1.5)
        ax.plot(df['date'], df['KDJ_J'], label='J',
                 color='#e74c3c', linewidth=1.5)

        # Add overbought/oversold zones
        ax.axhline(y=80, color=self.down_color, linestyle='--',
                   alpha=0.3, label='Overbought (80)')
        ax.axhline(y=20, color=self.up_color, linestyle='--',
                   alpha=0.3, label='Oversold (20)')

        ax.set_ylabel('KDJ', color=self.text_color)
        ax.set_title('KDJ (9, 3, 3)', color=self.text_color)
        ax.legend(loc='upper left')
        ax.grid(True, color=self.grid_color, alpha=0.3)
        ax.tick_params(colors=self.text_color)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ KDJ chart saved: {output_path}")

    def plot_rsi(self, df: pd.DataFrame, output_path: str):
        """Plot RSI indicator."""
        print(f"📊 Generating RSI chart...")

        if len(df) < 6:
            print("⚠️  Warning: Insufficient data for RSI")
            return

        fig, ax = plt.subplots(figsize=(self.width/100, self.height/100))
        fig.patch.set_facecolor(self.bg_color)

        # Plot RSI lines
        ax.plot(df['date'], df['RSI6'], label='RSI6',
                 color='#f1c40f', linewidth=1.5, alpha=0.7)
        ax.plot(df['date'], df['RSI12'], label='RSI12',
                 color='#3498db', linewidth=1.5)
        ax.plot(df['date'], df['RSI24'], label='RSI24',
                 color='#00aa00', linewidth=1.5, alpha=0.7)

        # Add overbought/oversold zones
        ax.axhspan(ymin=70, ymax=100, color=self.down_color, alpha=0.1)
        ax.axhline(y=70, color=self.down_color, linestyle='--',
                   alpha=0.3, label='Overbought (70)')
        ax.axhspan(ymin=0, ymax=30, color=self.up_color, alpha=0.1)
        ax.axhline(y=30, color=self.up_color, linestyle='--',
                   alpha=0.3, label='Oversold (30)')

        ax.set_ylim(0, 100)
        ax.set_ylabel('RSI', color=self.text_color)
        ax.set_title('RSI (6, 12, 24)', color=self.text_color)
        ax.legend(loc='upper left')
        ax.grid(True, color=self.grid_color, alpha=0.3)
        ax.tick_params(colors=self.text_color)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ RSI chart saved: {output_path}")

    def plot_boll(self, df: pd.DataFrame, output_path: str):
        """Plot Bollinger Bands."""
        print(f"📊 Generating Bollinger Bands chart...")

        if len(df) < 20:
            print("⚠️  Warning: Insufficient data for BOLL")
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(self.width/100, self.height/100*2),
                                          gridspec_kw={'height_ratios': [3, 1]})
        fig.patch.set_facecolor(self.bg_color)

        # Plot K-line
        for i in range(len(df)):
            if pd.isna(df.iloc[i]['open']):
                continue

            date = pd.to_datetime(df.iloc[i]['date'])
            open_price = df.iloc[i]['open']
            close_price = df.iloc[i]['close']
            high_price = df.iloc[i]['high']
            low_price = df.iloc[i]['low']

            color = self.up_color if close_price >= open_price else self.down_color
            ax1.bar(x=date, height=abs(close_price - open_price),
                     bottom=min(open_price, close_price),
                     width=1, color=color, alpha=0.8)

        # Plot Bollinger Bands
        ax1.plot(df['date'], df['BOLL_UPPER'], label='BOLL Upper',
                 color='#e74c3c', linewidth=1.5, alpha=0.6)
        ax1.plot(df['date'], df['BOLL_MID'], label='BOLL Mid',
                 color='#3498db', linewidth=1.5, alpha=0.6)
        ax1.plot(df['date'], df['BOLL_LOWER'], label='BOLL Lower',
                 color='#00aa00', linewidth=1.5, alpha=0.6)

        ax1.set_ylabel('Price', color=self.text_color)
        ax1.set_title('K-Line with Bollinger Bands (20, 2)',
                      color=self.text_color)
        ax1.legend(loc='upper left')
        ax1.grid(True, color=self.grid_color, alpha=0.3)
        ax1.tick_params(colors=self.text_color)

        # Plot volume
        ax2.bar(df['date'], df['volume'], color=self.up_color, alpha=0.5)
        ax2.set_ylabel('Volume', color=self.text_color)
        ax2.grid(True, color=self.grid_color, alpha=0.3)
        ax2.tick_params(colors=self.text_color)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ Bollinger Bands chart saved: {output_path}")

    def plot_composite(self, df: pd.DataFrame, output_path: str):
        """Plot composite dashboard with multiple panels."""
        print(f"📊 Generating composite dashboard...")

        if len(df) < 30:
            print("⚠️  Warning: Insufficient data for composite chart")
            return

        fig = plt.figure(figsize=(self.width/100, self.height/100*2))
        fig.patch.set_facecolor(self.bg_color)

        # Create subplots
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.2)

        ax1 = fig.add_subplot(gs[0, :])  # K-line with MA
        ax2 = fig.add_subplot(gs[1, 0])  # MACD
        ax3 = fig.add_subplot(gs[1, 1])  # KDJ
        ax4 = fig.add_subplot(gs[2, 0])  # RSI
        ax5 = fig.add_subplot(gs[2, 1])  # Volume

        # Plot K-line
        for i in range(len(df)):
            if pd.isna(df.iloc[i]['open']):
                continue

            date = pd.to_datetime(df.iloc[i]['date'])
            open_price = df.iloc[i]['open']
            close_price = df.iloc[i]['close']
            high_price = df.iloc[i]['high']
            low_price = df.iloc[i]['low']

            color = self.up_color if close_price >= open_price else self.down_color
            ax1.bar(x=date, height=abs(close_price - open_price),
                     bottom=min(open_price, close_price),
                     width=1, color=color, alpha=0.8)

        ax1.plot(df['date'], df['MA20'], label='MA20',
                 color='#f1c40f', linewidth=1.5)
        ax1.plot(df['date'], df['MA60'], label='MA60',
                 color='#3498db', linewidth=1.5)
        ax1.set_title('K-Line with MA', color=self.text_color)
        ax1.legend(loc='upper left', fontsize=8)
        ax1.grid(True, color=self.grid_color, alpha=0.3)
        ax1.tick_params(colors=self.text_color, labelsize=8)

        # Plot MACD
        ax2.plot(df['date'], df['MACD_DIF'], label='DIF',
                 color='#ff6b6b', linewidth=1.5)
        ax2.plot(df['date'], df['MACD_DEA'], label='DEA',
                 color='#4ecdc4', linewidth=1.5)
        ax2.axhline(y=0, color=self.grid_color, linestyle='--', alpha=0.5)
        ax2.set_title('MACD', color=self.text_color)
        ax2.legend(loc='upper left', fontsize=8)
        ax2.grid(True, color=self.grid_color, alpha=0.3)
        ax2.tick_params(colors=self.text_color, labelsize=8)

        # Plot KDJ
        ax3.plot(df['date'], df['KDJ_K'], label='K',
                 color='#f1c40f', linewidth=1.5)
        ax3.plot(df['date'], df['KDJ_J'], label='J',
                 color='#e74c3c', linewidth=1.5)
        ax3.axhline(y=80, color=self.down_color, linestyle='--', alpha=0.3)
        ax3.axhline(y=20, color=self.up_color, linestyle='--', alpha=0.3)
        ax3.set_title('KDJ', color=self.text_color)
        ax3.legend(loc='upper left', fontsize=8)
        ax3.grid(True, color=self.grid_color, alpha=0.3)
        ax3.tick_params(colors=self.text_color, labelsize=8)

        # Plot RSI
        ax4.plot(df['date'], df['RSI12'], label='RSI12',
                 color='#3498db', linewidth=1.5)
        ax4.axhspan(ymin=70, ymax=100, color=self.down_color, alpha=0.1)
        ax4.axhline(y=70, color=self.down_color, linestyle='--', alpha=0.3)
        ax4.axhspan(ymin=0, ymax=30, color=self.up_color, alpha=0.1)
        ax4.axhline(y=30, color=self.up_color, linestyle='--', alpha=0.3)
        ax4.set_ylim(0, 100)
        ax4.set_title('RSI', color=self.text_color)
        ax4.legend(loc='upper left', fontsize=8)
        ax4.grid(True, color=self.grid_color, alpha=0.3)
        ax4.tick_params(colors=self.text_color, labelsize=8)

        # Plot volume
        ax5.bar(df['date'], df['volume'], color=self.up_color, alpha=0.5)
        ax5.set_title('Volume', color=self.text_color)
        ax5.grid(True, color=self.grid_color, alpha=0.3)
        ax5.tick_params(colors=self.text_color, labelsize=8)

        plt.tight_layout()
        plt.savefig(output_path, facecolor=self.bg_color, dpi=150,
                    bbox_inches='tight')
        plt.close()

        print(f"✅ Composite dashboard saved: {output_path}")


def load_data(input_file: str) -> pd.DataFrame:
    """Load indicators data from CSV file."""
    print(f"📥 Loading data from {input_file}")

    try:
        df = pd.read_csv(input_file)

        # Convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        print(f"✅ Loaded {len(df)} records")
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()


def ensure_output_dir(output_path: str):
    """Ensure output directory exists."""
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created output directory: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate stock analysis charts",
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
        default='charts',
        help='Output directory for charts (default: charts/)'
    )

    parser.add_argument(
        '--charts',
        type=str,
        default='all',
        help='Comma-separated list of charts (default: all)'
    )

    parser.add_argument(
        '--theme',
        type=str,
        default='light',
        choices=['light', 'dark'],
        help='Chart theme (default: light)'
    )

    parser.add_argument(
        '--width',
        type=int,
        default=1200,
        help='Chart width in pixels (default: 1200)'
    )

    parser.add_argument(
        '--height',
        type=int,
        default=600,
        help='Chart height in pixels (default: 600)'
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

    # Initialize visualizer
    visualizer = StockVisualizer(
        theme=args.theme,
        width=args.width,
        height=args.height
    )

    # Ensure output directory
    ensure_output_dir(args.output)

    # Determine which charts to generate
    if args.charts == 'all':
        charts = ['kline_ma', 'macd', 'kdj', 'rsi', 'boll', 'composite']
    else:
        charts = [c.strip() for c in args.charts.split(',')]

    # Generate charts
    print("\n" + "="*50)
    print("📊 GENERATING CHARTS")
    print("="*50 + "\n")

    for chart_type in charts:
        try:
            if chart_type == 'kline_ma':
                output_path = f"{args.output}/kline_ma.png"
                visualizer.plot_kline_with_ma(df, output_path)

            elif chart_type == 'macd':
                output_path = f"{args.output}/macd.png"
                visualizer.plot_macd(df, output_path)

            elif chart_type == 'kdj':
                output_path = f"{args.output}/kdj.png"
                visualizer.plot_kdj(df, output_path)

            elif chart_type == 'rsi':
                output_path = f"{args.output}/rsi.png"
                visualizer.plot_rsi(df, output_path)

            elif chart_type == 'boll':
                output_path = f"{args.output}/boll.png"
                visualizer.plot_boll(df, output_path)

            elif chart_type == 'composite':
                output_path = f"{args.output}/composite.png"
                visualizer.plot_composite(df, output_path)

            else:
                print(f"⚠️  Unknown chart type: {chart_type}")

        except Exception as e:
            print(f"❌ Error generating {chart_type}: {e}")

    print("\n✅ Chart generation complete!")
    print(f"   Output directory: {args.output}")
    print(f"   Charts generated: {len(charts)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
