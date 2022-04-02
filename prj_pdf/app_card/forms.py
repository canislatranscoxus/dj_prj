
from datetime import date
from email.policy import default
from django                     import forms
from django.forms.widgets       import DateInput


class CardForm( forms.Form ):
    
    _from    = forms.CharField( label = 'From', initial= 'Eagle Wings'  )
    _to      = forms.CharField( label = 'To'  , initial = 'My family'    )
    _message = forms.CharField( widget=forms.Textarea, label = 'Message', initial= 'Get up & Fight for your dreams!' )
    
    _img_url = forms.CharField( 
        widget=forms.Textarea,
        label = 'image link', 
        initial= 'https://a-z-animals.com/media/2019/11/Eagle-header.jpg' )

    def clean(self):
        user_cleaned_data = super().clean()
