import sqlite3

connection = sqlite3.connect('bank.database.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS bankusers (user_id INTEGER, username TEXT, usernum TEXT, balance INTEGER);')

sql.execute('INSERT INTO bankusers VALUES(17062003, "Camilla", +998903508466, 17000000);')
sql.execute('INSERT INTO bankusers VALUES(17061998, "Andrew", +998915603698, 154000);')
sql.execute('INSERT INTO bankusers VALUES(12011976, "Helen", +998339051094, 18400000);')
sql.execute('INSERT INTO bankusers VALUES(15031996, "Frank", +998945407698, 4560000);')
sql.execute('INSERT INTO bankusers VALUES(17062005, "Margo", +998971594873, 20000);')

print(sql.execute('SELECT username, usernum FROM bankusers;').fetchall())

sql.execute('UPDATE bankusers SET balance = 25000000 WHERE username = "Camilla";')
print(sql.execute('SELECT * FROM bankusers;').fetchone())

sql.execute('DELETE FROM bankusers WHERE balance = 154000')
print(sql.execute('SELECT * FROM bankusers;').fetchall())

print(sql.execute('SELECT balance, username FROM bankusers;').fetchall())

# def calculate_interest(balance, months):
#     interest_rate = 1,0
#     total_balance = balance * ((1 + interest_rate) ** (months / 12))
#     return total_balance

print(sql.execute('SELECT user_id, username, usernum, balance FROM bankusers;').fetchall())

connection.commit()

