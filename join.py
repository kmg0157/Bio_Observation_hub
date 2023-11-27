
class JoinQuery:
    # 종(Species)와 서식지(Habitat), 관찰기록(ObservationRecord) 정보를 함께 가져오는 쿼리
    query1 = """
    SELECT DISTINCT *
    FROM ObservationRecord
    JOIN Species ON ObservationRecord.SpeciesID = Species.SpeciesID
    JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID;
    """

    # 관찰 기록(ObservationRecord)과 연구원(Researcher) 정보를 함께 가져오는 쿼리
    query2 = """
    SELECT DISTINCT *
    FROM ObservationRecord
    JOIN Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID;
    """
    
    #연구원(Researcher)과 프로그램(ConservationProgram) 정보를 함께 가져오는 쿼리
    query3 = """
    SELECT DISTINCT *
    FROM Researcher
    JOIN ConservationProgram ON Researcher.ProgramID = ConservationProgram.ProgramID;
    """

    