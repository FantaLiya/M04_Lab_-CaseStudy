
from flask import Flask
app=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQlALchemy(app)

class Book(db.Model):
    id=db.column(db.Integer,primary_key=True)
    name=db.column(db.String(80),unique=True,nullable=False)
    author=db.column(db.String(160))
    publisher=db.column(db.String(120))

    def __repr__(self):
        return f"{self.name}_{self.author}_{self.publisher}"


@app.route('/')
def index():
    return 'Hello!'

    @app.route('/books')
    def get_books():
        books=Books.query.all()

        output=[]
        for books in books:
            books_data={'name':books.name,'author':authot.name,'publisher':organization.name}

            output.append(book_data)

        return{"books":output} 
    @app.route('/books/<id>')
    def get_book(id):
        book=Book.query.get_or_404(id)
        return {"name":book.name,"author":author.name,"publisher":
        publisher.name}

    @app.route('/books',methods=['POST'])
    def add_book():
        book=Book(name=request.json['name'],author=request.json['author'])
        db.session.add(book)
        db.session.commint()
        return {'id':book.id}
    @app.route('/books/<id>',methods=['Delete'])
    def delete_book(id):
         book -Book.query.get(id)
         if book is None:
                return{"error":"not found"}
         db.session.delete(book)
         db.session.commit()
         return{"message":"Yeet!@"}
