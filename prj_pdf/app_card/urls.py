from django.urls                import path
from .                          import views


app_name = 'app_card'

urlpatterns = [
    path( ''        , views.EditView.as_view(), name = 'home'    ),
    path( 'edit/'   , views.EditView.as_view(), name = 'edit'    ),    
    path( 'preview/', views.EditView.as_view(), name = 'preview' ),
    path( 'pdf/'    , views.EditView.as_view(), name = 'pdf'     ),

]