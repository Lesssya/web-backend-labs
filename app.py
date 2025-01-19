from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """
    <!doctype html>
    <html>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>web-сервер на flask</h1>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """

