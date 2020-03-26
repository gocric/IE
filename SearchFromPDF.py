from Config import DB_NAME , TABLE_NAME
from Database import DBClass

def main():
    with DBClass(DB_NAME) as db:
        #data= db.select_all_data(TABLE_NAME)
        data = db.select_data(TABLE_NAME, " data like '%{0}%' ".format("solar"))

        import os
        if os.path.exists("output.txt"):
            os.remove("output.txt")

        with open("output.txt", "a") as f:
            for i in [i[0] for i in data]:
                f.write(i)
                f.write('\n')
        print("Total Files with text "+str(len(data)))
main()