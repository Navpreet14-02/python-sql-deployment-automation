import backup as Backup
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--server-name",
    type=str,
    required=True,
    default=False,
    help="Name of the server on which queries need to be run"
)
parser.add_argument(
    "--database-name",
    type=str,
    required=True,
    default=False,
    help="Name of the database on which queries need to be run"
)
parser.add_argument(
    "--username",
    type=str,
    required=True,
    default=False,
    help="Username for the connection with Server"
)
parser.add_argument(
    "--password",
    type=str,
    required=True,
    default=False,
    help="Password for the connection with server"
)
parser.add_argument(
    "--table-name",
    type=str,
    required=True,
    default=False,
    help="Name of the table on which queries need to be run"
)



if __name__ == "__main__":

    args = parser.parse_args()

    server = args.server_name
    database = args.database_name
    username = args.username
    password = args.password
    table_name = args.table_name

    Backup.BackupDB(server, database, username, password, table_name)
