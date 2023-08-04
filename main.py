from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    prise = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        prise = request.form['price']

        shop = Shop(title=title, prise=prise)

        try:
            db.session.add(shop)
            db.session.commit()
            return redirect('/')
        except:
            return 'Ошибка'
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)