import threading
#import time
from DBConnect import  DBConnect
from decimal import Decimal


class InsertPerformanceInfo(threading.Thread):

    def __init__(self,tflag,count):
            threading.Thread.__init__(self)
            self.tflag = tflag
            self.count = count


    def run(self):
            dbconnection = DBConnect()
            con = dbconnection.pgconn(dbname='Test', user='test', host='127.0.0.1', port=1030)
            queries=["insert into  public.tb_performance_info values('SN0101',1,%d,0,0);" %(a) for a in self.tflag[:self.count]]
            for query in queries:
                    #time.sleep(1)
               #print(query)
               dbconnection.executeOtherQuery(con,query)


class DeletePerformanceInfo(threading.Thread):

    def __init__(self,tflag,count):
            threading.Thread.__init__(self)
            self.tflag = tflag
            self.count = count

    def run(self):
            dbconnection = DBConnect()
            con = dbconnection.pgconn(dbname='Test', user='test', host='127.0.0.1', port=1030)
            queries=["delete from  public.tb_performance_info  where timeflag::integer=%d;" %(Decimal(a)) for a in self.tflag[:self.count]]
            for query in queries:
                #time.sleep(1)
               print(query)
               dbconnection.executeOtherQuery(con,query)


class ReindexPerformanceInfo(threading.Thread):

    def __init__(self,count):
            threading.Thread.__init__(self)
            self.count = count

    def run(self):
             dbconnection = DBConnect()
             con = dbconnection.pgconn(dbname='Test', user='test', host='127.0.0.1', port=1030)
             while self.count>0:
                query="REINDEX TABLE public.tb_performance_info ;"
                #time.sleep(1)
                print(query)
                dbconnection.executeOtherQuery(con,query)
                self.count=self.count-1

class VaccumPerformanceInfo(threading.Thread):

    def __init__(self,count):
            threading.Thread.__init__(self)
            self.count = count

    def run(self):
             dbconnection = DBConnect()
             con = dbconnection.pgconn(dbname='Test', user='test', host='127.0.0.1', port=1030)
             while self.count>0:
                query="VACUUM public.tb_performance_info ;"
                #time.sleep(1)
                print(query)
                dbconnection.executeOtherQuery(con,query)
                self.count=self.count-1