import pymysql
from table import Table
from data import Data
from join import JoinQuery
from query import Query
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
        self.cur.execute(Table.create_conservation_program_table)
        self.cur.execute(Table.create_researcher_table)
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
        insert_program = "INSERT INTO ConservationProgram (ProgramID, Name, StartDate, EndDate, Description) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(insert_program,Data.program_data)
        insert_researcher = "INSERT INTO Researcher (ResearcherID, ProgramID, FirstName, LastName, Affiliation) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(insert_researcher,Data.researcher_data)
        insert_record = "INSERT INTO ObservationRecord (RecordID, SpeciesID, HabitatID, ResearcherID, ObservationDate, Notes) VALUES (%s, %s, %s, %s ,%s, %s)"
        self.cur.executemany(insert_record,Data.observation_data)
        self.conn.commit()


    #조인 1
    def join1(self):
        self.cur.execute(JoinQuery.query1)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)

        response=input('Do you wanna save joined result? (yes/no) :')
        if response=='yes':
            result_df.to_csv('joined_result1.csv',index=False)
            print('Saved in joined_result1.csv')
        else:
            print('not saved TT')

    #조인 2
    def join2(self):
        self.cur.execute(JoinQuery.query2)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)
        response=input('Do you wanna save joined result? (yes/no) :')
        if response=='yes':
            result_df.to_csv('joined_result2.csv',index=False)
            print('Saved in joined_result2.csv')
        else:
            print('not saved TT')
    
    #조인 3
    def join3(self):
        self.cur.execute(JoinQuery.query3)
        result=self.cur.fetchall()
        columns=[desc[0] for desc in self.cur.description]
        result_df=pd.DataFrame(result,columns=columns)

        print(result_df)
        response=input('Do you wanna save joined result? (yes/no) :')
        if response=='yes':
            result_df.to_csv('joined_result3.csv',index=False)
            print('Saved in joined_result3.csv')
        else:
            print('not saved TT')

    #쿼리1(서브쿼리1)
    def query1(self):
        df_query1 = pd.read_sql_query(Query.query1, self.conn)
        print(df_query1)

    #쿼리2(서브쿼리2)
    def query2(self):
        df_query2 = pd.read_sql_query(Query.query2, self.conn)
        print(df_query2)

    #쿼리3(서브쿼리3)
    def query3(self):
        df_query3 = pd.read_sql_query(Query.query3, self.conn)
        print(df_query3)

    #쿼리4(서브쿼리4)
    def query4(self):
        df_query4 = pd.read_sql_query(Query.query4, self.conn)
        print(df_query4)

    #쿼리5(집계서브쿼리1)
    def query5(self):
        df_query5 = pd.read_sql_query(Query.query5, self.conn)
        print(df_query5)

    #쿼리6(집계서브쿼리2)
    def query6(self):
        df_query6 = pd.read_sql_query(Query.query6, self.conn)
        print(df_query6)

    #쿼리7(집계서브쿼리3)
    def query7(self):
        df_query7 = pd.read_sql_query(Query.query7, self.conn)
        print(df_query7)

    #쿼리8(집계서브쿼리4)
    def query8(self):
        df_query8 = pd.read_sql_query(Query.query8, self.conn)
        print(df_query8)



    