from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def Home(name=None):
    return render_template('home.html', name = 'home')

# if __name__=="__main__":
#     app.run()

# debud mode running on 8000 port
if __name__=="__main__":
    app.run(debug=True, port=8000)