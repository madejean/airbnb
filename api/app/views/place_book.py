from flask import Flask, request, jsonify
from app import app
from app.models.place_book import PlaceBook
from app.models.place import Place

@app.route('/places/<place_id>/books', methods=['GET', 'POST'])
def states(place_id):
    if request.method == 'GET':
        books_list = []
        books = PlaceBook.select().join(Place).where(Place.id == place_id)
        for book in books:
            books_list.append(book.to_hash())
        return jsonify(books_list)

    elif request.method == 'POST':
        new_book = PlaceBook.create(
            place=request.form['place'],
            user=request.form['user'],
            is_validated=request.form['is_validated'],
            date_start=request.form['date_start'],
            number_nights=request.form['number_nights'],
        )
        return jsonify(new_book.to_hash())

@app.route('/places/<place_id>/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_id(place_id, book_id):))
    if request.method == 'GET':
        book = Book.get(PlaceBook.id == book_id, PlaceBook.place == place_id)
        return jsonify(book.to_hash())

    if request.method == 'PUT':
        try:
            update_book = PlaceBook.update(place=request.form['place']).where(PlaceBook.place == place_id, PlaceBook.id == book_id)
            update_book.execute()
        except:
            pass
        try:
            update_book = PlaceBook.update(is_validated=request.form['is_validated']).where(PlaceBook.place == place_id, PlaceBook.id == book_id)
            update_book.execute()
        except:
            pass
        try:
            update_book = PlaceBook.update(date_start=request.form['date_start']).where(PlaceBook.place == place_id, PlaceBook.id == book_id)
            update_book.execute()
        except:
            pass
        try:
            update_book = PlaceBook.update(number_nights=request.form['number_nights']).where(PlaceBook.place == place_id, PlaceBook.id == book_id)
            update_book.execute()
        except:
            pass

    elif request.method == 'DELETE':
        book = PlaceBook.get(PlaceBook.id == book_id, PlaceBook.place == place_id)
        book.delete_instance()
        return 'Book %s deleted \n' % book_id
