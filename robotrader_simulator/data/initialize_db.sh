rm ../robotrader.db 2> /dev/null
sqlite3 robotrader.db < scripts/create_tables.sql