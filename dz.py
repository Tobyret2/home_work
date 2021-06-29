from flask import Flask ,session , redirect , render_template , request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['username']
  
@app.route('/reg',  methods=['POST'])
def reg():
    # if request.method == 'POST':
    #     return 'spasibo'
    return '''
        <form action="ya.ru" method="post">
            <p><input type=text name=user>
            <p><input type=text name=password>
            <p><input type=submit value=registration>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)