from django.db import models
from django.urls import reverse
# from django.conf import settings
# from django.utils.translation import ugettext_lazy as _ # TODO: not used temporarily.

'''
References:
    - https://github.com/vitorfs/bootcamp
'''


class BookQuerySet(models.QuerySet):
    def get_published(self):
        return self.filter(status='P')

    def get_drafts(self):
        return self.filter(status='D')

    # TODO: we should use 'annotate' or 'aggregate' to improve the efficiency for search.
    def get_num_of_book_pages(self):
        return self.aggregate(models.Sum('pages'))

    def get_num_of_published(self):
        return len(self.get_published())

    def get_num_of_drafts(self):
        return len(self.get_drafts())


class Book(models.Model):
    DRAFT = "D" # draft data,
    PUBLISHED = "P" # published data.
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    name = models.CharField(max_length=20, unique=True, null=False)
    pages = models.IntegerField(default=0, null=False)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    # TODO: need to learn how to use them.
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     null=True,
    #     related_name='book',
    #     on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = BookQuerySet.as_manager()

    class Meta:
        db_table = 'cbv_book'
        app_label = 'cbv'
        managed = True
        ordering = ['created_at', 'name', 'status']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
