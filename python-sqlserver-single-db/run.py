import DatabaseExecutor as DB
import getpass


server_name = input("Enter Server Name: ")
database = input("Enter Database Name: ")
username = input('Enter Username: ')
password = getpass.getpass(prompt="Enter Password: ") 
folder_path = input("Enter the folder in which the script files are located: ")

server_url = server_name + ".database.windows.net"
executor = DB.DatabaseExecutor(server_url, database, username, password)
executor.execute_sql_from_folder(folder_path)

