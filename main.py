from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    pages: int

books = []
book_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the CloudStation FastAPI Books API!"}

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    global book_id_counter
    book.id = book_id_counter
    book_id_counter += 1
    books.append(book)
    return book

@app.get("/books/", response_model=List[Book])
def read_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            updated_book.id = book_id
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
