from dataclasses import dataclass

import psycopg2

con = psycopg2.connect(
    host="localhost",
    port=5432,
    database="foziljon",
    user="foziljon",
    password="1"
)
cur = con.cursor()


@dataclass
class Users:
    user_id: int = None,
    is_bot: str = None,
    first_name: str = None,
    last_name: str = None,
    username: str = None,
    language_code: str = None

    query = """
        create table if not exists users(
            id serial primary key,
            user_id bigint,
            is_bot varchar(5),
            first_name varchar(30),
            last_name varchar(30),
            username varchar(30),
            language_code varchar(5),
            created_at date default current_timestamp
            
        )
    """

    def insert_into(self):
        query_insert = """
            insert into users(user_id,is_bot,first_name,last_name,username,language_code)
            values (%s,%s,%s,%s,%s,%s)
        """
        data = (self.user_id, self.is_bot, self.first_name, self.last_name, self.username, self.language_code)
        cur.execute(query_insert, data)
        con.commit()

    def see_users(self):
        query_see = """
            select first_name from users
        """
        cur.execute(query_see)
        return cur.fetchall()

    cur.execute(query)
    con.commit()
