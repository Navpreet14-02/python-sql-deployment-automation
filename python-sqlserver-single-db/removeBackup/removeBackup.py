import pyodbc
from datetime import date

def RemoveBackup(server_name, database, username, password, table_name):
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database};UID={username};PWD={password}"

    try:
        print("Removing Backup:")
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            today = date.today().strftime("%Y_%m_%d")
            backup_table_name = f"{table_name}_backup_{today}"
            
            remove_backup_query = f"""
            DROP TABLE {backup_table_name}
            """
            print(f"Executing query: {remove_backup_query}")
            
            try:
                cursor.execute(remove_backup_query)
                conn.commit()
                print("Backup Removed successfully.")
            except pyodbc.Error as err:
                print(f"Error while Removing Backup: {err}")
                # conn.rollback()

    except pyodbc.Error as err:
        print(f"Database Connection could not be established: {err}")