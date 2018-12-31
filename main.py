from sanic import Sanic
from sanic.response import json, html, text
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('main', 'templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl'])
)


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


app = Sanic(__name__)
app.static('/static', './static')


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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
