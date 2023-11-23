# 스키마 변경 모듈

class Table():

    # 테이블 생성 쿼리 작성
    create_species_table = """
    CREATE TABLE IF NOT EXISTS Species (
        SpeciesID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Family VARCHAR(255),
        ConservationStatus VARCHAR(50)
    );
    """

    create_habitat_table = """
    CREATE TABLE IF NOT EXISTS Habitat (
        HabitatID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Location VARCHAR(255),
        Climate VARCHAR(50),
        Area FLOAT
    );
    """

    create_researcher_table = """
    CREATE TABLE IF NOT EXISTS Researcher (
        ResearcherID INT PRIMARY KEY,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Affiliation VARCHAR(255)
    );
    """

    create_conservation_program_table = """
    CREATE TABLE IF NOT EXISTS ConservationProgram (
        ProgramID INT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        StartDate DATE,
        EndDate DATE,
        Description TEXT
    );
    """

    create_observation_record_table = """
    CREATE TABLE IF NOT EXISTS ObservationRecord (
        RecordID INT PRIMARY KEY,
        SpeciesID INT,
        HabitatID INT,
        ResearcherID INT,
        ObservationDate DATE,
        Notes TEXT,
        FOREIGN KEY (SpeciesID) REFERENCES Species(SpeciesID),
        FOREIGN KEY (HabitatID) REFERENCES Habitat(HabitatID),
        FOREIGN KEY (ResearcherID) REFERENCES Researcher(ResearcherID)
    );
    """

