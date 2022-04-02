from django.shortcuts import render

from django.shortcuts           import redirect, get_object_or_404
from django.urls                import reverse
from django.views               import View

from .forms                     import CardForm


# Create your views here.

class EditView( View ):
    '''Here we Edit the Card with a pretty message'''
    context_object_name = 'edit'
    success_url         = 'app_card:preview'
    template_name       = 'edit.html'
    form_class          = CardForm

    def get(self, request, *args, **kwargs):
        try:
            form = CardForm()

            my_dic       = {
                'form'     : form,
            }
            
            return render( request, self.template_name, my_dic )

        except Exception as e:
            print( 'EditView.get(), ... {}'.format( e ) )
            raise


    def post(self, request ):
        
        print( '... begin' )
        form = self.form_class(request.POST)

        if form.is_valid():
            request.session[ '_from'    ] = form.cleaned_data[ '_from'    ]
            request.session[ '_to'      ] = form.cleaned_data[ '_to'      ]
            request.session[ '_message' ] = form.cleaned_data[ '_message' ]
            request.session[ '_img_url' ] = form.cleaned_data[ '_img_url' ]

            return redirect( reverse( self.success_url ) )


