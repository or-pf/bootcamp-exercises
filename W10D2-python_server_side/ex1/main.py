from bottle import route, run

@route('/')
def index():
    return "Hello World- ex1"

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()