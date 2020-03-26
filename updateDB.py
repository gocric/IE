from Config import DB_NAME , TABLE_NAME, IMPORT_FOLDER
from Database import DBClass

with DBClass(DB_NAME) as db:

    #sql = 'UPDATE ' + TABLE_NAME + " SET file=replace(file,'C:\\IE\\\\PDF_FILES','E:\\Issues All') "
    sql = 'DELETE FROM  ' + TABLE_NAME + " where  file like '%gokvijay%'"
    cur = db.conn.cursor()
    cur.execute(sql)
    db.conn.commit()

    cur = db.conn.cursor()
    cur.execute("SELECT distinct file FROM " + TABLE_NAME)

    rows = cur.fetchall()

    output = []
    for row in rows:
        output.append(row)

    print(output[:10])
