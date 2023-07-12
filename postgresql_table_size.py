import psycopg2


if __name__ == "__main__":
    try:
        url = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format('localhost', 'postgres', 'postgres', '12345')


        conn = psycopg2.connect(url)


        cursor = conn.cursor()

        sql = """SELECT datname AS "Nombre de la base de datos", 
  pg_roles.rolname AS "Propietario de la base de datos",
  relname AS "Nombre de las tablas"
FROM pg_database
JOIN pg_roles ON pg_database.datdba = pg_roles.oid
JOIN pg_class ON pg_database.oid = pg_class.relnamespace
WHERE relkind = 'r'
ORDER BY relname"""

        cursor.execute(sql)

        for row in cursor:
            print("\t",row[0],"\t",row[1],"\t",row[2])


        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
