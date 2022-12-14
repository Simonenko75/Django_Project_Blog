from django.db import models


class Post(models.Model):
    title = models.CharField('Назва поста', max_length=50)
    author = models.CharField('Автор поста', max_length=50)
    text = models.TextField('Опис даного поста')
    published = models.CharField('Рік публікації', max_length=4, default='2022')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'