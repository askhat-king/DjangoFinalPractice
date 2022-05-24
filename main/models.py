from django.db import models

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    price = models.IntegerField()
    description = models.CharField(max_length=200, verbose_name='Description')
    created_at = models.DateTimeField(verbose_name='Created at')

    class Meta:
        ordering = ['name']
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    TYPE_CHOICE = (
        (1, "Bullet"),
        (2, "Food"),
        (3, "Travel"),
        (4, "Sport")
    )
    type = models.IntegerField(choices=TYPE_CHOICE, verbose_name="Type")
    publisher = models.CharField(max_length=100, verbose_name='Publisher')

