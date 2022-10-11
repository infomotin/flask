from flask import Flask, render_template, request, redirect, url_for
# inport rander_template 
# from flask import render_template
# for demo data crete a dics 
data =[
    {'name':'sachin','age':25},
    {'name':'saurav','age':30},
    {'name':'rahul','age':35},
    {'name':'virat','age':40},
    {'name':'rohit','age':45},
    {'name':'dhoni','age':50},
    {'name':'jadeja','age':55},
]
# create flask app
app = Flask(__name__)
# create home route 
@app.route('/',methods=['GET','POST'])
def home():
    # get data from url request
    if request.method == 'POST':
        name = request.form['name']

        email = request.form['email']
        password = request.form['password']
        # add data to list
        data.append({'name':name,'email':email,'password':password})
        print(name,email,password)

    return render_template('index.html', data=data)
# create about route page 
@app.route('/about')
def about():
    return render_template('about.html')

# create server and run 
if __name__ == '__main__':
    app.run(debug=True)
