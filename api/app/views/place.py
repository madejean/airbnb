from flask import Flask, request, jsonify
from app import app
from app.models.place import Place
from app.models.city import City
from app.models.state import State

@app.route('/places', methods=['GET', 'POST'])
def places():
    if request.method == 'GET':
        places_list = []
        places = Place.select()
        for place in places:
            places_list.append(place.to_hash())
        return jsonify(places_list)

    elif request.method == 'POST':
        new_place = Place.create(
            owner=request.form['owner'],
            city=request.form['city'],
            name=request.form['name'],
            description=request.form['description'],
            number_rooms=request.form['number_rooms'],
            number_bathrooms=request.form['number_bathrooms'],
            max_guest=request.form['max_guest'],
            price_by_night=request.form['price_by_night'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
            )
        return jsonify(new_place.to_hash())

@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def place_id(place_id):
    if request.method == 'GET':
        place = Place.get(Place.id == place_id)
        return jsonify(place.to_hash())

    if request.method == 'PUT':
        try:
            update_place = Place.update(name=request.form['name']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(description=request.form['description']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(number_rooms=request.form['number_rooms']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(number_bathrooms=request.form['number_bathrooms']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(max_guest=request.form['max_guest']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(price_by_night=request.form['price_by_night']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(latitude=request.form['latitude']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        try:
            update_place = Place.update(longitude=request.form['longitude']).where(Place.id == place_id)
            update_place.execute()
        except:
            pass
        updated_place = Place.get(Place.id == place_id)
        return jsonify(updated_place.to_hash())

    elif request.method == 'DELETE':
        place = Place.get(Place.id == place_id)
        place.delete_instance()
        return 'Place %s deleted \n' % place_id

@app.route('/states/<state_id>/cities/<city_id>/places', methods=['GET', 'POST'])
def places_in_city(state_id, city_id):
    if request.method == 'GET':
        places_list = []
        places = Place.select().join(City).where(Place.city == city_id, City.state == state_id)
        for place in places:
            places_list.append(place.to_hash())
        return jsonify(places_list)
