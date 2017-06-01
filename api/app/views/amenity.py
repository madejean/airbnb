from flask import Flask, request, jsonify
from app import app
from app.models.amenity import Amenity

@app.route('/amenities', methods=['GET', 'POST'])
def amenities():
    if request.method == 'GET':
        amenities_list = []
        amenities = Amenity.select()
        for amenity in amenities:
            amenities_list.append(amenity.to_hash())
        return jsonify(amenities_list)

    elif request.method == 'POST':
        amenities = Amenity.select()
        for amenity in amenities:
            if amenity.name == request.form['name']:
                message = {
                    'code': 10003,
                    'msg': 'Amenity already exists',
                }
                res = jsonify(message)
                res.status_code = 409
                return res

        else:
            new_amenity = Amenity.create(name=request.form['name'])
            return jsonify(new_amenity.to_hash())

@app.route('/amenities/<amenity_id>', methods=['GET', 'DELETE'])
def amenity_id(amenity_id):
    if request.method == 'GET':
        amenity = Amenity.get(Amenity.id == amenity_id)
        return jsonify(amenity.to_hash())

    elif request.method == 'DELETE':
        amenity = Amenity.get(Amenity.id == amenity_id)
        amenity.delete_instance()
        return 'Amenity %s deleted \n' % place_id

@app.route('/places/<place_id>/amenities', methods=['GET'])
def amenities_in_places(place_id):
    if request.method == 'GET':
        amenities_list = []
        amenities = Amenity.select().join(Place).where(Place.id == place_id)
        for amenity in amenities:
            amenities_list.append(amenity.to_hash())
        return jsonify(amenities_list)
