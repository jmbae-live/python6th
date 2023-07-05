import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='password',
)

cur = conn.cursor()

# 테이블 생성 코드
# cur.execute('''
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# ''')
# conn.commit()

cur.close()
conn.close()