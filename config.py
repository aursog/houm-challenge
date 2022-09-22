mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': 'test',
         'port': '3306',
         'db': 'houm'}

mysqlConfig = "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql['user'], mysql['passwd'], mysql['host'], mysql['port'], mysql['db'])
