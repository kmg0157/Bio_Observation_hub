class Query:

    #종(Species)의 관측 기록(Observation Record) 조회 쿼리    
    query1="""
    SELECT * FROM ObservationRecord
    WHERE SpeciesID IN (
        SELECT SpeciesID 
        FROM Species 
        WHERE Name = 'Amur Leopard'
        );
    """

    #특정 서식지(Habitat)에서 관측된 기록 조회 쿼리    
    query2="""
    SELECT * 
    FROM ObservationRecord
    WHERE HabitatID IN (
        SELECT HabitatID 
        FROM Habitat 
        WHERE Name = 'Madagascar Forest'
        );
    """

    #특정 연구자(Researcher)가 수행한 관측 기록 조회 쿼리    
    query3="""
    SELECT * 
    FROM ObservationRecord
    WHERE ResearcherID IN (
        SELECT ResearcherID 
        FROM Researcher 
        WHERE FirstName = 'Jessica' AND LastName = 'Park'
        );
    """

    #특정 보전 프로그램(Conservation Program)에 참여한 연구자 조회 쿼리   
    query4="""
    SELECT * 
    FROM Researcher
    WHERE ProgramID IN (
        SELECT ProgramID 
        FROM ConservationProgram 
        WHERE Name = 'Panda Habitat Restoration'
        );
    """

    #종(Species)별로 관측된 횟수와 전체 넓이의 합을 계산하는 쿼리   
    query5="""
    SELECT Species.Name, COUNT(*) as ObservationCount, SUM(Habitat.Area) as TotalArea
    FROM ObservationRecord
    JOIN Species ON ObservationRecord.SpeciesID = Species.SpeciesID
    JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID
    GROUP BY Species.Name;
    """

    #서식지(Habitat)별로 관측된 횟수와 해당 서식지의 최대 넓이를 계산하는 쿼리   
    query6="""
    SELECT Habitat.Name, COUNT(*) as ObservationCount, MAX(Habitat.Area) as MaxArea
    FROM ObservationRecord
    JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID
    GROUP BY Habitat.Name;
    """

    #연구자(Researcher)별로 수행한 관측 횟수와 해당 연구자의 관측 기록의 평균 넓이를 계산하는 쿼리   
    query7="""
    SELECT CONCAT(Researcher.FirstName, ' ', Researcher.LastName) as ResearcherName, COUNT(*) as ObservationCount, AVG(Habitat.Area) as AvgArea
    FROM ObservationRecord
    JOIN Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID
    JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID
    GROUP BY ResearcherName;
    """

    #보전 프로그램(Conservation Program)별로 참여한 연구자 수와 프로그램의 평균 기간을 계산하는 쿼리   
    query8="""
    SELECT ConservationProgram.Name, COUNT(DISTINCT Researcher.ResearcherID) as ResearcherCount, AVG(DATEDIFF(ConservationProgram.EndDate, ConservationProgram.StartDate)) as AvgProgramDuration
    FROM ConservationProgram
    JOIN Researcher ON ConservationProgram.ProgramID = Researcher.ProgramID
    GROUP BY ConservationProgram.Name;
    """