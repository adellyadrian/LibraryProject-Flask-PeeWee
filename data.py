from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField, IntegerField, AutoField


db = SqliteDatabase('datab.db')


class BaseModel(Model):
    class Meta:
        database = db


class Books(BaseModel):
    image = CharField(null=False)
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100, null=False)
    year = IntegerField(null=False)
    author = CharField(max_length=100, null=False)
    content = CharField(max_length=100, null=False)
    isbn = IntegerField(null=False)

    class Meta:
        table_name = 'books'


class BookCopy(BaseModel):
    id = AutoField(primary_key=True, null=False)
    b_name = CharField(max_length=100, null=False)
    b_year = IntegerField(null=False)
    b_author = CharField(max_length=100, null=False)
    b_content = CharField(max_length=100, null=False)
    b_isbn = IntegerField(null=False)
    url = CharField(null=False)

    class Meta:
        table_name = 'book_copy'


class Student(BaseModel):
    first_name = CharField(max_length=100, null=False)
    last_name = CharField(max_length=100, null=False)
    code = IntegerField(null=False)
    email = CharField(max_length=100, null=False)
    password = CharField(max_length=100, null=False)

    class Meta:
        table_name = 'students'


def create_tables():
    with db:
        db.create_tables([Books, BookCopy, Student])
