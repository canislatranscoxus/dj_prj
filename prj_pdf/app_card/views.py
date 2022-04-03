from io                     import BytesIO
from pathlib import Path
from os.path                import join

import weasyprint
from   weasyprint           import HTML

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

    def get(self, request, *args, **kwargs):
        try:
            dt        = datetime.now()
            filename  = 'filename={}.pdf'.format( dt.isoformat( timespec= 'seconds' ) )

            # you can pass a dictionary with data, like in the example below.
            my_dic = {
                'from_name' : self.request.session[ 'from_name' ],
                'to_name'   : self.request.session[ 'to_name'   ],
                'message'   : self.request.session[ 'message'   ],
                'img_url'   : self.request.session[ 'img_url'   ],
            }

            html                            = render_to_string('pdf.html', my_dic )
            response                        = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] =  filename
            css_path                        = path.join( settings.STATICFILES_DIRS[0], 'css/pdf.css' )

            weasyprint.HTML     ( string=html, base_url=request.build_absolute_uri()  
                     ).write_pdf( response, stylesheets=[ weasyprint.CSS( css_path )] )

            return response
        except Exception as e:
            print( 'PreviewView.get(), ... {}'.format( e ) )
            raise


class SavePdfView( View ):
    context_object_name = 'preview'
    template_name       = 'pdf_saved.html'
    downloads_dir       = '{}/Downloads/'.format( Path.home() )

    def get(self, request, *args, **kwargs):
        try:
            dt        = datetime.now()
            filename  = '{}.pdf'.format( dt.isoformat( timespec= 'seconds' ) )
            file_path = join( self.downloads_dir, filename )

            # you can pass a dictionary with data, like in the example below.
            my_dic = {
                'from_name' : self.request.session[ 'from_name' ],
                'to_name'   : self.request.session[ 'to_name'   ],
                'message'   : self.request.session[ 'message'   ],
                'img_url'   : self.request.session[ 'img_url'   ],
                'file_path' : file_path,
            }
            
            # generate PDF
            html                            = render_to_string('pdf.html', my_dic )
            #response                        = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] =  filename

            htmldoc = HTML( string=html, base_url="" )
            out         = BytesIO()

            css_path    = join( settings.STATICFILES_DIRS[0], 'css', 'pdf.css' )
            stylesheets = [ weasyprint.CSS( css_path ) ]

            weasyprint.HTML     ( string=html, base_url=request.build_absolute_uri() 
                     ).write_pdf( out, stylesheets = stylesheets  )

            # save file
            with open( file_path, "wb") as f:
                f.write( out.getbuffer())

            return render( request, self.template_name, my_dic )

        except Exception as e:
            print( 'SavePdfView.get(), ... {}'.format( e ) )
            raise




'''

downloads_path = str(Path.home() / "Downloads")
'''