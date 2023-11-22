from connection import Database

def main():
    database=Database()

    database.connect_db()


if __name__=="__main__":
    main()