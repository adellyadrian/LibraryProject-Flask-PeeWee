from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField, IntegerField, ForeignKeyField, DateTimeField, BooleanField


db = SqliteDatabase('datab.db')


class BaseModel(Model):
    class Meta:
        database = db


class Books(BaseModel):
    image = CharField()
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100, null=False)
    year = IntegerField(null=False)
    author = CharField(max_length=100, null=False)
    content = CharField(max_length=100, null=False)
    isbn = IntegerField(null=False)
    status = CharField()
    available = BooleanField(default=True) 

    class Meta:
        table_name = 'books'


class Student(BaseModel):
    first_name = CharField(max_length=100, null=False)
    last_name = CharField(max_length=100, null=False)
    code = IntegerField(null=False)
    email = CharField(max_length=100, null=False)
    password = CharField(max_length=100, null=False)

    class Meta:
        table_name = 'students'


class BorrowedBooks(BaseModel):
    student = ForeignKeyField(Student, backref='borrowed_books')
    book = ForeignKeyField(Books, backref='borrowed_by_students')
    borrow_date = DateTimeField()

    class Meta:
        table_name = 'borrowed_books'
        

def create_tables():
    with db:
        db.create_tables([Books, Student, BorrowedBooks])
        
