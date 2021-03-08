import flask

app = flask.Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

def readfromtxt():
    with open("requests.txt", "r") as f:
        return f.read()

def inctxt():
    with open("requests.txt", "r+") as f:
        try:
            count = int(f.read())
            count+=1
            newcount = count
            f.seek(0)
            f.truncate()
            f.write(str(newcount))
        except:
            f.seek(0)
            f.truncate()
            f.write("SOMETHING WENT WRONG, PLEASE CONTACT THE AUTHOR OF THIS PAGE")

@app.route('/')
def home():
    inctxt()
    return flask.render_template('index.html', requests=readfromtxt())


from waitress import serve
import os
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 5000
serve(app, listen=f'*:{port}')
