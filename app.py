from flask import Flask
from flask_flatpages import FlatPages
from flask import render_template



FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True

app = Flask(__name__) 
app.config.from_object(__name__)
pages = FlatPages(app)

pages.get('foo')


@app.route('/')
def index():
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])

    catList = []
    for a in latest:
        catList.append(a.meta['cat'])
    
    catList = list(dict.fromkeys(catList))

    return render_template('index.html', articles=latest , catList=catList  )



@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    return render_template('single.html', page=page)







