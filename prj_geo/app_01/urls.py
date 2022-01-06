from django.urls                import path
from .                          import views


app_name = 'app_01'

urlpatterns = [

    path( ''             , views.ConfirmGeoView.as_view()  , name = 'home'   ),
    path( 'confirm_geo/'             , views.ConfirmGeoView.as_view()  , name = 'confirm_geo'   ),
    path( 'show_location/<lat>/<lon>', views.ShowLocationView.as_view(), name = 'show_location' ),

]