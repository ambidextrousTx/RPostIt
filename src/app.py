'''
The main app
'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Go to /add or /show instead'

@app.route('/add', methods=['GET'])
def add_reminder():
    return render_template('input.html')

@app.route('/show', methods=['GET'])
def show_reminders(reminder):
    return render_template('notes.html', reminder=reminder)

@app.route('/justadded', methods=['POST'])
def add_entry():
    return show_reminders(request.form['postitnote'])


if __name__ == '__main__':
    app.run(debug=True)
