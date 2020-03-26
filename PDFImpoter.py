import fnmatch
import os
import shutil
from Database import DBClass
from PDFHandler import PDFFile
from Config import DB_NAME ,NEW_FOLDER ,IMPORT_FOLDER ,TABLE_NAME

def main():
        matches = []
        for root, dirnames, filenames in os.walk(IMPORT_FOLDER):
            for filename in fnmatch.filter(filenames, '*.pdf'):
                matches.append(os.path.join(root, filename))

        with DBClass(DB_NAME) as db:

            db.create_table(TABLE_NAME, {'file': 'TEXT', 'data': 'TEXT'})

            all_data = db.select_all_data(TABLE_NAME)
            all_data = [i[0] for i in all_data]
            matches = [i for i in matches if i not in all_data]
            for pdf_file in matches:
                try:
                    print("Working on file : {0}".format(pdf_file))
                    pdf_data = PDFFile(pdf_file).load_text_From_pdf()
                    new_pdf_file = pdf_file.replace(IMPORT_FOLDER, NEW_FOLDER)

                    data = (pdf_file, pdf_data)

                    project_id = db.insert_data(TABLE_NAME, data)
                    print("Completed file : {0}".format(pdf_file))
                    '''
                    if not os.path.exists(os.path.dirname(new_pdf_file)):
                        os.mkdir(os.path.dirname(new_pdf_file))
                    shutil.move(pdf_file, new_pdf_file)
                    '''
                except:
                    pass
            #data = db.select_all_data(TABLE_NAME)
            print('Total files completed : {0}'.format(len(data)))

main()