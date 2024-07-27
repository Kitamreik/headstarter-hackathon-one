from flask import Flask, jsonify, url_for, request
from flask_cors import CORS #update after installing cors and setting up react boilerplate

app = Flask(__name__) # Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
CORS(app)

@app.route('/') #We then use the route() decorator to tell Flask what URL should trigger our function.
def home():
    return jsonify({'message':'Hello, World! This is the index page for our pending app'})

@app.route('/about')
def about():
    return jsonify({'message':'Here is a place where you can learn more about our hackathon team'})


@app.route('/error') 
def error():
    return jsonify({'error':'Uh oh, page not found.'})

#Mock API:

@app.route('/api/data', methods=['GET']) 
def get_data():
    return jsonify({'message':'This is the get route for retrieving the data'})

@app.route('/api/data/create', methods=['GET', 'POST']) 
def post_data():
    if request.method == 'POST':
        return 'Success'
    else:
        return jsonify({'message':'This is the create route for posting the data'})

if __name__ == '__main__':
    app.run(debug=True)

# https://flask.palletsprojects.com/en/3.0.x/quickstart/