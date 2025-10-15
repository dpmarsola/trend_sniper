import sqlite3
import constants
from datetime import datetime

def select_market_data_by_period(asset, period):
    
    datetime_obj = period.to_pydatetime().strftime("%Y-%m-%d %H:%M:%S.000000")
    
    try:
        with sqlite3.connect(f'./data/{constants.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'SELECT * FROM {constants.MARKET_DATA_TABLE} WHERE asset = :asset and datetime = :datetime', {"asset" : asset, "datetime" : datetime_obj})
            conn.commit()
            return result.fetchone()
    except Exception as e:
        print(e)