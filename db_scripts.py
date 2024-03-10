import psycopg2

con = psycopg2.connect(
    database='german_app_DB',
    user='postgres',
    password='baza123',
    host='localhost',
    port='4444'
)


with open('conjugation_verbs/verbs_final.csv', 'r', encoding='utf-8') as file:
    verbs = [row.strip('\n').split(',') for row in file]
    
    with con.cursor() as cursor:
        
        for verb in verbs[1:]:
            print(verb)
            cursor.execute('''INSERT INTO conjugation_conjverb("translation", "infinitive", "sg_Ip_form", "sg_IIp_form", "sg_IIIp_form", "pl_Ip_form", "pl_IIp_form", "pl_IIIp_form")
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', [form for form in verb])
        
con.commit()



