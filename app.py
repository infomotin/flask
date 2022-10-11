from flask import Flask

# create flask app
app = Flask(__name__)
# create home route 
@app.route('/')
def home():
    return 'Hello World'
# create about route page 
@app.route('/about')
def about():
    return 'About Page'

# create server and run 
if __name__ == '__main__':
    app.run()
