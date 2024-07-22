import DatabaseExecutor as DB
import sys


server_name = sys.argv[1] 
database = sys.argv[2]  
username = sys.argv[3] 
password = sys.argv[4] 
folder_path = sys.argv[5]  

server_url = server_name + ".database.windows.net"
# server_url = server_name
executor = DB.DatabaseExecutor(server_url, database, username, password)
executor.execute_sql_from_folder(folder_path)

