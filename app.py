from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
    <!doctype html>
    <html>
        <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        </head>

        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>

            <h1>web-сервер на flask</h1>

            <nav>
                <ul>
                    <li><a href="/lab1">Первая лабораторная</a></li>
                </ul>
            </nav>

            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """

@app.route("/lab1")
def lab1():
    return """
    <!doctype html>
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>
            
            <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов-приложений, 
            сознательно предоставляющих лишь самые базовые возможности.
            </p>

            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """