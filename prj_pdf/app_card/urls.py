from django.urls                import path
from .                          import views


app_name = 'app_card'

urlpatterns = [
    path( ''        , views.EditView.as_view()   , name = 'home'       ),
    
    # here you enter data to create a greeting card
    path( 'edit/'   , views.EditView.as_view()   , name = 'edit'       ),

    # here you see an html of your greeting card
    path( 'preview/', views.PreviewView.as_view(), name = 'preview'    ),

    # here we create and load a pdf to the browser
    path( 'load_pdf/', views.LoadPdfView.as_view(),  name = 'load_pdf' ),

    # here we create the pdf object, put in into a BytesIO object, next save to file
    path( 'save_pdf/', views.SavePdfView.as_view(),  name = 'save_pdf' ),

]