from django import forms
from . import models
from django.core.validators import FileExtensionValidator
 

    
class PostCreateForm(forms.ModelForm):
    #text = forms.CharField(label='')
    #file = forms.FileField(label='')
    #author = forms.TextInput()
    class Meta:
        model = models.UserPost
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs = {},),
            'image': forms.ClearableFileInput(attrs={'value': 'choose a file', 'class': 'image-input', 'id': 'image_input_field'}),
            'video': forms.ClearableFileInput(attrs={'value': 'choose a file', 'class': 'video-input', 'id': 'video_input_field'}),
            'file': forms.ClearableFileInput(attrs={'value': 'choose a file', 'class': 'file-input', 'id': 'file_input_field'}),
        }
        labels = {
            'text': '',
            'image': '',
            'video': '',
            'file': '',
        }
        validators = {
            'video': [FileExtensionValidator(allowed_extensions=['mp4', 'gif', 'avi', 'wmv', 'mov',])]
        }
