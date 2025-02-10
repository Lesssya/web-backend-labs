from flask import Blueprint, redirect, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    name = name if name else "Аноним"
    age = request.cookies.get ('age')
    age = age if age else "Неизвестно"
    name_color = request.cookies.get('name_color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    
    age = request.args.get ('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get ('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        drink = request.form.get('drink')
        price = 0

        # Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffe':
            price = 120
        elif drink == 'black-tea':
            price = 80
        else:
            price = 70

        # Добавка молока удорожает напиток на 30 рублей, а сахара на 10.
        if request.form.get('milk') == 'on':
            price += 30
        if request.form.get('sugar') == 'on':
            price += 10

        return redirect(f'/lab3/success?price={price}')

    return render_template('lab3/order.html')


@lab3.route('/lab3/pay', methods=['GET', 'POST'])
def pay():
    return render_template('lab3/pay.html')


@lab3.route('/lab3/success', methods=['GET'])
def success():
    price = request.args.get('price', type=int)
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    #Получение значения параметра X из query string
    color = request.args.get('color')
    background_color = request.args.get('background-color')
    font_size = request.args.get('font-size')
    if color:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color) #Установка cookie с именем и значением, полученным из query string.
        resp.set_cookie('background-color', background_color)
        resp.set_cookie('font-size', font_size)
        return resp
    
    #Получение значения cookie
    color = request.cookies.get('color') 
    background_color = request.cookies.get('background-color')
    font_size = request.cookies.get('font-size')
    resp = make_response(render_template('lab3/settings.html', color=color, background_color=background_color, font_size=font_size))
    return resp