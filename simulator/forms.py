from django.forms import ModelForm
from .models import StockForm

class stockForm(ModelForm):
    class Meta:
        model = StockForm
        fields = '__all__'