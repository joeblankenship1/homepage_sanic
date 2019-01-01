from sanic import Sanic

# create an app object
app = Sanic(__name__)
# serve your static data file at /
# you can stipulate virtual host with host='url'
# if your data is large, use stream_large_files=True
app.static('/', 'census_2010_ky.json', name='census')
# run the app
app.run(host="0.0.0.0", port=8080)
