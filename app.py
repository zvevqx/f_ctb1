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
    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    return render_template('home.html', articles=latest)



@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    return render_template('single.html', page=page)







