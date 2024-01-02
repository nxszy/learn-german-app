import psycopg2

with open('verbs.txt', 'r', encoding='utf-8') as file:
    verbs = [row.strip('\n').split(',') for row in file]
    print(verbs)



'''
con = psycopg2.connect(
    database='german_app_DB',
    user='postgres',
    password='baza123',
    host='localhost',
    port='4444'
)

cursor = con.cursor()
'''


