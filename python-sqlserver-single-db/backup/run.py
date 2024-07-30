import sys
import BackupDB as Backup

if __name__ == "__main__":

    server = sys.argv[1]
    database = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    
    Backup.BackupDB(server, database, username, password)