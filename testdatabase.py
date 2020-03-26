from Config import DB_NAME , TABLE_NAME, IMPORT_FOLDER
from Database import DBClass
import fnmatch
import os

def main():
    with DBClass(DB_NAME) as db:
        print(db.conn)
        res = db.select_all_data(TABLE_NAME)
        print("Total Files in  DB : " + str(len(res)))

    matches = []
    for root, dirnames, filenames in os.walk(IMPORT_FOLDER):
        for filename in fnmatch.filter(filenames, '*.pdf'):
            matches.append(os.path.join(root, filename))
    print("Total Files in  Folder : " + str(len(matches)))
main()