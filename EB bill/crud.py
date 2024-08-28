from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            units = request.form["units"]
            amount = request.form["amount"]
            with sqlite3.connect("EB_Bill") as con:
                cur = con.cursor()   
                cur.execute("INSERT into EB_Bill (units, amount) values (?,?)",(units,amount))
                con.commit()
                msg = "Electricity successfully Added"   
        except:
            con.rollback()
            msg = "We can not add Contact to the list"
        finally:
            return render_template("success.html",msg = msg)
            con.close()

@app.route("/view")
def view():
    con = sqlite3.connect("EB_Bill")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from EB_Bill")   
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("EB_Bill") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from EB_Bill where id = ?",id)
            msg = "Contact successfully deleted"   
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)  
