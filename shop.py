import os
from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Product, Category

shop = Blueprint('shop', __name__)
@shop.route('/home')
def home():
    category_id = request.args.get('category_id')
    products = Product.query.all()
    if category_id:
        products = Product.query.filter_by(category_id=category_id).all()
    categories = Category.query.all()
    return render_template('home.html', products=products, categories=categories)
@shop.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category_id = request.form['category']
        image = request.files['image']

        if image and image.filename:
            filename = image.filename
            image_path = os.path.join('uploads', filename)
            image.save(image_path)

            new_product = Product(title=title, description=description, category_id=category_id, image=url_for('uploads', filename=filename))
            db.session.add(new_product)
            db.session.commit()

        return redirect(url_for('shop.home'))
    categories = Category.query.all()
    return render_template('add.html', categories=categories)
@shop.route('/category_add', methods=['GET', 'POST'])
def category_add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']

        if image and image.filename:
            filename = image.filename
            image_path = os.path.join('uploads', filename)
            image.save(image_path)

            category = Category(title=title, description=description, image=url_for('uploads', filename=filename))
            db.session.add(category)
            db.session.commit()

        return redirect(url_for('shop.home'))
    return render_template('category_add.html')
