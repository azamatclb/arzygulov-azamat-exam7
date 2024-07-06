from django.db import models

# Create your models here.

status_choices = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class GuestBook(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(null=False, blank=False, verbose_name='Эмейл')
    text = models.TextField(null=False, blank=False, verbose_name='Текст записи')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=10, choices=status_choices, default='active', verbose_name='Статус')

    def __str__(self):
        return f"{self.id} {self.author} {self.email} {self.date_added} {self.date_updated}"

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'Запись в гостевой книге'
        verbose_name_plural = 'Записи в гостевой книге'
        ordering = ['-date_added']
