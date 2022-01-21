import random
from django.shortcuts           import render, redirect, get_object_or_404
from django.urls                import reverse, reverse_lazy
from django.views               import View

from .forms                     import *

# Create your views here.


sports = [ 
    ( 'tkd', 'Tae Kwon Do'  ), 
    ( 'bjj', 'Jiu Jitsu'    ), 
    ( '8mt', 'Muay Thai'    ),
    ( '8x8', 'Chess'        ),
    ( 'wre', 'Wrestling'    ),
    ( 'jud', 'Judo'         ),
    ( 'box', 'Boxing'       ),
    ( 'nin', 'Ninjitsu'     ),
    ( 'jkd', 'Jeet Kune Do' ),
    ( 'sk8', 'Skateboarding'),
    ( 'gym', 'Gymnastics'   ),
    ( 'sur', 'Surfing'      ),
    ( 'wis', 'Wind Surfing' ),
]

def home( request ):
    return render(request, 'home.html' )


class TakePetView( View ):
    context_object_name = 'take_pet'
    template_name = 'take_pet.html'

    def get(self, request, *args, **kwargs):
        form = TakePetForm()
        my_dic = { 'form' : form }
        return render( request, self.template_name, my_dic  )     

    def post(self, request, *args, **kwargs):
        #address_id          = kwargs.get( 'pk', None )
        my_dic = {}
        form = TakePetForm( request.POST )
        if form.is_valid():
            
            # get the seleceted option
            value = int( form.cleaned_data[ 'pet' ] )
            label = ''
            for _value, _label in form.PET_CHOICES: 
                if value == _value:
                    label = _label
                    break

            print( 'option value: {}'.format( value ) )
            print( 'option label: {}'.format( label ) )
            pet = label

        my_url = reverse( 'app_01:my_pet', args=( pet, )   ) 
        print( 'my_url: {}'.format( my_url ) )
        return redirect( reverse( 'app_01:my_pet', args=( pet, )   ) )

class MyPetView( View ):
    def get(self, request, *args, **kwargs):
        pet = kwargs.get( 'pet', None )
        my_dic = {
            'pet' : pet
        }
        return render( request, 'my_pet.html', my_dic  )     

class SportsView( View ):
    context_object_name = 'sports'
    template_name       = 'sports.html'
    success_url         = 'app_01:my_sport'
    form_class          = forms.Form


    def get(self, request, *args, **kwargs):
        my_dic = {  }
        return render( request, self.template_name, my_dic  )     

    def post(self, request, *args, **kwargs):
        choices = []
        form   = self.form_class( request.POST )
        
        if form.is_valid():
            #value = form.cleaned_data[ 'sports' ] 
            s = form.data[ 'sports' ].split( ',' ) 
            if len( s ) % 2 == 1:
                s.append( 'All Sports' )

            for i in range( len( s ) -1 ):
                t = ( s[ i ].strip(), s[ i + 1].strip() )
                choices.append( t )

            print( 'choices: {}'.format( choices ) )

        return redirect( reverse( 'app_01:my_sport'  ) )



class MySportView( View ):
    # tkd, Tae Kwon Do, bjj, Jiu Jitsu, 8mt, Muay Thai
    context_object_name = 'my_sport'
    template_name       = 'my_sport.html'

    success_url         = 'app_01:sport_club'
    form_class          = DynamicSportForm



    def get(self, request, *args, **kwargs):
        
        # generate dynamically a list of choices and pass it to the form.
        choices = random.sample( sports, 3 )

        form    = DynamicSportForm( request.POST, choices = choices, initial={ 'sport_id' : choices[0][0] }  )

        my_dic  = { 'form' : form }
        return render( request, self.template_name, my_dic  )     


    def post( self, request ):

        form   = DynamicSportForm( request.POST )
        
        sport_id = None
        sport = None
        if form.is_valid():
            sport_id = form.cleaned_data[ 'sport_id' ] 
        else:
            sport_id = form.data[ 'sport_id' ] 

        for i in sports:
            if i[ 0 ] == sport_id:
                sport = i[ 1 ]
                print( i[ 1 ] )


        return redirect( reverse( self.success_url, args=( sport, ) )  )



class SportClubView( View ):
    context_object_name = 'sport_club'
    template_name       = 'sport_club.html'


    def get(self, request, *args, **kwargs):

        sport = kwargs.get( 'sport', None )
        my_dic  = { 'sport' : sport }
        return render( request, self.template_name, my_dic  )     

