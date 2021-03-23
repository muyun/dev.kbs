from flask import Blueprint, render_template

#from flask_flatpages import FlatPages

bp = Blueprint('info', __name__)

from app import pages

@bp.route('/link')
def link():
    page = pages.get_or_404('link')
    return render_template('info/link.html', page=page)

@bp.route('/business')
def business():
    page = pages.get_or_404('business')
    return render_template('info/business.html', page=page) 

@bp.route('/proj')
def proj():
    page = pages.get_or_404('proj')
    return render_template('info/proj.html', page=page)

@bp.route('/book')
def book():
    page = pages.get_or_404('book')
    return render_template('info/book.html', page=page)

@bp.route('/invest')
def invest():
    page = pages.get_or_404('invest')
    return render_template('info/invest.html', page=page) 

@bp.route('/about')
def about():
    page = pages.get_or_404('about')
    return render_template('info/about.html', page=page)
