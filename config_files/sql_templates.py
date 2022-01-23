sql_templates = {
    #TODO: How to parameterize columns here?
    "create_table_books":
        """
    CREATE TABLE IF NOT EXISTS books (
        id integer PRIMARY KEY,
        genre text NOT NULL,
        title text,
        release_date text,
        to_read integer,
        rating integer,
        date_complete text,
        tags text
        """,
    "create_table_movies":
    """
    CREATE TABLE IF NOT EXISTS {screen} (
        id integer PRIMARY KEY,
        genre text NOT NULL,
        title text,
        release_date text,
        to_watch integer,
        my_rating integer,
        rt_critics integer,
        rt_audience integer,
        date_complete text,
        tags text
        """,
    "insert_record":
    """INSERT INTO ({columns})
        VALUES ({values})"""
}