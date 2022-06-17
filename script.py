import sqlite3
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""
cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'Charlie','Rakshith shetty',2022,'Kiran raj')")
cursor.execute("INSERT INTO movies VALUES(2,'RRR','Ram charan',2022,'Raj mouli')")
cursor.execute("INSERT INTO movies VALUES(3,'Bahubali-2','Prabhas',2020,'Raj mouli')")
cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
print(results)
print('Details of the movie in which Ram charan was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Ram charan'")
res = cursor.fetchall()
print(res)