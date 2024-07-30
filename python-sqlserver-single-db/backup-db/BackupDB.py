import pyodbc
import sys
# import FileLogger
# from datetime import date

# logger = FileLogger()

server_name = sys.argv[1] 
database = sys.argv[2]  
username = sys.argv[3] 
password = sys.argv[4] 
folder_path = sys.argv[5]  


connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={server_name};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )


def BackupDB():
    try:
        print("Backup Function Executed:")
        # with pyodbc.connect(connection_string) as conn:
        #     cursor=conn.cursor()
        #     today = date.today()
        #     backup_query = f"SELECT * FROM {database} INTO {database+f"{date.isoformat(today)}"}"
        #     cursor.execute(backup_query)
        #     conn.commit()
    except pyodbc.Error as err:
        print(f"Failed to take backup: {err}")



BackupDB()




