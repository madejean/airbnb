from flask import Flask, request, jsonify
from app import app
from app.models.user import User

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        #get list users
        users = []
        query_users = User.select()

        for user in query_users:
            users.append(user.to_hash())
            return jsonify(users)

    elif request.method == 'POST':
        #create new user
        post_first_name = request.form['first_name']
        post_last_name = request.form['last_name']
        post_email = request.form['email']
        post_password = request.form['password']
        query_users = User.select()
        for user in query_users:
            if user.email == post_email:
                message = {
                    'code': 10000,
                    'message': 'User already exists',
                }
                res = jsonify(message)
                res.status_code = 409

            return res

        else:
            new_user = User.create(first_name=post_first_name, last_name=post_last_name, email=post_email, password=post_password)
            return jsonify(new_user.to_hash())
