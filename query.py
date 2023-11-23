from connection import Database

class Query:
    def __init__(self):
        self.query=Database()

    def join_1(self):
        self.query.connect_db()

        # 연구자와 보호 프로그램에 대한 조인 쿼리
        join_query = """
        SELECT Researcher.FirstName, Researcher.LastName, Researcher.Affiliation,
            ConservationProgram.Name as ProgramName, StartDate, EndDate, Description
        FROM Researcher
        JOIN ObservationRecord ON Researcher.ResearcherID = ObservationRecord.ResearcherID
        JOIN ConservationProgram ON ObservationRecord.ProgramID = ConservationProgram.ProgramID;
        """
        # 조인 쿼리 실행
        self.query.cur.execute(join_query)

        # 결과 가져오기
        result = self.query.cur.fetchall()

        # 결과 출력
        for row in result:
            print(row)
        
        self.query.close_db()

    def join_2(self):
        self.query.connect_db()

        # 종과 서식지에 대한 조인 쿼리
        join_query = """
        SELECT Species.Name as SpeciesName, Family, ConservationStatus, Habitat.Name as HabitatName, Location, Climate
        FROM Species
        JOIN ObservationRecord ON Species.SpeciesID = ObservationRecord.SpeciesID
        JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID;
        """

        # 조인 쿼리 실행
        self.query.cur.execute(join_query)

        # 결과 가져오기
        result = self.query.cur.fetchall()

        # 결과 출력
        for row in result:
            print(row)
        
        self.query.close_db()