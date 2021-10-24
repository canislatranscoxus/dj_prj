from django   import forms


class TakePetForm( forms.Form ):

    PET_CHOICES = [ (1, 'cat'), (2, 'dog'), (3, 'fish') ]
    pet = forms.ChoiceField( widget = forms.RadioSelect, choices = PET_CHOICES )

    
