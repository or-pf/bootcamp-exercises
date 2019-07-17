from bottle import route, run
from jinja2 import Template

counter= {"count":0}

@route('/')
def index():
    counter["count"]+=1
    template = Template('this server has been accessed {{ my_counter }} times')    
    return template.render(my_counter=counter["count"])

if __name__ == "__main__":
    run(host='localhost', port=7001, debug=True)