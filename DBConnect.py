import psycopg2
from psycopg2 import DatabaseError
from psycopg2 import OperationalError

class DBConnect:
    def pgconn(self,*args,**kwords):
        ret=None
        try:
            print("Trying to connect...")
            pgcon=psycopg2.connect("dbname = %s user=%s  host =%s port=%s"%                \
                               (kwords['dbname'],kwords['user'],kwords['host'],kwords['port']))
            print("Connection to postgres server successful")
            ret=pgcon
        except OperationalError as e:
            print (e)
        except Exception as e:
            print (e)
        finally:
            return ret

    def executeSelectQuery(self,pgconn,query):
        try:
            cur = pgconn.cursor()
            cur.execute(query)
            rows=cur.fetchall()

        except DatabaseError as dberror:
            pgconn.rollback()
            print ('Database Error :- %s'%(dberror))
            rows = None
        finally:
            return rows

    def executeOtherQuery(self,pgconn,query):
        try:
            cur = pgconn.cursor()
            cur.execute(query)
            pgconn.commit()
        except DatabaseError as dberror:
            pgconn.rollback()
            print ('Database Error :- %s'%(dberror))