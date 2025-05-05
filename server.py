from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def render_page(page_name):
    try:
        return render_template(page_name)
    except Exception as e:
        return f"Error: {e}", 404



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return 'Thank you form submitted successfully!', 200
        except Exception as e:
            return f"Error: {e}", 500
    else:
        return "Something went wrong. Try again!"
    
def write_to_csv(data):
    with open('database2.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')
        print(file)