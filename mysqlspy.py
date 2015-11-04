import MySQLdb,time,argparse

class MysqlSpy(object):

    def __init__(self,host,uesr,passwd,port=3306):

        self.host = host
        self.user = uesr
        self.passwd = passwd
        self.port = port

    def connect(self,sec=60):
        try:
            conn = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = 'mysql', port = self.port)
            cu = conn.cursor()
            sql = 'select event_time, argument from general_log where event_time > "{time}";'.format(time = self.getTime(sec))
            cu.execute(sql)
            results = cu.fetchall()
            for date,sql in results:
                print date.strftime("%Y-%m-%d %X")+"=>"+sql

        except MySQLdb.Error,e:
            print "error id:{id},erro:{error}".format(id=e.args[0], error=e.args[1])


    def getTime(self,second):
        """return system time before second time"""

        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-second))



    def help(self):
        print"Tool for catch sql\rInpurt s get the sql in a minute\r"
        pass


    def main(self):
        print "Fuck sql,input s for sql~~~"
        while 1:
            userKey = raw_input()
            result = {
                's':self.connect,
                'h':self.help
            }[userKey]()

def parse():

    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--host", default="127.0.0.1", help="Mysql host")
    parser.add_argument("-p","--port", default=3306, type=int, help="Mysql port")
    parser.add_argument("-u","--user", required=True, help="mysql user")
    parser.add_argument("-P","--passwd", help="Mysql connection password")
    args = parser.parse_args()

    spy = MysqlSpy(args.host,args.user,args.passwd,args.port)
    spy.main()

if __name__=="__main__":
    parse()