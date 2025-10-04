import sqlite3
import data.parms as parms

def insert_simulation_data(simulation_data):
    
    try:
        with sqlite3.connect(f'./data/{parms.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'INSERT INTO {parms.SIMULATION_TABLE} VALUES (:simulation_id, :cycle_start, :cycle_end, :frequency, :asset_under_simulation, :initial_balance, :current_balance)', simulation_data)
            conn.commit()
            return result
    except Exception as e:
        print(e)

def select_simulation_data_by_id(id):
    
    try:
        with sqlite3.connect(f'./data/{parms.DATABASE_NAME}') as conn:
            cursor = conn.cursor()
            result = cursor.execute(f'SELECT * FROM {parms.SIMULATION_TABLE} WHERE simulation_id = :simulation', {"simulation" : id})
            conn.commit()
            return result.fetchone()
    except Exception as e:
        print(e)
    