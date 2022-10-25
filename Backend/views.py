from unicodedata import category
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import yaml, json, string, hashlib, secrets


def init(app, mysql):
        
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

    @app.route('/users',methods=['GET','POST'])
    def users():
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users")
        if result > 0:
            user_details = cur.fetchall();
            print('AAAAAAAAAAAAAAAAA',user_details)
            return render_template('users.html', user_details=user_details)

    # Get all categories
    @app.route('/categories', methods=['GET'])
    def getAllCategories():
        cur = mysql.connection.cursor()
        querry = "SELECT * FROM Categories"
        cur.execute(querry)
        result = cur.fetchall()
        json_data = []
        for _,categories_name in result:
            json_data.append(categories_name)
        return json.dumps(json_data)
    
    # Get all tables, isOccupied = 1 means True, isOccupied = 0 means False
    @app.route('/tables/', defaults={'isOccupied': 2}, methods=['GET'])
    @app.route('/tables/<isOccupied>', methods=['GET'])
    def getAllTables(isOccupied):
        cur = mysql.connection.cursor()
        querry = """
            SELECT * 
            FROM Restaurant_Table 
            """
        print('AAAAAAAAAAAAAAAAA', isOccupied)
        if isOccupied == "1":
            querry += "WHERE status = 1;"
        elif isOccupied == "0":
            querry += "WHERE status = 0;"
        else:
            querry += ";"
            
        print("QUERRY: ", querry)

        cur.execute(querry)
        result = cur.fetchall()
        json_data = []
        for _,table_number,status in result:
            json_data.append({
                'table_number': table_number,
                'status': status 
            })
        return json.dumps(json_data)

    # Get all items from Items table
    @app.route('/menu', methods=['GET'])
    def getAllItems():
        cur = mysql.connection.cursor()
        querry = """
            SELECT I.*, P.photo
            FROM Items I
            JOIN Photos P
            ON I.photoID=P.ID
            ;
        """
        print(querry)
        cur.execute(querry)
        result = cur.fetchall()
        json_data = []
        for i in result:
            json_data.append(i[1])
        return json.dumps(json_data)
    
    #Create an order
    

