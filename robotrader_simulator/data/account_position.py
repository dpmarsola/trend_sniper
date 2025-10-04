import sqlite3
import data.parms as parms

def insert_account_position_data(account_data):
    
    try:
        with sqlite3.connect(f'./data/{parms.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'INSERT INTO {parms.ACCOUNT_POSITION_TABLE} VALUES (:account_id, :account_name, :cash_position, :simulation_id)', account_data)
            conn.commit()
            return result
    except Exception as e:
        print(e)

def select_account_position_data_by_id(id):
    
    try:
        with sqlite3.connect(f'./data/{parms.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'SELECT * FROM {parms.ACCOUNT_POSITION_TABLE} WHERE account_id = :account_id', {"account_id" : id})
            conn.commit()
            return result.fetchone()
    except Exception as e:
        print(e)

def select_account_position_data_by_simulation_id(id):
    
    try:
        with sqlite3.connect(f'./data/{parms.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'SELECT * FROM {parms.ACCOUNT_POSITION_TABLE} WHERE simulation_id = :simulation_id', {"simulation_id" : id})
            conn.commit()
            return result.fetchone()
    except Exception as e:
        print(e)
    