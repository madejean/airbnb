from flask import Flask, request, jsonify
from app import app
from app.models.user import User

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        #get list users
        users_list = []
        users = User.select()
        for user in users:
            users_list.append(user.to_hash())
        return jsonify(users_list)

    elif request.method == 'POST':
        #create new user
        post_first_name = request.form['first_name']
        post_last_name = request.form['last_name']
        post_email = request.form['email']
        post_password = request.form['password']
        users = User.select()
        for user in users:
            if user.email == post_email:
                message = {
                    'code': 10000,
                    'msg': 'User already exists',
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
        try:
            update_user = User.update(first_name=request.form['first_name']).where(User.id == user_id)
            update_user.execute()
        except:
            pass
        try:
            update_user = User.update(last_name=request.form['last_name']).where(User.id == user_id)
            update_user.execute()
        except:
            pass
        updated_user = User.get(User.id == user_id)
        return jsonify(updated_user.to_hash())

    elif request.method == 'DELETE':
        user = User.get(User.id == user_id)
        user.delete_instance()
        return 'User %s deleted \n' % user_id
