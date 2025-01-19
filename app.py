from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.errorhandler(404)
def not_found(err):
    return 'нет такой страницы', 404


@app.route("/")
<<<<<<< HEAD
@app.route("/index")
def start():
=======
@app.route("/lab1/web") # Изменен роут /web на /lab1/web
def start():
    return """
    <!doctype html>
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>
            <a href="/lab1/author">author</a>  #изменен роут /author на /lab1/author
            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """, 200, {"X-Server": "sample",
             "Content-Type": "text/plain; charset=utf-8"
             }


@app.route("/lab1/author")  # Изменен роут /author на /lab1/author
def author():
    name = "Занозина Олеся Евгеньевна"
    group = "ФБИ-23"
    faculty = "ФБ"

>>>>>>> 60df162016aef4d6e01a92e65e199a451d45a4c1
    return """
<!doctype html>
<html>
    <body>
        <p>Студент: """ + name + """</p>
        <p>Группа: """ + group + """</p>
        <p>Факультет: """ + faculty + """</p>
        <a href="/lab1/web">web</a>   #изменен роут /web на /lab1/web
    </body>
</html>
"""


@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpeg")
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
       <link rel="stylesheet" href="{css_path}">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="{path}">
    </body>
</html>
'''


count = 0


@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return f'''
<!doctype html>
<html>
    <body>
        Сколько раз вы заходили: {count}
       <a href="{url_for('clear_counter')}">Очистить счётчик</a>
    </body>
</html>
'''

@app.route('/lab1/clear_counter')
def clear_counter():
    global count
    count = 0
    return redirect(url_for('counter'))

@app.route('/lab1/info') # Изменен роут /info на /lab1/info
def info():
    return redirect('/lab1/author') # Изменен роут /author на /lab1/author


@app.route('/lab1/created')
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201