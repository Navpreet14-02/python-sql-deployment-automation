import pyodbc
from datetime import date

def BackupDB(server_name, database, username, password, table_name):
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database};UID={username};PWD={password}"
    try:
        print("Executing Backup Function:")
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            today = date.today().strftime("%Y_%m_%d")
            backup_table_name = f"{table_name}_backup_{today}"
            
            backup_query = f"""
            SELECT * INTO {backup_table_name}
            FROM {table_name};
            """
            print(f"Executing query: {backup_query}")
            
            try:
                cursor.execute(backup_query)
                conn.commit()
                print("Backup completed successfully.")
            except pyodbc.Error as err:
                print(f"Error while creating backup: {err}")
                # conn.rollback()

    except pyodbc.Error as err:
        print(f"Database Connection could not be established: {err}")
