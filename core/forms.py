from django import forms
from .models import Areas

# class AreasForm(forms.ModelForm):
#     class Meta:
#         model = Areas
#         fields = ['name']

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields["name"].widget.attrs.update({"class": "form-control px-4"})