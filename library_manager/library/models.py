from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_of_membership = models.DateTimeField(
        auto_now=False, null=True)
    age = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(
        default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE = (
            ('Science Fiction', 'Science Fiction'),
            ('Thriller', 'Thriller'),
            ('Biography', 'Biography'),
            ('Fable', 'Fable'),
            ('Literature', 'Literature'),
            ('History', 'History'),
    )

    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)

    genre = models.CharField(max_length=200, null=True, choices=GENRE)
    ageGroup = models.CharField(max_length=200, null=True)
    bookCopies = models.CharField(max_length=200, null=True)

    date_published = models.DateTimeField(
        auto_now=False, max_length=200, null=True)
    date_of_keeping = models.DateTimeField(
        auto_now=False, max_length=200, null=True)

    def __str__(self):
        return self.name


class BookOrder(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)

    order_date = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.book.name


class BookRent(models.Model):
    STATUS = (
        ('Returned', 'Returned'),
        ('Pending', 'Pending'),
        ('Not Returned', 'Not Returned'),
    )

    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)

    rental_date = models.DateTimeField()
    #return_date = models.DateTimeField(null=True, blank=True)

    #fine = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.book.name


class BookPDF(models.Model):
    name = models.CharField(max_length=200, null=True)
    pdf = models.FileField()

    def __str__(self):
        return self.name
