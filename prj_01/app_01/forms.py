from django   import forms


class TakePetForm( forms.Form ):
    PET_CHOICES = [ (1, 'cat'), (2, 'dog'), (3, 'fish') ]
    pet = forms.ChoiceField( widget = forms.RadioSelect, choices = PET_CHOICES )


class DynamicSportForm( forms.Form ):
    
    #pet = forms.ChoiceField( widget = forms.RadioSelect, choices = PET_CHOICES )
    sport_id = forms.ChoiceField( widget = forms.RadioSelect, label = '' )

    def clean(self):
        user_cleaned_data = super().clean()

    def __init__(self, *args,**kwargs):
        try:
            choices = None
            if 'choices' in kwargs:
                choices = kwargs.pop( 'choices' )

            selected_id = None
            if 'selected_id' in kwargs:
                selected_id = kwargs.pop( 'selected_id' )
                
            super( DynamicSportForm, self ).__init__( *args, **kwargs )

            if choices != None:
                self.fields[ 'sport_id' ].choices    = choices

                self.fields[ 'sport_id' ].initial    = choices[ 0 ][ 0 ]

                print( self.fields[ 'sport_id' ].initial )
                print( '...' )

                #if selected_id == None:
                #    # select the first option by default
                #    self.fields[ 'sport_id' ].initial    = choices[ 0 ][ 0 ]
                #else:
                #    self.fields[ 'sport_id' ].initial    = selected_id


        except Exception as e:
            print( 'DynamicSportForm.__init__(), error: {}'.format( e ) )
            raise

