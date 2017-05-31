from flask import Flask, request, jsonify
from app import app
from app.models.user import User

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        #get list users
        user_list = []
        users = User.select()
        for user in users:
            user_list.append(user.to_hash())
            return jsonify(user_list)

    elif request.method == 'POST':
        #create new user
        post_first_name = request.form['first_name']
        post_last_name = request.form['last_name']
        post_email = request.form['email']
        post_password = request.form['password']
        post_is_admin = request.form['is_admin']
        users = User.select()
        for user in users:
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

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_id(user_id):
    if request.method == 'GET':
        #get user with id
        user = User.get(User.id == user_id)
        return jsonify(user.to_hash())

    if request.method == 'PUT':
        #update user with id
        put_first_name = request.form['first_name']
        put_last_name = request.form['last_name']
        put_is_admin = request.form['is_admin']
        put_password = request.form['password']
        users = User.select()
        for user in users:
            if user.first_name != put_first_name:
                User.update(first_name=put_first_name).where(User.id == user_id)
            if user.last_name != put_last_name:
                User.update(last_name=put_last_name).where(User.id == uesr_id)
            if user.is_admin != put_is_admin:
                User.update(is_admin=put_is_admin).where(User.id == user_id)
        updated_user = User.get(User.id == user_id)
        return jsonify(user.to_hash())
