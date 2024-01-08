 
# Import necessary libraries
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/supervised_learning')
def supervised_learning():
    return render_template('supervised_learning.html')

@app.route('/unsupervised_learning')
def unsupervised_learning():
    return render_template('unsupervised_learning.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
