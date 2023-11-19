from django.db import models
from django import forms

CHOICES = [
    ('еда', 'Еда'),
    ('транспорт', 'Транспорт'),
    ('шоппинг', 'Шоппинг'),
    ('здоровье', 'Здоровье'),
    ('счета', 'Счета'),
    ('развлечения', 'Развлечения'),
    ('транзакции', 'Транзакции'),

]


class Person(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=250)


class Income(models.Model):
    title_income = models.CharField(max_length=250)
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES, )
    income_num = models.DecimalField(max_digits=50, decimal_places=2)
    date = models.DateTimeField()


class Expenses(models.Model):
    title_expenses = models.CharField(max_length=250)
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES, )
    expenses_num = models.DecimalField(max_digits=50, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.title_expenses

