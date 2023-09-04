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


@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        author = request.form['author']
        content = request.form['content']
        isbn = request.form['isbn']
        image = request.form['image']

        if not title:
            flash('Title is required!')
        elif not year:
            flash('Year is required!')
        elif not author:
            flash('Author is required!')
        elif not content:
            flash('Content is required!')
        elif not isbn:
            flash('ISBN is required!')
        elif not image:
            flash('Image is required!')
    return render_template('borrow_book.html')


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


@app.route('/book-registration', methods=['GET', 'POST'])
def book_reg():
    if request.method == 'POST':
        title = request.form['b_name']
        year = request.form['b_year']
        author = request.form['b_author']
        content = request.form['b_content']
        isbn = request.form['b_isbn']
        image = request.form['url']

        if not title:
            flash('Title is required!')
        elif not year:
            flash('Year is required!')
        elif not author:
            flash('Author is required!')
        elif not content:
            flash('Content is required!')
        elif not isbn:
            flash('ISBN is required!')
        elif not image:
            flash('Image is required!')
        else:
            Books.create(b_name=title, b_year=year, b_author=author, b_content=content, b_isbn=isbn, url=image)
            return redirect(url_for('all_books'))
    return render_template('book-reg.html')


@app.route('/student_info')
def student_info():
    if 'user_id' in session:
        user_id = session['user_id']
        user = Student.get(Student.id == user_id)
        if user:
            return render_template('our-students.html', user=user)
        else:
            flash('User not found.', 'danger')
            return redirect(url_for('main'))
    else:
        flash('Please log in to view this page.', 'info')
        return redirect(url_for('login'))
    
    
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


@app.route('/borrow/<int:book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    if request.method == 'POST':
        flash('Book borrowed successfully.', 'success')
        return redirect(url_for('display'))
    else:
        flash('Please log in to borrow books.', 'info')
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
        db.create_tables([Books, Student])


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=80)
