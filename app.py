def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return bytes('Yo!!!', 'utf-8')