from bottle import route, static_file, run, response, error

@route('/')
def main_page():
    return "This is the main page"

@error(404)
def not_found(error):
    return static_file("404.html", root="")

if __name__ == "__main__":
    run(host='localhost', port=7001, reloader=True)