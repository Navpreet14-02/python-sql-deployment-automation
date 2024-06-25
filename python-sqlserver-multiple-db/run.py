import DatabaseExecutor as DB
import getpass


server_name = input("Enter Server Name: ")
database_count = int(input("Enter the number of databases you want to execute the query on: "))
databases = []

for i in range(1,database_count+1):
    db = input(f"Enter database {i} name: ")
    databases.append(db)

        
username = input('Enter Username: ')
password = getpass.getpass(prompt="Enter Password: ") 
folder_path = input("Enter the folder in which the script files are located: ")

server_url = server_name + ".database.windows.net"
executor = DB.DatabaseExecutor(server_url, databases, username, password)
executor.execute_sql_from_folder(folder_path)

