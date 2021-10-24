from django.urls                import path
from .                          import views


app_name = 'app_01'

urlpatterns = [
    path( ''                  , views.TakePetView.as_view(), name = 'take_pet' ),    
    path( 'take_pet/'         , views.TakePetView.as_view(), name = 'take_pet' ),
    path( 'my_pet/<slug:pet>/', views.MyPetView.as_view()  , name = 'my_pet'   ),


]