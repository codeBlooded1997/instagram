from flask import Flask, render_template, request
from backend import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    #user_id = request.form['user']
    scraper = InstaScraper()
    scraper.run()

    return render_template('results.html', result=scraper.results)

if __name__ == "__main__":
    app.run(debug=True, threaded = True)