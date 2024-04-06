from django.db import models

# Create your models here.

class Statuses(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование статуса")
    priority = models.PositiveIntegerField(verbose_name="Приоритет статуса")
    description = models.CharField(max_length=300, verbose_name="Описание статуса")
    sign_of_relevance = models.BooleanField(verbose_name="Признак статуса незавершенных задач")
    sign_of_decreased_attention = models.BooleanField(verbose_name="Признак статуса задач, требующих пониженного внимания")
    sign_for_information = models.BooleanField(verbose_name="Признак статуса задач, носящих информационный и(или) ознакомительный характер")

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ["priority"]


