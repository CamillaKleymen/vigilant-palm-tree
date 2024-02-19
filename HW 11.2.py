import sqlite3

connection = sqlite3.connect('mydatabase.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, username TEXT, age INTEGER, grade TEXT);')

sql.execute('INSERT INTO students VALUES(17062003, "Camilla", 20, "C");')
sql.execute('INSERT INTO students VALUES(17061998, "Andrew", 25, "C");')
sql.execute('INSERT INTO students VALUES(12011976, "Helen", 21, "B");')
sql.execute('INSERT INTO students VALUES(15031996, "Frank", 23, "A");')
sql.execute('INSERT INTO students VALUES(17062005, "Margo", 26, "B");')

def get_student_by_name(username):
    username=sql.execute('SELECT username, age, grade FROM students;')
    return username.fetchall()
    # username1 = sql.execute('SELECT username, age, grade FROM students WHERE username = "Camilla";')
    # return username1.fetchone()

print(get_student_by_name('username'))

def update_student_grade(username):
    username = sql.execute('UPDATE students SET grade = "A" WHERE username = "Camilla";')
    return username.fetchone()

print(update_student_grade('username'))

def delete_student(username):
    username = sql.execute('DELETE FROM students WHERE username = "Camilla";')
    return username.fetchone()

print(delete_student('username'))




