import flask

app = flask.Flask(__name__)

def readfromtxt():
    with open("requests.txt", "r") as f:
        return f.read()

def inctxt():
    with open("requests.txt", "r+") as f:
        count = int(f.read())
        count+=1
        newcount = count
        f.seek(0)
        f.truncate()
        f.write(str(newcount))

@app.route('/')
def home():
    inctxt()
    return f'This website got requested: {readfromtxt()}'


