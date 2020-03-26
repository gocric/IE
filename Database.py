import sqlite3

class DBClass(object):

    def __init__(self, connName):
        self.conn = self.create_connection(connName)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.conn.close()

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception  as e:
            print(e)

        return None

    def insert_data(self, tableName, tableData):

        print(tableData)
        sql = 'INSERT INTO ' + tableName + '(file, data) VALUES(?,?)'
        cur = self.conn.cursor()
        cur.execute(sql, tableData)
        self.conn.commit()

        return cur.lastrowid



    def select_all_data(self, tableName):
        cur = self.conn.cursor()
        cur.execute("SELECT distinct(file) FROM " + tableName)

        rows = cur.fetchall()

        output = []
        for row in rows:
            output.append(row)

        return output

    def select_data(self, tableName, sqltext):
        cur = self.conn.cursor()
        cur.execute("SELECT distinct file, data FROM " + tableName + " where " + sqltext)


        rows = cur.fetchall()

        output = []
        for row in rows:
            output.append(row)

        return output

    def drop_table(self, tableName):
        try:
            cur = self.conn.cursor()
            cur.execute("drop table {0}".format(tableName))
            self.conn.commit()
        except:
            pass

    def create_table(self, tableName, columns):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE ''' + tableName + ''' ( {0} )
            '''.format(','.join([key + ' ' + value for key, value in columns.items()])))
            self.conn.commit()
        except:
            print("Gokul")