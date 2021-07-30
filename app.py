from flask import Flask, app, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.0.20'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'adminho'

mysql = MySQL(app)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['POST'])
def registro():

    tip_doc = request.form['tip_doc']
    num_doc = request.form['num_doc']
    nombre = request.form['nombres']
    apellidos = request.form['apellidos']
    celular = request.form['celular']
    correo = request.form['correo']
    num_doc = int(num_doc)
    celular = int(celular)
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO persona (tip_doc,num_doc,nombres,apellidos,celular,correo) VALUES(%s,%s,%s,%s,%s,%s)"
    datos = (tip_doc,num_doc,nombre,apellidos,correo,celular)
    cursor.execute(sql,datos)
    mysql.connection.commit()
    cursor.close()
    return "<h1>ok. información registrada</h1>"

@app.route('/Register')
def register():
    return render_template('Register.html')

if __name__ == "__app__":
    app.run(debbug=True)