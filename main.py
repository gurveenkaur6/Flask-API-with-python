from flask import Flask, jsonify, request
# jsonify to create a json resonse, but why?


app= Flask(__name__)

# create a root -  endpoint of our API, we write a function to create a root. To make the root accessible,
# we use a python decorator like @

# @app.route("/")
# def home():
#     return "Home"

# GET route - to fetch the user data and some extra queries. GET is the default request.
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "users_id" : user_id,
        "name" : "John Doe",
        "email" : "john.doe@gmail.com"
    }
    # query parameters - extra value included after the main path. Eg: get-user/123?extra=hello world
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    # return dict data in json format to the user, 200 is the default status code of success
    return jsonify(user_data), 200

# Method =  POST
@app.route("/create-user", methods =["POST"])
def create_user():
    data = request.get_json()
    # add data to a database

    # return a "succesfully added user data" message
    return jsonify(data), 201


# Testing the APIs using postman


if __name__ =="__main__":
    app.run(debug=True)