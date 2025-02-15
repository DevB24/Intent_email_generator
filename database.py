import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="intent_assignment",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()



def search_case_studies(intent: str, visited_urls: list):
    """Query the database for relevant case studies based on intent and visited URLs."""
    try:
        # Query for case studies matching intent or visited URLs
        query = """
        SELECT title, description, content FROM case_studies
        WHERE category ILIKE %s OR source_url = ANY(%s)
        """
        cursor.execute(query, (f"%{intent}%", visited_urls))
        case_studies = cursor.fetchall()

        # Format the results
        results = [{"title": cs[0], "description": cs[1], "content": cs[2]} for cs in case_studies]
        return results
    
    except Exception as e:
        return {"error": str(e)}
