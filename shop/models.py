from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Текст', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']