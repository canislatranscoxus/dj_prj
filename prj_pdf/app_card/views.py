import weasyprint

from datetime               import datetime
from os                     import path
from django.conf            import settings
from django.http            import HttpResponse
from django.shortcuts       import render
from django.shortcuts       import redirect
from django.template.loader import render_to_string
from django.urls            import reverse
from django.views           import View

from .forms             import CardForm


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
            request.session[ 'from_name' ] = form.cleaned_data[ 'from_name' ]
            request.session[ 'to_name'   ] = form.cleaned_data[ 'to_name'   ]
            request.session[ 'message'   ] = form.cleaned_data[ 'message'   ]
            request.session[ 'img_url'   ] = form.cleaned_data[ 'img_url'   ]

            url = self.success_url
            if 'btn_load_pdf' in request.POST:
                url = 'app_card:load_pdf'
            elif 'btn_save_pdf' in request.POST:
                url = 'app_card:save_pdf'

            return redirect( reverse( url ) )

class PreviewView( View ):
    context_object_name = 'preview'
    #success_url         = 'app_card:preview'
    template_name       = 'pdf.html'

    def get(self, request, *args, **kwargs):
        try:
            my_dic = {
                'from_name' : self.request.session[ 'from_name' ],
                'to_name'   : self.request.session[ 'to_name'   ],
                'message'   : self.request.session[ 'message'   ],
                'img_url'   : self.request.session[ 'img_url'   ],
            }

            return render( request, self.template_name, my_dic )

        except Exception as e:
            print( 'PreviewView.get(), ... {}'.format( e ) )
            raise

# Create the Pdf
class LoadPdfView( View ):
    context_object_name = 'preview'
    #success_url         = 'app_card:preview'
    template_name       = 'pdf.html'

    # ~/git/dj_prj/prj_pdf/my_pdf
    tar_dir = '/home/art/git/dj_prj/prj_pdf/my_pdf/'


    def get(self, request, *args, **kwargs):
        try:
            dt        = datetime.now()
            # you can pass a dictionary with data, like in the example below.

            my_dic = {
                'from_name' : self.request.session[ 'from_name' ],
                'to_name'   : self.request.session[ 'to_name'   ],
                'message'   : self.request.session[ 'message'   ],
                'img_url'   : self.request.session[ 'img_url'   ],
            }

            html                            = render_to_string('pdf.html', my_dic )

            response                        = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
            response['Content-Disposition'] =  'filename={}.pdf'.format( dt.isoformat( timespec= 'seconds' ) )


            ##css_path = os.path.join(settings.STATIC_ROOT, 'css/pdf.css')
            css_path = path.join( settings.STATICFILES_DIRS[0]  , 'css/pdf.css' )

            weasyprint.HTML     ( string=html, base_url=request.build_absolute_uri() 
                    ).write_pdf(response, stylesheets=[ weasyprint.CSS( css_path )])

            return response

            #return render( request, self.template_name )

        except Exception as e:
            print( 'PreviewView.get(), ... {}'.format( e ) )
            raise







'''
    def save_file( self, obj ):
        try:
            dt        = datetime.now()
            s         = dt.isoformat( timespec= 'seconds' ) + '.pdf'
            file_name = path.join( self.tar_dir, s )
            print( file_name )


        except Exception as e:
            print(  )


'''