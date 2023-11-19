from .models import Expenses
from django.forms import ModelForm


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['title_expenses', 'expenses_num', 'date']
