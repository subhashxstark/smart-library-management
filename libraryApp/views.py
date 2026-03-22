from django.shortcuts import render, redirect
from .models import Book, Issue
from django.utils import timezone
from datetime import timedelta

# View to display all books on homepage
def book_list(request):
    # Fetch all book records from database
    books = Book.objects.all()

    # Send books data to template
    return render(request, 'book_list.html', {'books': books})


# View to add a new book
def add_book(request):
    # Check if form is submitted
    if request.method == "POST":
        # Get data from form
        title = request.POST['title']
        author = request.POST['author']

        # Create new book record
        Book.objects.create(title=title, author=author)

        # Redirect to homepage after adding
        return redirect('/')

    # If GET request, show add book page
    return render(request, 'add_book.html')


# View to issue a book
def issue_book(request, book_id):
    # Get book by ID
    book = Book.objects.get(id=book_id)

    # If form submitted
    if request.method == "POST":
        # Get user name from form
        user_name = request.POST['user_name']

        # Check if book is available
        if book.is_available:
            # Create issue record with due date (1 day from now)
            Issue.objects.create(
                user_name=user_name,
                book=book,
                due_date=timezone.now() + timedelta(days=1)  # due date set here
            )

            # Mark book as not available
            book.is_available = False
            book.save()

        # Redirect to homepage
        return redirect('/')

    # Show issue page with book details
    return render(request, 'issue_book.html', {'book': book})


# View to show all issued books (not returned)
def issued_books(request):
    # Filter only books that are not returned
    issues = Issue.objects.filter(returned=False)

    # Send data to template
    return render(request, 'issued_books.html', {'issues': issues})


# View to return a book
def return_book(request, issue_id):
    # Get issue record
    issue = Issue.objects.get(id=issue_id)

    # Mark as returned
    issue.returned = True

    # Store return date
    issue.return_date = timezone.now()

    # Make book available again
    issue.book.is_available = True
    issue.book.save()

    # Save issue changes
    issue.save()

    # Redirect to issued books page
    return redirect('/issued-books/')


# View to edit book details
def edit_book(request, book_id):
    # Get book by ID
    book = Book.objects.get(id=book_id)

    # If form submitted
    if request.method == "POST":
        # Update fields from form
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')

        # Save updated data
        book.save()

        # Redirect to homepage
        return redirect('/')

    # Show edit form with existing data
    return render(request, 'edit_book.html', {'book': book})


# View to delete a book
def delete_book(request, book_id):
    # Get book by ID
    book = Book.objects.get(id=book_id)

    # Delete book record
    book.delete()

    # Redirect to homepage
    return redirect('/')