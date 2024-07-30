import os
import pyodbc

class DatabaseExecutor:
    def __init__(self, server, database, username, password):
        self.__connection_string = f'Driver={{SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        print(server)
        print(database)
        print(username)
        print(password)


    def get_database_tables(self):
        with pyodbc.connect(self.__connection_string) as conn:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM sys.tables")
            tables = cursor.fetchall()
            for row in tables:
                print(row)


    def execute_sql_from_file(self, file_path):
        with pyodbc.connect(self.__connection_string) as conn:
            cursor=conn.cursor()
            with open(file_path,'r') as file:
                sql_script = file.read()
                print(sql_script)
                cursor.execute(sql_script)
                conn.commit()

    def execute_sql_from_folder(self, folder_path):  
        try:
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.sql'):
                    file_path = os.path.join(folder_path, file_name)
                    try:
                        # self.get_database_tables()
                        self.execute_sql_from_file(file_path)
                        # self.get_database_tables()
                    except pyodbc.Error as err:
                        print(f"An error occurred while running the query in the file {file_name}. \n")
                        print(f"Error: {err}")
                        print("Stopping the Program...") 
                        quit()

        except Exception as error:
            print(f"Error occurred: {error}")

                


                         
