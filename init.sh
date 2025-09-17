#!/bin/bash

current_dir=$(pwd)
export PYTHONPATH="$current_dir/venv/Lib/site-packages:$current_dir/ts_app/backend:$PYTHONPATH"

## Create a venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
    flag_created_venv=true
fi

## Activate the venv
## If this is a git bash shell on Windows, use source venv/Scripts/activate
## Otherwise, use source venv/bin/activate
if [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

if [ "$flag_created_venv" = true ]; then
    echo "Virtual environment created and activated."
    echo "Installing required packages..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "Virtual environment activated."
fi

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

## lowercase the service name
SERVICE=$(echo "$SERVICE" | tr '[:upper:]' '[:lower:]')

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