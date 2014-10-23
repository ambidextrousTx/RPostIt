'''
The main app
'''


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'A work in progress, check back later'

@app.route('/add', methods=['GET'])
def add_reminder():
    return render_template('input.html')

@app.route('/show', methods=['GET'])
def show_reminders():
    return render_template('notes.html')


if __name__ == '__main__':
    app.run()
