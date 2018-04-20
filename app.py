import os
import sys
from flask import Flask, render_template, request
from pymongo import MongoClient
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '.\images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)



def dbconnect():

    if(("DB_USER" not in os.environ) and ("DB_PASS" not in os.environ) ):
        mongo_username = "muser"
        mongo_password = "mpass"
    else:
        mongo_username = os.environ['DB_USER']
        mongo_password = os.environ['DB_PASS']
    
    
    uri = "mongodb://"+ mongo_username +":"+mongo_password+"@ds147459.mlab.com:47459/sampledb"
    #uri = "mongodb://localhost:27017/testdb"
    client = MongoClient(uri)
    db = client.get_default_database()
    print (db.collection_names())
    #print(client.server_info())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/newrecipe',methods=['POST'])
def newrecipe():
    # check if the post request has the file part
    print(request.files)
    if 'imgImp0Name' not in request.files:
        print('No file part')
        return "<h1>Error no file part</h1>"
    file = request.files['imgImp0Name']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        print('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "<h1>uploaded image ok</h1>"
    
    

    print ("TEST 5")
    dict = request.form
    
    for key in dict:
        print ('key=' + key + ' value='+dict[key])
    return "<h1>OK6</h1>"
     

@app.route('/')
def homepage():
    return"<H1>Hello World hr</H1>"

    
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
    

