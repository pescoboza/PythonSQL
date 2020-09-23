import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode

load_dotenv()

config = {
    "user": os.environ.get("USER"),
    "password": os.environ.get("PASSWORD"),
    "host": os.environ.get("HOST"),
    "database": os.environ.get("DATABASE")
}

for k, v in config.items():
    if v == None:
        raise ValueError("Configuration attribute {} was None.".format(k))


def connect(config=config):
    try:
        return mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("ERROR Database does not exist")
            else:
                print("ERROR {}".format(err))
            exit()


def main():
    db = connect()
    cursor = db.cursor()
    while True:
        user_input = input("pysql>")
        if user_input in ("quit", "exit"):
            db.close()
            break
        cursor.execute(user_input)

        print(cursor.column_names)
        for v in cursor:
            print(v)
    print("Bye-bye!")


if __name__ == "__main__":
    main()
