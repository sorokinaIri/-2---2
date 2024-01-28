from pydantic import BaseModel, model_validator

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


# TODO написать класс Book

class Book(BaseModel):
    """ Класс, описывающий объект Книга, который будет использоваться для нахождения нужной вам книги """
    name: str
    id: int
    pages: int  # говорит о том, что атрибут pages для всех экземпляров должен быть типа int

    # Инициализация экземпляра класса

    @model_validator(mode='before')
    def check(cls, values):
        if type(values['id'])   is not int or type(values['pages'])  is not int or type(values['name'])  is not str:
            raise TypeError("Некорректный формат данных")
        if values["pages"] <= 0 or values["id"] <= 0:
            raise ValueError("pages и id должны быть положительным числом")
        return values

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    result = []
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(f"{book}")  # проверяем метод __str__
    print(list_books)


