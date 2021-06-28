from flask import Flask ,session , render_template , request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login' , method = 'POST')
def login():
    result_pass =  request.form['my_pass']
    
  

if __name__ == '__main__':
    app.run(debug=True)
