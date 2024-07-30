import sys
from BackupDB import Backup

if __name__ == "__main__":

    server = sys.argv[1]
    database = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    
    server_url = server + ".database.windows.net"
    backup_executor = Backup(server_url, database, username, password)
    backup_executor.BackupDB()