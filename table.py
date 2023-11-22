# 스키마 변경 모듈

class Table():

    # 테이블 생성 쿼리 작성
    create_species_table = """
    CREATE TABLE Species (
        SpeciesID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Family VARCHAR(255),
        ConservationStatus VARCHAR(50)
    );
    """

    create_habitat_table = """
    CREATE TABLE Habitat (
        HabitatID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Location VARCHAR(255),
        Climate VARCHAR(50),
        Area FLOAT
    );
    """

    create_observation_record_table = """
    CREATE TABLE ObservationRecord (
        RecordID INT AUTO_INCREMENT PRIMARY KEY,
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

    create_researcher_table = """
    CREATE TABLE Researcher (
        ResearcherID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Affiliation VARCHAR(255)
    );
    """

    create_conservation_program_table = """
    CREATE TABLE ConservationProgram (
        ProgramID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        StartDate DATE,
        EndDate DATE,
        Description TEXT
    );
    """

       

