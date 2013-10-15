from wsgiref.simple_server import make_server

def application(environ, start_response):
    path = environ.get('PATH_INFO')
    if path == '/':
        response_body = "Index"
    else:
        response_body = "Hello"
    status = "200 OK"
    #response_headers = [("Content-Length", str(len(response_body)))]
    response_headers = []
    response_headers.append(('Content-Type', 'text/plain'))
    start_response(status, response_headers)
    return [response_body]

httpd = make_server(
    '127.0.0.1', 8051, application)

httpd.serve_forever()
