class Query:
    #subquery
    
    query1="""
    SELECT 
    FROM 
    WHERE LOCATION='Asia' in
    (
        SELECT HabitatID
        FROM habitat
        WHERE LOCATION='Asia'
    )

    """