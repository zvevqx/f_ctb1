from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template

FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True

app = Flask(__name__) 
app.config.from_object(__name__)
pages = FlatPages(app)

pages.get('foo')

def Liste_cat():
    articles = (p for p in pages if 'published' in p.meta)
    catList = []
    for a in articles:
        catList.append(a.meta['cat'])
    catList = list(dict.fromkeys(catList))
    return catList 

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
    return render_template('single.html', page=page ,catList=catList )

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


