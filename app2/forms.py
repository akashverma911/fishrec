from django import forms
from app1.models import Fish
# Create your views here.
class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = "__all__"
