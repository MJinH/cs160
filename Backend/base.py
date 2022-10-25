from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import yaml, json, string, hashlib, secrets

app = Flask(__name__)
CORS(app, support_credentials=True)

with open('db.yaml', 'r') as file:
    db = yaml.safe_load(file)
# db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


@app.route("/auth", methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def authentication():

    if request.method == 'POST':
        data = json.loads(request.data)

        employeeID = data.get('employeeID') # Extract employeeID
        print(employeeID)
        password = data.get('password') # Extract password
        print(password)

        encrypted = hashlib.sha1(password.encode('utf-8')).hexdigest()

        cur = mysql.connection.cursor()
        query = f'SELECT * FROM users WHERE employeeID = {employeeID} AND ' \
                f'password = "{encrypted}";'

        result = cur.execute(query)

        cur.close()

        if result > 0:
            return json.dumps({"employeeID": employeeID})

        return json.dumps({"response": False})


@app.route("/registration", methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def registration():

    if request.method == 'POST':

        data = json.loads(request.data)

        employeeID = data.get('employeeID')
        password = data.get('password')
        encrypted = hashlib.sha1(password.encode('utf-8')).hexdigest()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(employeeID, password) VALUES(%s,%s)",
                    (employeeID, encrypted))

        mysql.connection.commit()
        cur.close()

    return {"response": "success"}


@app.route('/', methods=['GET', 'POST'])
def index():
    response_body = {
        "name": "Nagato",
        "about": "Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch Form Data
        user_details = request.form
        employee_id = user_details['Employee ID Number']
        password = user_details['Password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(employeeID, password) VALUES(%s,%s)",
                    (employee_id, password))

        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
"""

@app.route('/users', methods = ['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    # db = cur.cursor(dictionary=True)
    result = cur.execute("SELECT * FROM users")
    if result > 0:
        row_headers = [x[0] for x in cur.description]  # this will extract
        # row headers
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)

if __name__ == '__main__':
    app.run(debug=True)
