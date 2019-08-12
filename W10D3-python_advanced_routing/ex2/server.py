from bottle import route, static_file, run, get
import feedparser
import json

# print(d['feed']['title'])



@route('/')
def get_my_page():
    return static_file("index.html", root="")

@get('/rss/jpost')
def get_info():
    d = feedparser.parse('https://www.jpost.com/Rss/RssFeedsHeadlines.aspx')
    return json.dumps(d["entries"])

@get('/rss/themarker')
def show_info():
    d = feedparser.parse('http://www.themarker.com/cmlink/1.145')
    return json.dumps(d["entries"])
    
@route('/static/css/<filename:re:.*\.css>')
def get_my_css(filename):
    return static_file(filename,  root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def get_my_js(filename):
    return static_file(filename,  root='static/js')

if __name__ == "__main__":
    run(host='localhost', port=8000, reloader=True)