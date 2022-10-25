from flask_mysqldb import MySQL
import yaml

def init(app):
    print("Connecting to mySQL")
    with open('db.yaml', 'r') as file:
        db = yaml.safe_load(file)
    # db = yaml.load(open('db.yaml'))
    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']

    mysql = MySQL(app)
    print("MySQL", mysql)
    return mysql