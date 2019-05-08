import flask
from flask import request, jsonify
from predictor_api import make_api_prediction, feature_names

# Initialize the app

app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
@app.route("/")
def get_predict_page():
    "Returns the rendered page"
    # We can try other template pages as well.
    # Change this line to any of the other html files in the template folder
    # Described in README
    return flask.render_template('index.html')

@app.route("/predict_api", methods=["POST"])
def get_api_response():
    # This function will throw an error if we are missing one of
    # the features it expects. Any status code that is not 200 - 299
    # is flagged as an error
    try:
        print(request.json)
        feature_dictionary=request.json
        category_list = ['main_category_comics',
       'main_category_crafts', 'main_category_dance', 'main_category_design',
       'main_category_fashion', 'main_category_film & video',
       'main_category_food', 'main_category_games', 'main_category_journalism',
       'main_category_music', 'main_category_photography',
       'main_category_publishing', 'main_category_technology',
       'main_category_theater']
        input_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #print('made it this far')
        category_input = feature_dictionary["category_input"]
        if category_input in category_list:
            print(category_list.index(category_input))
            input_list[category_list.index(category_input)] = 1
        i=0
        #print('worked so far')
        for item in category_list:
            feature_dictionary[item]=input_list[i]
            i=i+1
        #print('worked')
        print(feature_dictionary)
        response = make_api_prediction(feature_dictionary)
        #response = {"msg":"this is amazing"}
        status = 200
    except KeyError:
        missing = [f for f in feature_names if f not in request.json]
        response = {
            'status': 'error',
            'msg': f'not all required feature names ({feature_names}) present. Missing {missing}'
        }
        status = 300
    return jsonify(response), status


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
if __name__ == '__main__':
    app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
