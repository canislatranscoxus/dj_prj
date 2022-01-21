from django.urls                import path
from .                          import views


app_name = 'app_01'

urlpatterns = [
    path( ''                  , views.home , name = 'home' ),    
    path( 'take_pet/'         , views.TakePetView.as_view(), name = 'take_pet' ),
    path( 'my_pet/<slug:pet>/', views.MyPetView.as_view()  , name = 'my_pet'   ),

    path( 'sports/'  , views.SportsView.as_view() , name = 'sports'   ),
    path( 'my_sport/', views.MySportView.as_view(), name = 'my_sport' ),
    path( 'sport_club/<slug:sport>', views.SportClubView.as_view(), name = 'sport_club' ),

]