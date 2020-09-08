from flask import Flask, render_template,request,redirect # this render_template help us to use html files
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database','a') as db:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=db.write(f'\n{email}{subject}{message}')
def write_to_csv(data):
    with open('database.csv','a',newline='') as db2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer = csv.writer(db2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])#post & get are default method help to grab data in DB
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'


