
class JoinQuery:
    # 종(Species)와 서식지(Habitat) 정보를 함께 가져오는 쿼리
    query1 = """
    SELECT Species.Name AS SpeciesName, Species.Family, Species.ConservationStatus,
           Habitat.Name AS HabitatName, Habitat.Location, Habitat.Climate, Habitat.Area
    FROM Species
    LEFT JOIN ObservationRecord ON Species.SpeciesID = ObservationRecord.SpeciesID
    LEFT JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID;
    """

    # 관찰 기록(ObservationRecord)과 연구원(Researcher) 정보를 함께 가져오는 쿼리
    query2 = """
    SELECT
    ObservationRecord.RecordID,
    Researcher.FirstName,
    Researcher.LastName,
    ObservationRecord.ObservationDate,
    ObservationRecord.Notes
    FROM
    ObservationRecord
    JOIN
    Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID;
    """
    
    #종(Species), 서식지(Habitat), 연구원(Researcher) 정보를 함께 가져오는 쿼리
    query3 = """
    SELECT Species.Name AS SpeciesName, Species.Family, Species.ConservationStatus,
           Habitat.Name AS HabitatName, Habitat.Location, Habitat.Climate, Habitat.Area,
           Researcher.FirstName, Researcher.LastName, Researcher.Affiliation
    FROM Species
    INNER JOIN ObservationRecord ON Species.SpeciesID = ObservationRecord.SpeciesID
    INNER JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID
    INNER JOIN Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID;
    """