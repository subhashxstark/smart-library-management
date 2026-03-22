"""
URL configuration for smartLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraryApp import views  # importing all view functions from app

# URL patterns define which URL calls which view
urlpatterns = [

    # Admin panel (default Django feature)
    path('admin/', admin.site.urls),

    # Homepage → shows list of books
    path('', views.book_list, name='book_list'),

    # Page to add a new book
    path('add-book/', views.add_book, name='add_book'),

    # Issue a book (book_id is passed from URL)
    path('issue/<int:book_id>/', views.issue_book),

    # Return a book (issue_id is passed from URL)
    path('return/<int:issue_id>/', views.return_book),

    # Show all issued (not returned) books
    path('issued-books/', views.issued_books),

    # Edit book details (update title/author)
    path('edit-book/<int:book_id>/', views.edit_book),

    # Delete a book from database
    path('delete-book/<int:book_id>/', views.delete_book),
]