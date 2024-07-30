import sys
from BackupDB import Backup

if __name__ == "__main__":

    server = sys.argv[1]
    database = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    
    backup_executor = Backup(server, database, username, password)
    backup_executor.BackupDB()