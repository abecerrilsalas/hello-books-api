from app import db
from app.models.book import Book
from flask import request, Blueprint, Response, jsonify, make_response

books_bp =Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET", "POST"])#it says give me all the books or alternatively, create a book. 
def books():
    if request.method =="GET":#here we talk about multiple books
        title_from_url = request.args.get("title")####new
        if title_from_url:
            books = Book.query.filter_by(title=title_from_url)####new. stores all of the books with that title. 
        else:####new
            books=Book.query.all()####new
        books_response=[]
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response)
    elif request.method == "POST":
        request_body=request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("<book.id>", methods=["GET", "PUT", "DELETE"])#in this function would be the best place to add the 404 status code
def book(book_id):
    book=Book.query.get(book_id)

    if book == None:######new
        return make_response("", 404)

    if request.method == "GET":
        return{
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    elif request.method == "PUT":
        form_data=request.get_json()

        book.title = form_data ["title"]
        book.description = form_data ["description"]

        db.session.commit()

        return Response(f"Book #{book.id} successfully updated", status=200)
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return Response(f"Book #{book.id} successfully deleted", status=200)    




