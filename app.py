from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date

DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/bookstore"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    published_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}')>"

def add_book(session, title, author, genre, price, published_date):
    new_book = Book(title=title, author=author, genre=genre, price=price, published_date=published_date)
    session.add(new_book)
    session.commit()
    print(f"Added book: {new_book}")

def list_books(session):
    books = session.query(Book).all()
    for book in books:
        print(book)

def update_book(session, book_id, **kwargs):
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        print("Book not found.")
        return
    for key, value in kwargs.items():
        setattr(book, key, value)
    session.commit()
    print(f"Updated book: {book}")

def delete_book(session, book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        print("Book not found.")
        return
    session.delete(book)
    session.commit()
    print(f"Deleted book with ID: {book_id}")

def search_books(session, keyword):
    results = session.query(Book).filter(
        (Book.title.ilike(f"%{keyword}%")) |
        (Book.author.ilike(f"%{keyword}%")) |
        (Book.genre.ilike(f"%{keyword}%"))
    ).all()
    if not results:
        print("No books found.")
    for book in results:
        print(book)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    add_book(session, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.99, date(1925, 4, 10))

    print("\nAll books:")
    list_books(session)

    update_book(session, 1, price=12.99)

    print("\nSearch results for 'Fitzgerald':")
    search_books(session, "Fitzgerald")

    delete_book(session, 1)

    print("\nBooks after deletion:")
    list_books(session)

    session.close()
