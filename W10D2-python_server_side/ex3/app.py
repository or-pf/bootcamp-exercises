from bottle import route, static_file, run

@route('/')
def get_my_page():
    return static_file("index.html", root="")


@route('/static/css/<filename:re:.*\.css>')
def get_my_css(filename):
    return static_file(filename,  root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def get_my_js(filename):
    return static_file(filename,  root='static/js')


@route('/static/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def get_my_pics(filename):
    return static_file(filename,  root='static/images')

if __name__ == "__main__":
    run(host='localhost', port=8000, reloader=True)