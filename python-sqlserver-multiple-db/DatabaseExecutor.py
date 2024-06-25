import os
import pyodbc

class DatabaseExecutor:
    def __init__(self, server, databases, username, password):
        self.server=server
        self.databases=databases
        self.username=username
        self.password=password

        # self.__connection_string = f'Driver={{ODBC Driver 18 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'


    def generate_db_conn_string(self,database):
        connection_string = f'Driver={{ODBC Driver 18 for SQL Server}};Server={self.server};Database={database};Uid={self.username};Pwd={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        return connection_string
    
    def execute_sql_from_file(self, file_path,conn_string):
        with pyodbc.connect(self.__connection_string) as conn:
            cursor=conn.cursor()
            with open(file_path,'r') as file:
                sql_script = file.read()
                cursor.execute(sql_script)
                conn.commit()

    def execute_sql_from_folder(self, folder_path,databases):

        for database in databases:
            database_path = os.path.join(folder_path,database)

            for file_name in os.listdir(database_path):
                if file_name.endswith('.sql'):
                    file_path = os.path.join(folder_path, file_name)
                    self.execute_sql_from_file(file_path)