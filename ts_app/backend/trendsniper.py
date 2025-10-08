#!/usr/bin/env python
import sys 
import json
from lib.data_enricher import DataEnricher
from lib.data_visualizer import DataVisualizer 
from lib.data_normalizer import DataNormalizer
from lib.context import ContextLoader 
from lib.cli_handler import CLIHandler

def parse_input_from_cli_request(sys):

    try:
        cloader = ContextLoader()
        cloader.load_context()
        cli_handler = CLIHandler()
        context = cli_handler.get_context_from_cmd_line(sys, cloader.context)
        run(context)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

def parse_input_from_backend_request(ticker_data, options_list):
    try:
        cloader = ContextLoader()
        context = cloader.add_to_context("ticker_data", ticker_data)

        if ticker_data.get("end_period") is None or ticker_data.get("end_period") == "":
            from datetime import datetime, timedelta
            tomorrow = datetime.now() + timedelta(days=1)
            ticker_data["end_period"] = tomorrow.strftime("%Y-%m-%d")

        context = cloader.add_to_context("options_list", options_list)
        context = cloader.add_to_context("is_backend_request", True)
        return run(context)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

def run(context):

    try:
        # Get the data from MetaTrader 5 and normalize it
        d_normalizer = DataNormalizer()
        normalized_data = d_normalizer.execute(context)
        
        # Enrich the data with additional indicators
        d_enricher = DataEnricher()
        enriched_normalized_data  = d_enricher.execute(context, normalized_data)

        if "json" in context["options_list"]:
            return enriched_normalized_data
        else:
            # Visualize the data
            d_visual = DataVisualizer()
            result = d_visual.execute(context, enriched_normalized_data)
            
            if result != None:
                return result

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    parse_input_from_cli_request(sys)
