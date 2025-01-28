from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/berries')
def berries():
    return render_template('berries.html')


@app.route('/lab2/example')
def example():
    name, num_lab, group, course = 'Олеся Занозина', 2, 'ФБИ-23', 3
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321},
    ]
    book = [
        {'author': 'Габриэль Гарсиа Маркес', 'name_book': 'Сто лет одиночества', 'style': 'Роман', 'num_page': '480'},
        {'author': 'Рэй Брэдбери', 'name_book': '451 градус по Фаренгейту', 'style': 'Антиутопия', 'num_page': '200'},
        {'author': 'Михаил Булгаков', 'name_book': 'Мастер и Маргарита', 'style': 'Роман', 'num_page': '470'},
        {'author': 'Джон Эрнст Стейнбек', 'name_book': 'Гроздья гнева', 'style': 'Реалистический роман', 'num_page': '590'},
        {'author': 'Эрих Мария Ремарк', 'name_book': 'На западном фронте без перемен', 'style': 'Антивоенный роман', 'num_page': '200'},
        {'author': 'Колин Маккалоу', 'name_book': 'Поющие в терновнике', 'style': 'Семейная сага', 'num_page': '820'},
        {'author': 'Михаил Шолохов', 'name_book': 'Тихий дон', 'style': 'Роман-эпопея', 'num_page': '1810'},
        {'author': 'Лев Толстой', 'name_book': 'Война и Мир', 'style': 'Роман-эпопея', 'num_page': '1979'},
        {'author': 'Виктор Мари Гюго', 'name_book': 'Отверженные', 'style': 'Трагедия', 'num_page': '1871'},
        {'author': 'Антуан де Сент-Экзюпери', 'name_book': 'Маленький принц', 'style': 'Философская сказка', 'num_page': '78'},
    ]
    return render_template ('example.html', num_lab=num_lab, 
                            name=name, group=group, course=course,
                            fruits=fruits, book=book)


@app.route("/menu")
def menu():
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
                    <li><a href="/lab2">Вторая лабораторная</a></li>
                </ul>
            </nav>

            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """