import pyodbc
from datetime import date

def BackupDB(server_name,database,username,password):
    connection_string = f'Driver={{SQL Server}};Server={server_name};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    # try:
    print("Backup Function Executing:")
    with pyodbc.connect(connection_string) as conn:
        cursor=conn.cursor()
        today = date.today()
        backup_query = f"SELECT * FROM {database} INTO {database+f"-{date.isoformat(today)}"}"

        # try:
        cursor.execute(backup_query)
        conn.commit()
        # except pyodbc.Error as err:
        #     print(f"Error while creating backup: {err}")
        #     quit()

        print(backup_query)

    # except pyodbc.Error as err:
    #     print(f"Database Connection could not be established: {err}")







