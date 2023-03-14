from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template
import os

FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True

app = Flask(__name__) 
app.config['APPLICATION_ROOT'] = '/flaskapp'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config.from_object(__name__)
pages = FlatPages(app)
application = app
pages.get('foo')

def Liste_cat():
    articles = (p for p in pages if 'published' in p.meta)
    catList = []
    for a in articles:
        catList.append(a.meta['cat'])
    catList = list(dict.fromkeys(catList))
    return catList 

def imagelist(articlename):
    dir_path = os.path.dirname(os.path.realpath(articlename))+'/pages/'
    gallery_path = os.path.join(dir_path, articlename)
    if os.path.exists(gallery_path):
        images = [f for f in os.listdir(gallery_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.gif')]
        return gallery_path ,images
    else:
        return None, None

@app.errorhandler(404)
def page_not_found(e):
        # note that we set the 404 status explicitly
            return "NOPE NOTHING HERE plz leave now 🛸"

#@app.route(app.config['APPLICATION_ROOT'] + '/')
@app.route('/')
def index():
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    catList = Liste_cat()
    return render_template('index.html', articles=latest , catList=catList  )

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    catList = Liste_cat()
    g_path, imgs = imagelist(path)
    if imgs:
        return render_template('single.html', page=page ,catList=catList  , g_path=g_path, imgs = imgs)
    else :
        return render_template('single.html', page=page ,catList=catList)

@app.route('/info')
def info():
    page = pages.get_or_404('info')
    catList = Liste_cat()
    return render_template('staticpage.html', page=page , catList=catList)

@app.route('/cat/<catname>')
def catPage(catname):
    articles = (p for p in pages if 'published' in p.meta and 'cat' in p.meta and p.meta['cat']==catname )
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    catList = Liste_cat()
    return render_template('index.html', articles=latest , catList=catList  )

@app.route('/author/<authorname>')
def authorPage(authorname):
    articles = (p for p in pages if 'published' in p.meta and 'author' in p.meta and p.meta['author']==authorname )
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    catList = Liste_cat()
    return render_template('index.html', articles=latest , catList=catList  )


@app.route('/yolo')
def app1():
        return 'This is app1!'


if __name__ == "__main__":
        app.run(host='0.0.0.0')
