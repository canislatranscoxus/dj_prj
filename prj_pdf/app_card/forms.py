
from datetime import date
from email.policy import default
from django                     import forms
from django.forms.widgets       import DateInput


class CardForm( forms.Form ):
    
    from_name    = forms.CharField( label = 'From', initial= 'Canis'  )
    to_name      = forms.CharField( label = 'To'  , initial = 'Bananits'    )
    message = forms.CharField( widget=forms.Textarea, label = 'Message', initial= 'Te quiero mucho' )
    
    img_url = forms.CharField( 
        widget=forms.Textarea,
        label = 'image link', 
        initial= 'https://a-z-animals.com/media/2019/11/Birman-close-up-768x401.jpg' )

    def clean(self):
        user_cleaned_data = super().clean()
