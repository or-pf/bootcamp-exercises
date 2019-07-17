from bottle import route, run, request, static_file
from jinja2 import Template

@route('/signup')
def login():
    return static_file("index.html", root="")
       

@route('/signup', method='POST')
def do_login():
    new_user = {
    "first_name": request.forms.get("first_name"),
    "last_name": request.forms.get("last_name")
    }
    greeting = Template('<h1> Welcome {{first_name}} </h1><p> We are very happy to greet you {{first_name}} {{last_name}}!</p>')
    return greeting.render(first_name= new_user["first_name"], last_name= new_user["last_name"])


if __name__ == "__main__":
    run(host='localhost', port=7002, debug=True, reloader=True)