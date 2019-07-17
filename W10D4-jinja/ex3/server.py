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
    greeting = Template('<h1> Welcome {{first_name}} </h1><p> We are very happy to greet you {{first_name}} {{last_name}}!</p><p>congrats {{first_name}} You won the lottery! in order to get the prize you need to:</p>')
    winning= Template('<ul><li>send us an email to lottary@gmail.com</li><li> attatch to the email a picture of yourself</li><li>wait for a reply</li></ul>')
    trying= Template('<ul><li>fill in our winners form in http://hitechlottery.com/form</li><li>wait for a reply</li></ul>')
    
    if new_user["first_name"][0]=="g":
        return greeting.render(first_name= new_user["first_name"], last_name= new_user["last_name"]), winning.render()
    else:
        return greeting.render(first_name= new_user["first_name"], last_name= new_user["last_name"]), trying.render()

if __name__ == "__main__":
    run(host='localhost', port=7002, debug=True, reloader=True)