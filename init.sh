#!/bin/bash

## get args from command line
SERVICE=$1
if [ -z "$SERVICE" ]; then
    echo " "
    echo "No service specified. Usage: ./init.sh <service> [args]"
    echo " "
    echo "Available services: server, cli"
    echo " "
    echo "For server, provide the following argument:"
    echo "  Port: The port number for the server (e.g., 8000)"  
    echo " "
    echo "For CLI, provide the following arguments:"
    echo "  Ticker: The stock ticker symbol (e.g., AAPL)"
    echo "  Timeframe: The time interval for the data (e.g., 1m, 5m, 1d)"
    echo "  Initial Date: The start date for the data (YYYY-MM-DD)"
    echo "  End Date: The end date for the data (YYYY-MM-DD)"
    exit 1
fi

if [ "$SERVICE" != "server" ] && [ "$SERVICE" != "cli" ]; then
    echo "Invalid service specified. Use 'server' or 'cli'."
    exit 1
fi

if [ "$SERVICE" == "server" ]; then
    echo "Starting server..."
    python manage.py runserver $2
elif [ "$SERVICE" == "cli" ]; then
    echo "Starting CLI..."
    cd ts_app/backend || exit
    ./cli.sh
fi