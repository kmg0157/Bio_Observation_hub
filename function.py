import pymysql
from table import Table
from data import Data
from join import JoinQuery
import pandas as pd

class Database:
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",port=3306,user="root",password="0157",db="bio_observation_hub",charset="utf8")   #DB 연결
        self.cur=self.conn.cursor() #커서 생성
        
    # DB 연결 종료
    def close_db(self):
        self.conn.commit()  #테이블 변경사항 저장
        self.cur.close()    #커서 종료
        self.conn.close()   #DB 접속 종료
        print('DataBase Saved & Closed')

    #table 생성(동작 good~)
    def create_table(self):
        self.cur.execute(Table.create_researcher_table)
        self.cur.execute(Table.create_conservation_program_table)
        self.cur.execute(Table.create_species_table)
        self.cur.execute(Table.create_habitat_table)
        self.cur.execute(Table.create_observation_record_table)
        print('Created Table')

    #table 삭제(동작 good~)
    def drop_table(self, table_name):
        drop_query = f"DROP TABLE IF EXISTS {table_name}"
        self.cur.execute(drop_query)
        print('Droped Table!')

    #data 삽입
    def insert_data(self):
        insert_species="INSERT INTO Species (SpeciesID, Name, Family, ConservationStatus) VALUES (%s, %s, %s, %s)"
        self.cur.executemany(insert_species,Data.species_data)
        insert_habitat="INSERT INTO Habitat (HabitatID, Name, Location, Climate, Area) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(insert_habitat, Data.habitat_data)
        insert_researcher = "INSERT INTO Researcher (ResearcherID, FirstName, LastName, Affiliation) VALUES (%s, %s, %s, %s)"
        self.cur.executemany(insert_researcher,Data.researcher_data)
        insert_program = "INSERT INTO ConservationProgram (ProgramID, Name, StartDate, EndDate, Description) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(insert_program,Data.program_data)
        insert_record = "INSERT INTO ObservationRecord (RecordID, SpeciesID, HabitatID, ResearcherID, ObservationDate, Notes) VALUES (%s, %s, %s, %s ,%s, %s)"
        self.cur.executemany(insert_record,Data.observation_data)
        self.conn.commit()

    #조인 1
    def join1(self):
        self.cur.execute(JoinQuery.join_species_habitat)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)

    #조인 2
    def join2(self):
        self.cur.execute(JoinQuery.join_observation_researcher)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)
    
    #조인 3
    def join3(self):
        self.cur.execute(JoinQuery.join_species_habitat_researcher)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)