from flask import Flask, request, jsonify
from app import app
from app.models.state import State
from app.models.city import City

@app.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def cities(state_id):
    if request.method == 'GET':
        #get cities list
        cities_list = []
        cities = City.select(City, State).join(State).where(City.state == state_id)
        for city in cities:
            cities_list.append(city.to_hash())
        return jsonify(cities_list)

    elif request.method == 'POST':
        post_name = request.form['name']
        cities = City.select(City, State).join(State).where(City.state == state_id)
        for city in cities:
            if city.name == post_name:
                message = {
                    'code': 10002,
                    'msg': 'City already exists in this state',
                }
                res = jsonify(message)
                res.status_code = 409
                return res
        else:
            new_city = City.create(name=post_name, state_id=state_id)
            return jsonify(new_city.to_hash())

@app.route('/states/<state_id>/cities/<city_id>', methods=['GET', 'DELETE'])
def city_id(state_id, city_id):
    if request.method == 'GET':
        city = City.get(City.id == city_id, City.state == state_id)
        return jsonify(city.to_hash())

    elif request.method == 'DELETE':
        city = City.get(City.id == city_id, City.state == state_id)
        city.delete_instance()
        return 'City %s deleted \n' % city_id
