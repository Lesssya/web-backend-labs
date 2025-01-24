from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

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

    
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="'''+url_for('static', filename='oak.jpeg')+'''">
    </body>
</html>
'''

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
        <head>
        <title>Занозина Олеся Евгеньевна, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>

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

            <nav>
                <ul>
                    <li><a href="/menu">Меню</a></li>
                </ul>
            </nav>

            <h2>Реализованные роуты</h2>
            <nav>
                <ul>
                    <li><a href="/lab1/oak">Дуб</a></li>
                    <li><a href="/lab1/student">Студент</a></li>
                    <li><a href="/lab1/python">Python</a></li>
                    <li><a href="/lab1/WEB">Веб-программирование</a></li>
                </ul>
            </nav>

            <footer>
                &copy; Занозина Олеся, ФБИ-23, 2024
            </footer>
        </body>
    </html>
    """
@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Занозина Олеся Евгеньевна</h1>
        <img src="'''+url_for('static', filename='NETI.jpg')+'''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Преимущества: чем хорош Python</h1>
        <img src="'''+url_for('static', filename='python.jpeg')+'''">
        <p>
        Специалисты выделяют массу преимуществ Python — остановимся на ключевых из них.
        <b>Простота синтаксиса, а значит — низкий порог вхождения.</b> 
        Код языка чистый и понятный, без лишних символов и выражений.<br>
        <b>Расширяемость и гибкость.</b> Не зря один из слоганов языка — это «Just Import!» 
        Python можно легко расширить для взаимодействия с другими программными 
        системами или встроить в программы в качестве компонента. Он очень и очень гибкий. 
        Это даёт больше возможностей для использования языка в разных сферах.<br>
        <b>Интерпретируемость и кроссплатформенность.</b> Интерпретатор Python есть для всех 
        популярных платформ и по умолчанию входит в большинство дистрибутивов Linux.<br>
        <b>Стандартизированность.</b> У Python есть единый стандарт для написания кода — Python
        Enhancement Proposal или PEP, благодаря чему язык остаётся читабельным даже при 
        переходе от одного программиста к другому.<br>
        <b>Open Source.</b> У интерпретатора Python открытый код, то есть любой, 
        кто заинтересован в развитии языка, может поучаствовать в его разработке и улучшении.<br>
        <b>Сильное комьюнити и конференции.</b> Вокруг Python образовалось дружественное 
        комьюнити, которое готово прийти на помощь новичку или уже опытному разработчику 
        и разобраться в его проблеме. Во всём мире проходит много мероприятий, где можно 
        познакомиться с коллегами и узнать много нового о применении Пайтона.<br>
        <b>Широта применения.</b> Наиболее широко Python используется в web-разработке, 
        работе с данными, автоматизации бизнес-процессов и геймдеве.<br>
        <b>Востребованность на рынке труда и поддержка гигантами IT-сферы.</b> Python-разработчики востребованы 
        во многих проектах и им несложно найти работу. Разработку на Python ведут в Google, 
        Facebook, Dropbox, Spotify, Quora, Netflix, Microsoft Intel, а в России — «Яндекс», 
        «ВКонтакте» и «Сбербанк». Это серьёзно влияет на статус языка.<br>
        </p>
    </body>
</html>
'''

@app.route("/lab1/WEB")
def SQL():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Для чего нужно веб-программирование</h1>
        <img src="'''+url_for('static', filename='WEB.png')+'''">
        <p>
            <b>Веб-программирование</b> — это процесс создания веб-сайтов и веб-приложений, которые работают в интернете. 
            Оно позволяет разработчикам создавать интерактивные, динамичные и функциональные платформы, которые 
            могут использоваться для различных целей: от простых блогов до сложных интернет-магазинов и корпоративных 
            систем. Главная задача веб-программирования — обеспечить пользователям удобный доступ к информации и 
            сервисам через браузер, а также сделать взаимодействие с сайтом максимально комфортным и эффективным.
            Чтобы понять, зачем нужно веб-программирование, представьте, что вы хотите открыть интернет-магазин. 
        </p>
        <p>
            Вам нужно, чтобы пользователи могли просматривать товары, добавлять их в корзину, оформлять заказы 
            и отслеживать доставку. Веб-программирование позволяет реализовать все эти функции, создавая 
            интуитивно понятный интерфейс и обеспечивая быструю работу сайта. <i>Например, с помощью таких технологий, 
            как HTML, CSS и JavaScript, можно создать красивый и удобный интерфейс, а с помощью серверных языков, 
            таких как Python, PHP или Node.js, — обрабатывать данные, управлять заказами и взаимодействовать с базой данных.</i>
        </p>
    </body>
</html>
'''