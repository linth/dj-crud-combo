from django.test import TestCase
from .models import Book


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name='machine learning',
                            pages=100,
                            current_price=1000,
                            last_price=1000,
                            min_price=500,)

        Book.objects.create(name='TensorFlow',
                            pages=200,
                            current_price=900,
                            last_price=900,
                            min_price=1000,)

    def test_max_price(self):
        """ create new object first for testing. """
        m = Book.objects.get(name='machine learning')
        t = Book.objects.get(name='TensorFlow')

        m.set_max_price()
        assert m.max_price == m.current_price

        t.set_max_price()
        assert t.max_price == t.current_price

    def test_min_price(self):
        """ create new object for testing. """
        m = Book.objects.get(name='machine learning')
        t = Book.objects.get(name='TensorFlow')

        m.set_min_price()
        assert m.min_price == 500
        t.set_min_price()
        assert t.min_price == 900

    def test_status(self):
        m = Book.objects.get(name='machine learning')
        t = Book.objects.get(name='TensorFlow')

        assert m.status == 'DRAFT'
        assert t.status == 'DRAFT'
