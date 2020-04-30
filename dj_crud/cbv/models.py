from django.db import models
from django.urls import reverse
from django.utils import timezone
# from django.conf import settings
# from django.utils.translation import ugettext_lazy as _ # TODO: not used temporarily.
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager
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
    # DRAFT = "D" # draft data,
    # PUBLISHED = "P" # published data.
    STATUS = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    )

    name = models.CharField(max_length=20, unique=True, null=False)
    pages = models.IntegerField(default=0, null=False)
    status = models.CharField(max_length=10, choices=STATUS, default='DRAFT')
    # TODO: need to learn how to use them.
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     null=True,
    #     related_name='book',
    #     on_delete=models.SET_NULL)
    current_price = models.FloatField(null=True)
    last_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True, default=0)
    min_price = models.FloatField(null=True, default=0)
    description = MarkdownxField()
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True) # timestamp
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = BookQuerySet.as_manager()

    class Meta:
        db_table = 'cbv_book'
        app_label = 'cbv'
        managed = True
        ordering = ['created_at', 'name', 'status']

    def __str__(self):
        return self.name

    def get_markdown(self):
        return markdownify(self.description)

    def to_dict_json(self):
        return {'id': self.id,
                'name': self.name,
                'pages': self.pages,
                'status': self.STATUS,
                'price': self.current_price,
                'created_at': self.created_at,
                'updated_at': self.updated_at,}

    # def get_absolute_url(self):
    #     return reverse('books_cbv:book_edit', kwargs={'pk': self.pk})

    # TODO: to understand the save function.
    # def save(self):
    #     super().save(self)
    #     # print('args=>', args)
    #     # print('kwargs=>', kwargs)

    # TODO: how to use the function: get_absolute_url()
