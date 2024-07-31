from django import forms
from . import models

class UploadFileForm(forms.ModelForm):
    #text = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={}))
   # file = forms.FileField(label='', required=False, widget=forms.ClearableFileInput(attrs={'value': 'choose a file', 'class': 'file-input', 'name': 'ssss'}))

    class Meta:
        model = models.UserPost
        fields = ['text', 'file']
        widgets = {
            'text': forms.Textarea(attrs = {}),
            'file': forms.FileInput(attrs={'value': 'choose a file', 'class': 'file-input', 'name': 'ssss', 'id': 'file_input_field'})
        }