from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class BotSetting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PersonStatus(models.Model):
    status = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status

class Person(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    roles = models.ManyToManyField(Role, blank=True)
    person_status = models.ForeignKey(PersonStatus, on_delete=models.SET_NULL, null=True, blank=True)
    additional_info = models.TextField(blank=True)
    personal_number = models.CharField(max_length=11, unique=True, blank=True, null=True)  # Новое поле для личного номера
    iban = models.CharField(max_length=34, unique=True, blank=True, null=True)  # Новое поле для IBAN

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()  # Время необходимое для проведения сервиса
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)  # Размер оплаты за час

    def __str__(self):
        return self.name

class Visit(models.Model):
    client = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='visits_as_client')
    specialist = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='visits_as_specialist')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Ссылка на модель Service
    visit_time = models.DateTimeField()
    prepayment_made = models.BooleanField(default=False)  # Добавлено поле для предоплаты

    def __str__(self):
        prepayment_status = "с предоплатой" if self.prepayment_made else "без предоплаты"
        return f"{self.client.name} - {self.service.name} - {self.visit_time.strftime('%Y-%m-%d %H:%M')}"

class CompletedService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='completed_services_as_client')
    specialist = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='completed_services_as_specialist')
    duration = models.DurationField(default="00:30:00")  # Фактическое время проведения сервиса
    payment = models.DecimalField(max_digits=10, decimal_places=2)  # Фактический размер оплаты

    def __str__(self):
        return f"{self.service.name} - {self.client.name} - {self.payment}"

class WorkSchedule(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)  # Связь с моделью Person
    start_time = models.TimeField(default='09:00')  # Начало рабочего дня
    end_time = models.TimeField(default='18:00')  # Окончание рабочего дня
    break_start_time = models.TimeField(default='18:00')  # Время начала перерыва
    break_duration = models.DurationField(default='01:00:00')  # Продолжительность перерыва
    work_days = models.CharField(max_length=7, default="1111111", help_text="დღეების ორობითი წარმოდგენა (1 სამუშაო დღე, 0 დასვენების დღე)")

    def __str__(self):
        return f"{self.person.name} - Work Schedule"

