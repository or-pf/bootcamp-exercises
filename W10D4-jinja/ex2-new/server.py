from bottle import route, run, jinja2_view, request
import functools

view = functools.partial(jinja2_view, template_lookup=['templates'])


@route('/')
@view('signup.html')
def index():
    return {}

@route('/signup', method='POST')
@view('greeting.html')
def greeting():
    new_user = {
    "first_name": request.forms.get("first_name"),
    "last_name": request.forms.get("last_name")
    }
    return new_user

if __name__ == "__main__":
    run(host='localhost', port=7004, debug=True, reloader=True)
