
class JoinQuery:
    # 종(Species)와 서식지(Habitat) 정보를 함께 가져오는 쿼리
    join_species_habitat = """
    SELECT Species.Name AS SpeciesName, Species.Family, Species.ConservationStatus,
           Habitat.Name AS HabitatName, Habitat.Location, Habitat.Climate, Habitat.Area
    FROM Species
    INNER JOIN ObservationRecord ON Species.SpeciesID = ObservationRecord.SpeciesID
    INNER JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID;
    """

    # 관찰 기록(ObservationRecord)과 연구원(Researcher) 정보를 함께 가져오는 쿼리
    join_observation_researcher = """
    SELECT ObservationRecord.RecordID, ObservationRecord.ObservationDate, ObservationRecord.Notes,
           Researcher.FirstName, Researcher.LastName, Researcher.Affiliation
    FROM ObservationRecord
    INNER JOIN Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID;
    """
    
    #종(Species), 서식지(Habitat), 연구원(Researcher) 정보를 함께 가져오는 쿼리
    join_species_habitat_researcher = """
    SELECT Species.Name AS SpeciesName, Species.Family, Species.ConservationStatus,
           Habitat.Name AS HabitatName, Habitat.Location, Habitat.Climate, Habitat.Area,
           Researcher.FirstName, Researcher.LastName, Researcher.Affiliation
    FROM Species
    INNER JOIN ObservationRecord ON Species.SpeciesID = ObservationRecord.SpeciesID
    INNER JOIN Habitat ON ObservationRecord.HabitatID = Habitat.HabitatID
    INNER JOIN Researcher ON ObservationRecord.ResearcherID = Researcher.ResearcherID;
    """