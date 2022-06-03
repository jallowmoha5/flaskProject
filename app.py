# import flask and template
from flask import Flask, render_template

# import pandas library
import pandas as pd

# initialize the flask app
app = Flask(__name__)

# reading the data in the csv file
df = pd.read_csv('config/data.csv')
df.to_csv('data.csv', index=None)


# route to html page  "table"
@app.route('/')
@app.route('/table')
def table():
    # converting csv to html
    global data
    try:
        data = pd.read_csv('data.csv')
    except NameError:
        print("Please install pandas or load csv file")

    return render_template('table.html', tables=[data.to_html()], titles=[''])


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"), debug=False)
