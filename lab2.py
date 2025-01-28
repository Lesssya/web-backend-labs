from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/berries')
def berries():
    return render_template('berries.html')


@lab2.route('/lab2/example')
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
