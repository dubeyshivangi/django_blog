from django	import forms
from .models	import	Comment, Contactus

class CommentForm(forms.ModelForm):
    class Meta:
        model	=	Comment
        fields	=	('name',	'email', 'body')

class ContactusForm(forms.ModelForm):
    class Meta:
        model	=	Contactus
        fields	=	('name',	'email', 'message')

class EmailPostForm(forms.Form):
    name	=	forms.CharField(max_length=25)
    email	=	forms.EmailField()
    to	=	forms.EmailField()
    comments	=	forms.CharField(required=False,widget=forms.Textarea)
