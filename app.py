from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

# Список пользователей:
users = [
    {'username': 'Adam', 'age': 20, 'eye_color': "blue", 'email': 'adam@gmail.com'},
    {'username': 'Rayan', 'age': 19, 'eye_color': "brown", 'email': 'rayan@gmail.com'},
    {'username': 'Islam', 'age': 22, 'eye_color': "black", 'email': 'islam@gmail.com'}
]


@app.route('/')
def index():
    return render_template('home.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html', users=users)


@app.route('/contact')
def contact():
    return render_template('contact.html', users=users)


# Реализуйте перенаправление с одной страницы на другую при помощи Flask.
# Создайте страницу /redirect_example, на которой будет кнопка,
# при нажатии на которую происходит перенаправление на другую страницу вашего приложения.
@app.route('/redirect_example')
def redirect_1():
    return render_template('redirect_example.html')

# Когда вы перейдете на /redirect_example, вы увидите кнопку "Redirect to About Page".
# При ее нажатии вы будете перенаправлены на страницу /about.
@app.route('/redirect', methods=["POST"])
def redirect_action():
    return redirect(url_for('about'))


# Доработайте обработку ошибок в вашем приложении,
# добавив обработку ошибки 500 (Internal Server Error)
# и отображение пользователю информации об этой ошибке.
# Обработка ошибки 500
@app.route('/error_500')
def error_500():
    return render_template('error_500.html'), 500


@app.route('/language')
def select_language():
    return render_template('cookie.html')


@app.route('/set-cookie', methods=["POST"])
def set_cookie():
    # Получение выбранного языка из запроса:
    language = request.form.get("lang")
    # Создание объекта ответа:
    response = make_response("Language set to: {}".format(language))
    # Установка cookie:
    response.set_cookie('lang', language)
    # Возвращаем ответ:
    return response


@app.route('/get-cookie')
def get_cookie():
    # Получение значения языка из cookie
    lang = request.cookies.get('lang')

    if lang:
        return "Language set to: {}".format(lang)
    else:
        return "Language not set."


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
