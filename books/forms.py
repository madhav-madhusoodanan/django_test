from django import forms
from .models import request_detail


class RequestPeriodForm(forms.ModelForm):
    class Meta:
        model = request_detail
        fields = ['duration']

