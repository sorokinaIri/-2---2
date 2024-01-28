from pydantic import BaseModel, field_validator, model_validator

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):  # Book унаследован от BaseModel

    name: str
    id: int
    pages: int  # говорит о том, что атрибут pages для всех экземпляров должен быть типа int

    @field_validator('name')
    def name_type_str(cls, name):
        if type(name) is not str:
            raise TypeError(" Введен некорректный формат данных в name ")
        return name

    @model_validator(mode='before')
    def id_and_pages_values_and_types(cls, values):
        if type(values['id']) is not int or type(values['pages']) is not int:
            raise TypeError(" Введен некорректный формат данных в id или pages ")
        if values["pages"] <= 0 or values["id"] <= 0:
            raise ValueError("pages и id должны быть положительным числом")
        return values


# TODO написать класс Book

class Library(BaseModel):  # Library унаследован от BaseModel

    books: list = []  # Список книг, изначально пустой

    @field_validator('books')
    def books_values_and_types(cls, books):
        if type(books) is not list:
            raise TypeError(" Введен некорректный формат данных в books ")
        return books

    def get_next_book_id(self):

        if len(self.books) == 0:
            return 1
        else:
            id_res = self.books[-1].get("id")
            return id_res + 1

    def get_index_by_book_id(self, id):

        for i, val in enumerate(self.books):
            if val["id"] == id:
                return i
        raise ValueError("Книга с запрашиваемым id не существует")


# TODO написать класс Library

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    library_with_books = Library(books=BOOKS_DATABASE)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1