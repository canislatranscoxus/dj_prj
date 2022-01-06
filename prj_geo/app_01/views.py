from django                     import forms
from django.shortcuts           import render
from django.shortcuts           import redirect, get_object_or_404
from django.urls                import reverse, reverse_lazy
from django.views               import View
from django.views.generic       import ListView
from django.views.generic.edit  import CreateView, UpdateView, DeleteView

# Create your views here.



class ConfirmGeoView( View ):

    context_object_name = 'confirm_geo_location'
    template_name       = 'geo/confirm_geo.html'
    success_url         = 'app_01:show_location'
    form_class          = forms.Form

    def get(self, request, *args, **kwargs):

        
        return render( request, self.template_name )


    def post(self, request ):
        latitude  = 0
        longitude = 0
        form = self.form_class(request.POST)
        if form.is_valid():

            latlng = form.data[ 'txt_latlon' ]
            lat    = form.data[ 'txt_lat'    ]
            lon    = form.data[ 'txt_lon'    ]

            print( 'latlng : {}'.format( latlng ) )
            print( 'lat    : {}'.format( lat    ) )
            print( 'lon    : {}'.format( lon    ) )

        return redirect( reverse( self.success_url, args=( lat, lon, )  ) ) 


class ShowLocationView( View ):

    context_object_name = 'confirm_geo_location'
    template_name       = 'geo/show_location.html'


    def get(self, request, *args, **kwargs):

        my_dic = {
            'lat' : self.kwargs[ 'lat' ],
            'lon' : self.kwargs[ 'lon' ],
        }

        
        return render( request, self.template_name, my_dic )


