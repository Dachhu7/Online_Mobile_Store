from flask import *
import mysql.connector as mysql

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/homepage')
def homepage1():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/check_login')
def check_login():
    username = request.args.get('username')
    pswd = request.args.get('pswd')
    
    try:
        con = mysql.connect(host='localhost', user='root', password='Dachhu@0007', database='Sample1')
        cur = con.cursor()
        cur.execute("SELECT * FROM check_register WHERE username = %s AND pswd = %s", (username, pswd))
        result = cur.fetchall()
        con.close()
        
        if len(result) == 0:
            msg = "Invalid Username or Password"
            return render_template("login.html", msg=msg)
        else:
            return render_template('home.html')
    except Exception as e:
        return render_template("login.html", msg=f"An error occurred: {e}")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/check_register')
def check_register():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    username = request.args.get('username')
    pswd = request.args.get('pswd')
    
    try:
        con = mysql.connect(host='localhost', user='root', password='Dachhu@0007', database='Sample1')
        cur = con.cursor()
        cur.execute("INSERT INTO check_register (firstname, lastname, username, pswd) VALUES (%s, %s, %s, %s)",
                    (firstname, lastname, username, pswd))
        con.commit()
        con.close()
        msg = "Your data has been saved successfully"
        return render_template("login.html", msg=msg)
    except Exception as e:
        return render_template("login.html", msg=f"An error occurred: {e}")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/workers')
def workers():
    return render_template("workers.html")

@app.route('/done')
def done():
    return render_template("home.html")

@app.route('/accessories')
def accessories():
    return render_template("accessories.html")

@app.route('/users')
def users():
    con = mysql.connect(host='localhost', user='root', password='Dachhu@0007', database='deatils')
    cur = con.cursor()
    cur.execute("SELECT username FROM users")
    results = cur.fetchall()
    con.close()
    usernames = [row[0] for row in results]
    return render_template('users.html', usernames=usernames)

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")  

@app.route('/buy')
def buy():
    return render_template("buy.html")

@app.route('/buy_product')
def buy_product():
    mname = request.args.get('name')
    mbrand = request.args.get('imeinumber')
    mamount = request.args.get('amount')
    tamount = request.args.get('total')
    
    try:
        con = mysql.connect(host='localhost', user='root', password='Dachhu@0007', database='deatils')
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (mname, mbrand, mamount, tamount))
        con.commit()
        con.close()
        msg = "Your data has been saved successfully"
        return render_template("thankyou.html", msg=msg)
    except Exception as e:
        return render_template("thankyou.html", msg=f"An error occurred: {e}")
