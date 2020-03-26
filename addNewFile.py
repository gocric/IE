import fnmatch
import os
import shutil
from Database import DBClass
from PDFHandler import PDFFile
from Config import DB_NAME ,NEW_FOLDER ,IMPORT_FOLDER ,TABLE_NAME

def main():
    pdf_file = input("Enter the file to upload : ")  # Python 3
    pdf_file = pdf_file.strip()

    with DBClass(DB_NAME) as db:
        try:
            db.create_table(TABLE_NAME, {'file': 'TEXT', 'data': 'TEXT'})

            print("Working on file : {0}".format(pdf_file))
            pdf_data = PDFFile(pdf_file).load_text_From_pdf()
            data = (pdf_file, pdf_data)

            project_id = db.insert_data(TABLE_NAME, data)
            print("Completed file : {0}".format(pdf_file))
            input("File successfully processed")
        except Exception as e:
            input("Error processing file :"+str(e))

main()