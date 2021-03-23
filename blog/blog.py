from flask import Blueprint, render_template
from markupsafe import escape

#from flask_flatpages import FlatPages

bp = Blueprint('blog', __name__)

from app import pages

#FLATPAGES_AUTO_RELOAD = DEBUG
#FLATPAGES_EXTENSION = [".md", ".markdown"]
#POST_DIR = 'posts'
#FLATPAGES_AUTO_RELOAD = DEBUG
#FLATPAGES_EXTENSION = '.md'

@bp.route('/')
def index():
    #page = pages.get('hello')
    #print(type(pages))
    #page = pages.get('hello')
    #print(page.title)
    return render_template("blog/index.html", pages=pages)

@bp.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('blog/page.html',page=page) 

@bp.route('/blog')
def blog():
    return render_template("blog/index.html", pages=pages)

@bp.route('/<string:tag>/')
def tag(tag):
    tagged = [page for page in pages if tags in page.meta.get("tags", [])]
    #tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    #print("tagged:", _tagged)
    return render_template("blog/tag.html", tagged=tagged, tag=tag)