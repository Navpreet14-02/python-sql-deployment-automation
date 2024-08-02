import sys
import backup as Backup

if __name__ == "__main__":

    server = sys.argv[1]
    database = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    table_name = sys.argv[5]

    Backup.BackupDB(server, database, username, password, table_name)
