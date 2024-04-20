from flask import Flask, request
app = Flask(__name__)
def get_html(users):
    return  f'''
    <html>
        <body>
            Спсиок товаров <br>
            <form action = "http://localhost:5000/submit" method = "post">
                <p>Кто ты: </p>
                <p> <input type = "text" name="имя"/> </p>
                <p> <input type = "submit" value="отправси"/> </p>
            </form>
            здесь были: {users}
        </body>
    </html>
    '''
users_list = list()
@app.route('/')
def hello_world():
    return get_html(users_list)
@app.route('/submit', methods = ['POST'])
def submit():
    users_list.append(request.form["имя"])
    return 'ok'
app.run('0.0.0.0')
