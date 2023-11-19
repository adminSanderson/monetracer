from django.contrib import admin
from .models import Person, Expenses, Income

admin.site.register(Person)
admin.site.register(Expenses)
admin.site.register(Income)