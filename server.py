from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def render_page(page_name):
    try:
        return render_template(page_name)
    except Exception as e:
        app.logger.error(f"Error rendering page {page_name}: {e}")
        return "Page not found", 404

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if not validate_form_data(data):
                return "Invalid form data. Please fill out all fields.", 400
            write_to_file(data)
            write_to_csv(data)
            return 'Thank you! Form submitted successfully!', 200
        except Exception as e:
            app.logger.error(f"Error submitting form: {e}")
            return "An error occurred while submitting the form. Please try again later.", 500
    else:
        return "Invalid request method.", 405

def validate_form_data(data):
    """Validate that all required fields are present and not empty."""
    required_fields = ['name', 'email', 'subject', 'message']
    return all(field in data and data[field].strip() for field in required_fields)

def write_to_csv(data):
    """Write form data to a CSV file."""
    file_path = os.path.join(os.getcwd(), 'database2.csv')
    with open(file_path, mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['name'], data['email'], data['subject'], data['message']])

def write_to_file(data):
    """Write form data to a text file."""
    file_path = os.path.join(os.getcwd(), 'database.txt')
    with open(file_path, mode='a') as database:
        database.write(f"{data['name']}, {data['email']}, {data['subject']}, {data['message']}\n")