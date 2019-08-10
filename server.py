import pyodbc
from flask import Flask, jsonify, request
app = Flask(__name__)


#con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
#conn = pyodbc.connect("DRIVER={{SQL Server}};SERVER=GRAHAMP\SQLEXPRESS; database=TestDB; \
#       trusted_connection=yes;UID=testusername;PWD=passwordtest".format(ServerName,MSQLDatabase,username,password))
#cursor = con.cursor()

# rest api to get all users
@app.route('/api/user')
def get():
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
    cur=con.cursor()
    cur.execute('''select * from users''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)

 # rest api to get a single user
@app.route("/api/user/<id>", methods=["GET"])
def user_detail(id):
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
    cur=con.cursor()
    cur.execute('''select * from users where id='''+id)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)

#rest api to create a new user in mysql database
@app.route("/api/user", methods=["POST"])
def user_add():
    print("/api/user POST")
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
    cur=con.cursor()
    username=request.json['username']
    password=request.json['password']
    sql = "INSERT INTO users (username, password) VALUES (?, ?)"
    val = (username, password)
    cur.execute(sql, val)
    con.commit()
    return jsonify(cur.rowcount.__str__() + " records added ")

#rest api to update a user in mysql database
@app.route("/api/user/<id>", methods=["PUT"])
def user_update(id):
    print("/api/user PUT")
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
    cur=con.cursor()
    username=request.json['username']
    password=request.json['password']
    print(username,password)
    sql = "Update users SET username=?, password=? WHERE id=?"
    val = (username, password, id)
    cur.execute(sql, val)
    con.commit()
    return jsonify(cur.rowcount.__str__() + " records updated ")

#rest api to delete a user in mysql database
@app.route("/api/user/<id>", methods=["DELETE"])
def user_delete(id):
    print("/api/user PUT")
    con = pyodbc.connect('DRIVER={SQL Server};SERVER=GRAHAMP\SQLEXPRESS;DATABASE=TestDB;UID=testusername;PWD=passwordtest')
    cur=con.cursor()
    sql = "Delete from users WHERE id=?"
    val = (id)
    cur.execute(sql, val)
    con.commit()
    return jsonify(cur.rowcount.__str__() + " records deleted ")

    
if __name__ == '__main__':
    app.run()
