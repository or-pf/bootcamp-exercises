from bottle import route, run, jinja2_view, request
import functools

view = functools.partial(jinja2_view, template_lookup=['templates'])


@route('/')
@view('signup.html')
def index():
    return {}

@route('/lottery', method='POST')
@view('lottery.html')
def greeting():
    new_user = {
    "first_name": request.forms.get("first_name"),
    "last_name": request.forms.get("last_name")
    }
    Win = False
    steps = []
    if new_user["first_name"][0].lower()=="g":
        Win= True
        steps=["send us an email to lottary@gmail.com", "attatch to the email a picture of yourself", "wait for a reply"]
    
    if new_user["first_name"][0].lower()=="d":
        Win= True
        steps=["fill in our winners form in http://hitechlottery.com/form", "wait for a reply"]
        
    return {"new_user": new_user, "Win": Win, "steps": steps}

if __name__ == "__main__":
    run(host='localhost', port=7004, debug=True, reloader=True)
