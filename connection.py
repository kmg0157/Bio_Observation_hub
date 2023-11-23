import pymysql
from table import Table
from data import Data

class Database:
    def __init__(self):
        self.conn=None
        self.cur=None

    # 생성해둔 DB 접속
    def connect_db(self):
        self.conn=pymysql.connect(host="localhost",port=3306,user="root",password="0157",db="bio_observation_hub",charset="utf8")   #DB 연결
        self.cur=self.conn.cursor() #커서 생성
        print('DataBase Connected!')

    # DB 연결 종료
    def close_db(self):
        self.conn.commit()  #테이블 변경사항 저장
        self.cur.close()    #커서 종료
        self.conn.close()   #DB 접속 종료
        print('DataBase Saved & Closed')

    #table 생성
    def create_table(self):
        self.cur.execute(Table.create_species_table)
        self.cur.execute(Table.create_habitat_table)
        self.cur.execute(Table.create_observation_record_table)
        self.cur.execute(Table.create_researcher_table)
        self.cur.execute(Table.create_conservation_program_table)
        print('Created Table')

    #table 삭제
    def drop_table(self, table_name):
        drop_query = f"DROP TABLE IF EXISTS {table_name}"
        self.cur.execute(drop_query)
        print('Droped Table!')

    #data 삽입
    def insert_data(self):
        insert_species_query = "INSERT INTO Species (Name, Family, ConservationStatus) VALUES (%s, %s, %s)"
        self.cur.executemany(insert_species_query, Data.species_data)

        insert_habitat_query = "INSERT INTO Habitat (Name, Location, Climate, Area) VALUES (%s, %s, %s, %s)"
        self.cur.executemany(insert_habitat_query, Data.habitat_data)

        insert_researcher_query = "INSERT INTO Researcher (FirstName, LastName, Affiliation) VALUES (%s, %s, %s)"
        self.cur.executemany(insert_researcher_query, Data.researcher_data)

        insert_program_query = "INSERT INTO ConservationProgram (Name, StartDate, EndDate, Description) VALUES (%s, %s, %s, %s)"
        self.cur.executemany(insert_program_query, Data.program_data)

        insert_observation_query = "INSERT INTO ObservationRecord (SpeciesID, HabitatID, ResearcherID, ObservationDate, Notes) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(insert_observation_query, Data.observation_data)
        
        print('Insert Complate!')
        self.conn.commit()