#!/bin/bash

echo "===================================================="
echo "CLI interface for trendsniper"
echo "===================================================="
echo ""
read -p "Ticker: " ticker
read -p "Timeframe (e.g., D1, W1, M1): " interval
read -p "Initial Date (YYYY-MM-DD): " initial_date
read -p "End Date (YYYY-MM-DD): " end_date
echo ""
echo "Adding arguments for the search ?"
echo "Available options: --guppy --macd --atr --adr --cbl --show-raw-data"
read additional_args
if [ -n "$additional_args" ]; then
    additional_args=" $additional_args"
fi
echo ""
echo "Processing your request..."
python trendsniper.py ${ticker} ${interval} ${initial_date} ${end_date} ${additional_args}
