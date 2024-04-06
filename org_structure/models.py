from django.db import models

# Create your models here.

class Position_titles(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование должности")
    job_description_number = models.CharField(max_length=50, blank=True, null= False, verbose_name="Номер должностной инструкции")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Должности"
        ordering = ["name"]

class Staff(models.Model):
    sex_choices = ( ( "Ж", "Женский"), ("М", "Мужской") )
    name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    sex=models.CharField(max_length=1, choices=sex_choices, verbose_name="Пол")
    birthday = models.DateField(verbose_name="Дата рождения")
    service_number = models.PositiveIntegerField(verbose_name="Табельный номер")
    position_title = models.ForeignKey(to=Position_titles, on_delete=models.PROTECT, verbose_name="Должность") 
    org_admission_date = models.DateField(verbose_name="Дата приёма на работу в организацию")
    division_admission_date = models.DateField(verbose_name="Дата приёма на работу в подразделение")
    dismissal_date = models.DateField(blank=True, null=True, verbose_name="Дата увольнения из предприятия")
    transfer_date = models.DateField(blank=True, null=True, verbose_name="Дата перевода в другое подразделение (за контуром управления)")
    login = models.CharField(max_length=30, verbose_name="Логин")
    email_address = models.EmailField()
    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"
    class Meta:
        verbose_name_plural = "Сотрудники"
        ordering = ["surname"]

class Org_elements(models.Model):
    short_name = models.CharField(max_length=30, verbose_name="Код структурной единицы")
    full_name = models.CharField(max_length=200, verbose_name="Полное наименование структурной единицы")
    staff = models.ManyToManyField(to=Staff, verbose_name="Непосредственные подчинённые", blank= True, related_name="subordinate_staff")
    org_elements = models.ManyToManyField(to="org_structure.Org_elements", verbose_name="Подчинённые организационные элементы", blank=True, related_name="subordinate_org_elements")
    head = models.ForeignKey(to=Staff, on_delete=models.PROTECT, verbose_name="Начальник")
    def __str__(self):
        return f"{self.short_name}"
    class Meta:
        verbose_name_plural = "Структурные единицы"
        ordering = ["short_name"]
