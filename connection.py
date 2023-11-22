import pymysql
from table import Table

class Database:
    def __init__(self):
        self.conn=None
        self.cur=None

    # 생성해둔 DB 접속
    def connect_db(self):
        self.conn=pymysql.connect(host="localhost",port=3306,user="root",password="0157",db="bio_observation_hub",charset="utf8")   #DB 연결
        self.cur=self.conn.cursor() #커서 생성
        print('')

    # DB 연결 종료
    def close_db(self):
        self.conn.commit()  #테이블 변경사항 저장
        self.cur.close()    #커서 종료
        self.conn.close()   #DB 접속 종료

    #table 생성
    def create_table(self):
        self.cur.execute(Table.create_species_table)
        self.cur.execute(Table.create_habitat_table)
        self.cur.execute(Table.create_observation_record_table)
        self.cur.execute(Table.create_researcher_table)
        self.cur.execute(Table.create_conservation_program_table)

    #table 삭제
    def drop_table(self, table_name):
        drop_query = f"DROP TABLE IF EXISTS {table_name}"
        self.cur.execute(drop_query)

    #data 삽입
    def insert_data():
        