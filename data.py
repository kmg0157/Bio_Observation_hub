class Data:
    # 종 데이터
    species_data = [
    (1, "Bengal Tiger", "Felidae", "Endangered"),
    (2, "Giant Panda", "Ursidae", "Vulnerable"),
    (3, "African Elephant", "Elephantidae", "Vulnerable"),
    (4, "Red-crowned Crane", "Gruidae", "Endangered"),
    (5, "Amur Leopard", "Felidae", "Critically Endangered"),
    (6, "Sumatran Orangutan", "Hominidae", "Critically Endangered"),
    (7, "Hawksbill Turtle", "Cheloniidae", "Critically Endangered"),
    (8, "California Condor", "Cathartidae", "Critically Endangered"),
    (9, "Snow Leopard", "Felidae", "Vulnerable"),
    (10, "Western Lowland Gorilla", "Hominidae", "Critically Endangered")
    ]

    # 서식지 데이터
    habitat_data = [
    (11, "Amazon Rainforest", "South America", "Tropical", 6700000),
    (12, "Great Barrier Reef", "Australia", "Tropical", 344400),
    (13, "Serengeti Plain", "Africa", "Savannah", 30000),
    (14, "Himalayan Mountains", "Asia", "Alpine", 2400000),
    (15, "Everglades", "United States", "Subtropical", 2300000),
    (16, "Galápagos Islands", "Ecuador", "Arid", 7880),
    (17, "Arctic Tundra", "Arctic Circle", "Polar", 8500000),
    (18, "Patagonian Desert", "Argentina", "Desert", 673000),
    (19, "Madagascar Forest", "Madagascar", "Tropical", 587000),
    (20, "Boreal Forest", "Canada", "Boreal", 8500000)
    ]
    
    # 연구자 데이터 삽입
    researcher_data = [
    (21, 35, "John", "Smith", "Wildlife Conservation Institute"),
    (22, 34, "Emily", "Johnson", "Serengeti Wildlife Foundation"),
    (23, 38, "David", "Kim", "Galapagos Research Society"),
    (24, 31, "Lisa", "Rodriguez", "Arctic Wildlife Fund"),
    (25, 32, "Michael", "Lee", "Primate Protection Organization"),
    (26, 37, "Sarah", "Brown", "Panda Preservation Project"),
    (27, 36,"Robert", "Chen", "Crane Conservation Society"),
    (28, 40, "Olivia", "Wang", "Orangutan Alliance"),
    (29, 33, "Daniel", "Garcia", "Condor Conservation Coalition"),
    (30, 39, "Jessica", "Park", "Snow Leopard Trust")
    ]
    
    # 보호 프로그램 데이터 삽입
    program_data = [   
    (31, "Bengal Tiger Conservation", "2022-01-01", "2023-12-31", "A program to protect and preserve Bengal Tigers."),
    (32, "Panda Habitat Restoration", "2022-02-15", "2023-12-31", "Restoration efforts for habitats of Giant Pandas."),
    (33, "Elephant Migration Study", "2022-03-20", "2023-12-31", "Studying the migration patterns of African Elephants."),
    (34, "Crane Nesting Protection", "2022-04-10", "2023-12-31", "Protecting nesting areas of Red-crowned Cranes."),
    (35, "Leopard Islands Preservation", "2022-05-05", "2023-12-31", "Preserving the unique ecosystem of the Galápagos Islands."),
    (36, "Orangutan Habitat Conservation", "2022-06-30", "2023-12-31", "Conservation of habitats for Sumatran Orangutans."),
    (37, "Turtle Arctic Awareness", "2022-07-15", "2023-12-31", "Raising awareness for the protection of Arctic Turtles."),
    (38, "Condor Fly Free Initiative", "2022-08-01", "2023-12-31", "Efforts to protect and rehabilitate California Condors."),
    (39, "Snow Leopard Monitoring", "2022-09-05", "2023-12-31", "Monitoring the population and habitats of Snow Leopards."),
    (40, "Gorilla Protection Project", "2022-10-10", "2023-12-31", "Protecting Western Lowland Gorillas in their natural habitat.")
    ]
    
    # 관찰 기록 데이터 삽입
    observation_data = [
    (101, 1, 11, 21, "2023-01-15", "Observed a Bengal Tiger hunting in the rainforest."),
    (102, 3, 13, 22, "2023-02-02", "Elephants migrating across the Serengeti."),
    (103, 5, 16, 23, "2023-03-10", "Amur Leopards spotted on the Galápagos Islands."),
    (104, 7, 17, 24, "2023-04-05", "Hawksbill Turtle nesting in the Arctic Tundra."),
    (105, 10, 19, 25, "2023-05-20", "Western Lowland Gorilla family observed in Madagascar."),
    (106, 2, 12, 26, "2023-06-18", "Giant Pandas feeding on bamboo in the Great Barrier Reef."),
    (107, 4, 14, 27, "2023-07-22", "Red-crowned Cranes flying over the Himalayan Mountains."),
    (108, 6, 15, 28, "2023-08-30", "Sumatran Orangutans playing in the Everglades."),
    (109, 8, 18, 29, "2023-09-14", "California Condors soaring over the Patagonian Desert."),
    (110, 9, 20, 30, "2023-10-05", "Snow Leopards resting in the Boreal Forest.")
    ]

