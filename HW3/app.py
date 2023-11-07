from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
from create_db import create_table

app = Flask(__name__)
create_table()
valid_sort_criteria = ['uid', 'uname', 'contact']


@app.route("/")
@app.route("/index")
def index():
    sort_by = request.args.get('sort_by', 'uid')
    sort_dir = request.args.get('sort_dir', 'asc')

    if sort_by not in valid_sort_criteria:
        sort_by = 'uid'
    if sort_dir not in ['asc', 'desc']:
        sort_dir = 'asc'

    con = sql.connect("phones.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    sql_query = f"SELECT * FROM users ORDER BY {sort_by} {sort_dir}"
    cur.execute(sql_query)

    data = cur.fetchall()

    return render_template("index.html", datas=data, sort_by=sort_by, sort_dir=sort_dir)


@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        con = sql.connect("phones.db")
        cur = con.cursor()
        cur.execute("insert into users(UNAME,CONTACT) values (?,?)", (uname, contact))
        con.commit()
        flash('User Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        con = sql.connect("phones.db")
        cur = con.cursor()
        cur.execute("update users set UNAME=?,CONTACT=? where UID=?", (uname, contact, uid))
        con.commit()
        flash('User Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("phones.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas=data)


@app.route("/delete_user/<string:uid>", methods=['GET'])
def delete_user(uid):
    con = sql.connect("phones.db")
    cur = con.cursor()
    cur.execute("delete from users where UID=?", (uid,))
    con.commit()
    flash('User Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
