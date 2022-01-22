sql_templates = {
    #TODO: How to parameterize columns here?
    "create_table":
        """
    CREATE TABLE IF NOT EXISTS {table_name} (
        id integer PRIMARY KEY,
        format text NOT NULL,
        title text,
        release_date text,
        to_do integer,
        rating integer,
        date_done text
        """
}