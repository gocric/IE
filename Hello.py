from flask import Flask, render_template,send_file
from Config import DB_NAME , TABLE_NAME
from Database import DBClass
import os

app = Flask(__name__)


@app.route('/index/', methods = ['OPTIONS', 'GET', 'POST'])
def Index():
   return render_template('index.html' )

@app.route('/search/<name>', methods = ['OPTIONS', 'GET', 'POST'])
def Search(name):
   name = name.replace("'","''")
   with DBClass(DB_NAME) as db:
      # data= db.select_all_data(TABLE_NAME)
      data = db.select_data(TABLE_NAME, " data like '%{0}%' ".format(name))

      data = [('/downloadFile/'+i[0],os.path.split(i[0])[1]) for i in data]
      print("Total Files with text " + str(len(data)))
   return render_template('search.html', name = name, data = data )

@app.route('/downloadFile/<path:file>')
def download_file(file):
   b=None
   static_file =  open(file, 'rb')
   return send_file(static_file, attachment_filename='file.pdf')


if __name__ == '__main__':
   app.run()