from flask import Flask, render_template, request
import json

app = Flask(__name__)
students = {}
my_data_file='students.json'


@app.route('/login' , methods=['GET' , 'POST'])
def logg():
    if request.method == 'POST':
        req_username = request.form['username']
        req_password = request.form['password']
        for key, value in students.items():
             if key == req_username and value == int (req_password):
                 return render_template('success.html' , username=req_username)
        else:
            msg="try again"
            return render_template('index3.html' , msg=msg)
    return render_template('index3.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        req_username = request.form['username']
        req_password = request.form['password']
        students[req_username] = int(req_password)
        save_data()
        return render_template('successreg.html', username=req_username)
    return render_template('register.html')

@app.route('/load_data', methods=['GET'])
def load_data():
    global students
    with open(my_data_file, 'r') as file:
        json_string = file.read()
        students = json.loads(json_string)
    return "Data loaded successfully"


@app.route('/', methods=['GET'])
def main():
    global students
    return render_template('main.html')
    

def save_data():
    with open(my_data_file, 'w') as file:
        json.dump(students, file)

if __name__ == '__main__':
    load_data()
    app.run(debug=True)

