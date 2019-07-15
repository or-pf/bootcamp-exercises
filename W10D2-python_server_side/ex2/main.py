from bottle import route, run, static_file
import json
import random

colors=[
    {"name":"red", "code":"#FF0000"},
    {"name":"blue", "code":"#0000FF"},
    {"name":"yellow", "code":"#FFFF00"},
    {"name":"black", "code":"#000000"},
    {"name":"coral", "code":"#FF7F50"},
    {"name":"deepPink", "code":"#FF1493"}
]
@route('/')
def get_colors():
    return static_file("index.html", root="")

@route('/colorslist')
def get_colors_list():
    color_chosen= random.choice(colors)
    return json.dumps(color_chosen)
   

if __name__ == "__main__":
    run(host='localhost', port=7000)