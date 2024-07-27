from flask import Flask, jsonify

app = Flask(__name__) # Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

@app.route('/') #We then use the route() decorator to tell Flask what URL should trigger our function.
def home():
    return 'Hello, World! This is the index page for our pending app'

@app.route('/about')
def about():
    return 'Here is a place where you can learn more about our hackathon team'

@app.route('/error') 
def error():
    return 'Uh oh, page not found.'

#Mock API:

@app.route('/api/data', methods=['GET']) 
def get_data():
    return jsonify({'message':'This is the get route for retrieving the data'})

if __name__ == '__main__':
    app.run(debug=True)

# https://flask.palletsprojects.com/en/3.0.x/quickstart/