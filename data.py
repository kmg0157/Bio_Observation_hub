from datetime import datetime

class Data:
    # 종 데이터
    species_data = [
    ("Bengal Tiger", "Felidae", "Endangered"),
    ("Giant Panda", "Ursidae", "Vulnerable"),
    ("African Elephant", "Elephantidae", "Vulnerable"),
    ("Red-crowned Crane", "Gruidae", "Endangered"),
    ("Amur Leopard", "Felidae", "Critically Endangered"),
    ("Sumatran Orangutan", "Hominidae", "Critically Endangered"),
    ("Hawksbill Turtle", "Cheloniidae", "Critically Endangered"),
    ("California Condor", "Cathartidae", "Critically Endangered"),
    ("Snow Leopard", "Felidae", "Vulnerable"),
    ("Western Lowland Gorilla", "Hominidae", "Critically Endangered")
    ]

    # 서식지 데이터
    habitat_data = [
    ("Amazon Rainforest", "South America", "Tropical", 6700000),
    ("Great Barrier Reef", "Australia", "Tropical", 344400),
    ("Serengeti Plain", "Africa", "Savannah", 30000),
    ("Himalayan Mountains", "Asia", "Alpine", 2400000),
    ("Everglades", "United States", "Subtropical", 2300000),
    ("Galápagos Islands", "Ecuador", "Arid", 7880),
    ("Arctic Tundra", "Arctic Circle", "Polar", 8500000),
    ("Patagonian Desert", "Argentina", "Desert", 673000),
    ("Madagascar Forest", "Madagascar", "Tropical", 587000),
    ("Boreal Forest", "Canada", "Boreal", 8500000)
    ]
    
    # 연구자 데이터 삽입
    researcher_data = [
    ("John", "Smith", "Wildlife Conservation Institute"),
    ("Emily", "Johnson", "Serengeti Wildlife Foundation"),
    ("David", "Kim", "Galápagos Research Society"),
    ("Lisa", "Rodriguez", "Arctic Wildlife Fund"),
    ("Michael", "Lee", "Primate Protection Organization"),
    ("Sarah", "Brown", "Panda Preservation Project"),
    ("Robert", "Chen", "Crane Conservation Society"),
    ("Olivia", "Wang", "Orangutan Alliance"),
    ("Daniel", "Garcia", "Condor Conservation Coalition"),
    ("Jessica", "Park", "Snow Leopard Trust")
    ]
    
    # 보호 프로그램 데이터 삽입
    program_data = [   
    ("Bengal Tiger Conservation", "2022-01-01", "2023-12-31", "A program to protect and preserve Bengal Tigers."),
    ("Panda Habitat Restoration", "2022-02-15", "2023-12-31", "Restoration efforts for habitats of Giant Pandas."),
    ("Elephant Migration Study", "2022-03-20", "2023-12-31", "Studying the migration patterns of African Elephants."),
    ("Crane Nesting Protection", "2022-04-10", "2023-12-31", "Protecting nesting areas of Red-crowned Cranes."),
    ("Leopard Islands Preservation", "2022-05-05", "2023-12-31", "Preserving the unique ecosystem of the Galápagos Islands."),
    ("Orangutan Habitat Conservation", "2022-06-30", "2023-12-31", "Conservation of habitats for Sumatran Orangutans."),
    ("Turtle Arctic Awareness", "2022-07-15", "2023-12-31", "Raising awareness for the protection of Arctic Turtles."),
    ("Condor Fly Free Initiative", "2022-08-01", "2023-12-31", "Efforts to protect and rehabilitate California Condors."),
    ("Snow Leopard Monitoring", "2022-09-05", "2023-12-31", "Monitoring the population and habitats of Snow Leopards."),
    ("Gorilla Protection Project", "2022-10-10", "2023-12-31", "Protecting Western Lowland Gorillas in their natural habitat.")
    ]
    
    # 관찰 기록 데이터 삽입
    observation_data = [
    (1, 1, 1, 101, datetime(2023, 1, 15), "Observed a Bengal Tiger hunting in the rainforest."),
    (2, 3, 3, 102, datetime(2023, 2, 2), "Elephants migrating across the Serengeti."),
    (3, 5, 6, 103, datetime(2023, 3, 10), "Amur Leopards spotted on the Galápagos Islands."),
    (4, 7, 7, 104, datetime(2023, 4, 5), "Hawksbill Turtle nesting in the Arctic Tundra."),
    (5, 10, 9, 105, datetime(2023, 5, 20), "Western Lowland Gorilla family observed in Madagascar."),
    (6, 2, 2, 106, datetime(2023, 6, 18), "Giant Pandas feeding on bamboo in the Great Barrier Reef."),
    (7, 4, 4, 107, datetime(2023, 7, 22), "Red-crowned Cranes flying over the Himalayan Mountains."),
    (8, 6, 5, 108, datetime(2023, 8, 30), "Sumatran Orangutans playing in the Everglades."),
    (9, 8, 8, 109, datetime(2023, 9, 14), "California Condors soaring over the Patagonian Desert."),
    (10, 9, 10, 110, datetime(2023, 10, 5), "Snow Leopards resting in the Boreal Forest.")
    ]
