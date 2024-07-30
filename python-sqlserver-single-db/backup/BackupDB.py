import pyodbc
from datetime import date



class Backup:
    def __init__(self,server_name,database,username,password):
        self.__connection_string = f'Driver={{SQL Server}};Server={server_name};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        self.database = database

    def BackupDB(self):
        # connection_string = f'Driver={{SQL Server}};Server={server_name};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        try:
            print("Backup Function Executing:")
            with pyodbc.connect(self.__connection_string) as conn:
                cursor=conn.cursor()
                today = date.today()
                backup_query = f"SELECT * FROM {self.database} INTO {self.database+f"-{date.isoformat(today)}"}"
                print(backup_query)

                try:
                    cursor.execute(backup_query)
                    conn.commit()
                except pyodbc.Error as err:
                    print(f"Error while creating backup: {err}")
                    quit()
        except pyodbc.Error as err:
            print(f"Database Connection could not be established: {err}")







