from flask import Flask, url_for
app = Flask (__name__)

@app.route("/")
@app.route("/web")
def start():
    return """
    <!doctype html>
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>
            <a href="/author">author</a>
            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """

@app.route("/author")
def author():
    name = "Занозина Олеся Евгеньевна"
    group = "ФБИ-23"
    faculty = "ФБ"

    return """
<!doctype html>
<html>
    <body>
        <p>Студент: """ + name + """</p>
        <p>Группа: """ + group + """</p>
        <p>Факультет: """ + faculty + """</p>
        <a href="/web">web</a>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpeg")
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''    
count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы заходили: ''' + str(count) + '''
    </body>
</html>
''' 

