from django import forms

class UploadFileForm(forms.Form):
    file_form = forms.FileField(label='', required=False, widget=forms.ClearableFileInput(attrs={'value': 'choose a file', 'class': 'file-input', 'name': 'ssss'}))
