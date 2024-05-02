from flask import Flask, request, render_template, url_for, redirect, flash
from flask_migrate import Migrate
from config import Config
from models import TechData, db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def index():
    all_data = TechData.query.all()
    my_data = TechData.query.first()

    return render_template ('index.html', title='TechShop', technique=all_data, my_data=my_data)


@app.route("/insert", methods=["POST", "GET"])
def insert():
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    instock = request.form['instock']
    price = request.form['price']

    my_data = TechData(manufacturer, model, instock, price)

    db.session.add(my_data)
    db.session.commit()

    flash('Order added successfuly!!!..')    
    
    return redirect (url_for('index'))


@app.route("/update/<int:tech_id>", methods=["POST"])
def update(tech_id):
    my_data = TechData.query.get_or_404(tech_id)

    if my_data:
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        my_data.manufacturer = manufacturer
        my_data.model = model
        my_data.instock = instock
        my_data.price = price

        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('update.html', my_data=my_data)


@app.route("/delete/<int:tech_id>", methods=["GET", "POST"])
def delete(tech_id):
    my_data = TechData.query.get_or_404(tech_id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('index'))


#=============================
if __name__ == '__main__':
    app.run(debug=True)
