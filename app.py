from flask import Flask, render_template, request, url_for, flash, redirect, abort, session
from data import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'am375'
app.config['DATABASE'] = 'datab.db'


def get_db_connection():
    db.connect()
    return db


def get_books(book_id):
    try:
        book = Books.get_by_id(book_id)
        return book
    except Books.DoesNotExist:
        abort(404)


@app.route('/')
def main():
    return render_template('home-page.html')


@app.route('/about')
def about():
    return render_template('about-page.html')


@app.route('/books')
def our_books():
    return render_template('our-books.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        code = request.form['code']
        email = request.form['email']
        password = request.form['password']

        new_contact = Student.create(
            first_name=first_name,
            last_name=last_name,
            code=code,
            email=email,
            password=password
        )
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('sign-up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['first_name']
        password = request.form['password']
        try:
            user = Student.get(Student.first_name == first_name)
            if user.password == password:
                session['user_id'] = user.id
                session['first_name'] = user.first_name
                return redirect(url_for('display'))
            else:
                flash('Invalid username or password.', 'error')
        except Student.DoesNotExist:
            flash('Invalid username or password.', 'error')
    return render_template('log-in.html')


@app.route('/new_book', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        author = request.form['author']
        content = request.form['content']
        isbn = request.form['isbn']
        image = request.form['image']
        status = request.form['status']
        new_book = Books.create(
            image=image,
            title=title,
            year=year,
            author=author,
            content=content,
            isbn=isbn,
            status=status
        )
        flash('Book added successfully!', 'success')
        return redirect(url_for('all_books'))
    return render_template('book-reg.html')
    
    
@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        name = request.form.get('title', '')
        try:
            book = Books.get(Books.title == name)
            return render_template('search_books.html', bs=[book])
        except Books.DoesNotExist:
            flash('No matching books found.', 'sorry')
            return redirect(url_for('search_books'))
    return render_template('home-page.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


@app.route('/all_books')
def all_books():
    books = Books.select()
    return render_template('our-books.html', books=books)


@app.route('/borrow/<int:book_id>', methods=['GET','POST'])
def borrow_book(book_id):
    if 'user_id' in session:
        user_id = session['user_id']
        user = Student.get(Student.id == user_id)
        book = Books.get(Books.id == book_id)
        if book.available:   
            book.borrowed_user = user.id
            book.available = False
            book.save()
            flash('Book borrowed successfully.')
        else:
            flash('Book is not available for borrowing.', 'warning')
        return render_template('borrow_book.html', user=user, book=book, bs=[book], book_id=book_id)
    else:
        flash('Please log in to borrow books.', 'info')
        return redirect(url_for('login'))                                                                                                                                                                                                                                           


@app.route('/student_info')
def student_info():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            user = Student.get(Student.id == user_id)
            if user:
                borrowed_books = BorrowedBooks.select().where(BorrowedBooks.student == user)
                return render_template('our-students.html', user=user, bb=[borrowed_books])
            else:
                flash('User not found.', 'danger')
                return redirect(url_for('main'))
        except Student.DoesNotExist:
            flash('User not found in the database.', 'danger')
            return redirect(url_for('main'))
    else:
        flash('Please log in to view this page.', 'info')
        return redirect(url_for('login'))


@app.route('/display')
def display():
    if 'user_id' in session:
        user_id = session['user_id']
        user = Student.get(Student.id == user_id)
        first_name = session.get('first_name')
        if user:
            borrowed_books = []
            return render_template('our-books.html', user=user, first_name=first_name, borrowed_books=borrowed_books)
        else:
            flash('User not found.', 'danger')
            return redirect(url_for('main'))
    else:
        flash('Please log in to view this page.', 'info')
        return redirect(url_for('login'))



def create_tables():
    with db:
        db.create_tables([Books, Student, BorrowedBooks])


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=80)
