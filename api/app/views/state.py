from flask import Flask, request, jsonify
from app import app
from app.models.state import State

@app.route('/states', methods=['GET', 'POST'])
def states():
    if request.method == 'GET':
        #get list states
        states_list = []
        states = State.select()
        for state in states:
            states_list.append(state.to_hash())
        return jsonify(states_list)

    elif request.method == 'POST':
        #create new state
        post_name = request.form['name']
        states = State.select()
        for state in states:
            if state.name == post_name:
                message = {
                    'code': 10001,
                    'msg': 'State already exists',
                }
                res = jsonify(message)
                res.status_code = 409
                return res
        else:
            new_state = State.create(name=post_name)
            return jsonify(new_state.to_hash())

@app.route('/states/<state_id>', methods=['GET', 'DELETE'])
def state_id(state_id):
    if request.method == 'GET':
        #get state from state_id
        state = State.get(State.id == state_id)
        return jsonify(state.to_hash())

    elif request.method == 'DELETE':
        #delete state with id state_id
        state = State.get(State.id == state_id)
        state.delete_instance()
        return 'State %s deleted \n' % state_id
