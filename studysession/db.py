import sqlite3

class ChatGPTDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Creates a new table in the database with the given name and columns.
        The columns parameter should be a comma-separated string.
        """
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_record(self, table_name, columns, record):
        """
        Insert a record into a target table with values separated by commas.
        """
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({record})"
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def retrieve_records(self, table_name, conditions=None):
        """
        Retrieve records from a table based on optional conditions.
        """
        select_sql = f"SELECT * FROM {table_name}"
        if conditions:
            select_sql += f" WHERE {conditions}"
        self.cursor.execute(select_sql)
        return self.cursor.fetchall()
    
    def close(self):
        print('db closed')
        self.cursor.close()
        self.conn.close()