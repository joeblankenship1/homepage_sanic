from sanic import Sanic
from sanic.response import json, html, text
from jinja2 import Environment, PackageLoader, select_autoescape

# define the environment for the Jinja2 templates
env = Environment(
    loader=PackageLoader('main', 'templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl'])
)


# a function for loading an HTML template from the Jinja environment
def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


# create the Sanic app and serve it statically
app = Sanic(__name__)
app.static('/static', './static')


# define our function for our homepage
@app.route('/')
async def home(request):
    greeting = 'Hello, Sanic!'
    link = 'https://sanic.readthedocs.io/en/latest/'
    return template(
        'index.html',
        title='Sanic Website - Demo',
        greeting=greeting,
        button=link
    )


# define our function for our homepage
@app.route('/about')
async def about(request):
    greeting = 'About'
    link = 'https://github.com/huge-success/sanic'
    return template(
        'about.html',
        title='Sanic Website - Demo',
        greeting=greeting,
        link=link
    )


# run the main.py on http://localhost:8000
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
