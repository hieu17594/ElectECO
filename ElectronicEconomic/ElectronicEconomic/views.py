"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask
from ElectronicEconomic import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.jade',
        title='Login',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/contact-us')
def contactUS():
    """Renders the contact page."""
    return render_template(
        'contact-us.jade',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/checkout')
def checkout():
    """Renders the contact page."""
    return render_template(
        'checkout.jade',
        title='Checkout',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/cart')
def cart():
    """Renders the contact page."""
    return render_template(
        'cart.jade',
        title='Cart',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/shop')
def shop():
    """Renders the contact page."""
    return render_template(
        'shop.jade',
        title='Shop',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/product-details')
def productDetails():
    """Renders the contact page."""
    return render_template(
        'product-details.jade',
        title='Product Details',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/blog')
def blog():
    """Renders the contact page."""
    return render_template(
        'blog.jade',
        title='Blog',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/blog-single')
def blogSingle():
    """Renders the contact page."""
    return render_template(
        'blog-single.jade',
        title='Blog Single',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/404')
def Erorr():
    """Renders the contact page."""
    return render_template(
        'error.jade',
        title='404',
        year=datetime.now().year,
        message='Your contact page.'
    )
