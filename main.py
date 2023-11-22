from connection import Database

def main():
    bio_db=Database()

    #DB 연결
    bio_db.connect_db()
    
    #테이블 생성
    bio_db.create_table()   #생성되는 테이블은 table.py 참조 및 변경 가능

    #테이블 삭제
    table_to_drop = "your_table"    #이 부분 사용자 입력으로 바꿔야함
    bio_db.drop_table(table_to_drop)
    
    #DB 종료
    bio_db.close_db()


if __name__=="__main__":
    main()