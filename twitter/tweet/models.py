from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.


class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=250)
    username = models.CharField(max_length=30, default='')

    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)

    # Define order in table.
    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return f"{self.username}:{self.content}"
