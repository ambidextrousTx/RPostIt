'''
The main app
'''


from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'A work in progress, check back later'

@app.route('/add', methods=['POST'])
def add_reminder():
    return 'Use this method to POST new reminders to the database'

@app.route('/show', methods=['GET'])
def show_reminders():
    return 'Use this method to GET all the reminders in the database' \
            'in a sticky format'


if __name__ == '__main__':
    app.run()
