from django.db import models
from datetime import timedelta
from django.utils import timezone

# This model stores all book details
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)

    # Author name
    author = models.CharField(max_length=200)

    # To check whether book is available or issued
    is_available = models.BooleanField(default=True)

    # This function defines how object is shown in admin or shell
    def __str__(self):
        return self.title


# This model stores issue/borrow details of books
class Issue(models.Model):
    # Name of the user who borrowed the book
    user_name = models.CharField(max_length=100)

    # ForeignKey creates relationship with Book model
    # If book is deleted, related issue records will also be deleted
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Automatically stores the date when book is issued
    issued_date = models.DateTimeField(auto_now_add=True)

    # Due date to return the book (can be empty initially)
    due_date = models.DateTimeField(null=True, blank=True)

    # Actual return date (empty until book is returned)
    return_date = models.DateTimeField(null=True, blank=True)

    # Status to check whether book is returned or not
    returned = models.BooleanField(default=False)

    # Display format of Issue object
    def __str__(self):
        return f"{self.user_name} - {self.book.title}"
    

    # Custom function to calculate late days
    def late_days(self):
        # Check if due_date exists
        if self.due_date:

            # If book is returned, use return_date
            if self.returned and self.return_date:
                end_date = self.return_date
            else:
                # If not returned, use current time
                end_date = timezone.now()

            # Calculate difference between end_date and due_date
            diff = (end_date.date() - self.due_date.date()).days

            # If negative, return 0 (no late)
            return max(0, diff)

        # If no due_date, return 0
        return 0