# Generate a PDF from a django html page.

In this mini example project we show how to create a pdf file,
we take as input an html page and generate a new pdf file.

The main idea is create an html page as pretty as you want,
you can use css style, fill data programatically, etc.
Just make your html as you want.

The next step is use weasyprint library to generate the pdf.
Simple like that.

Enjoy it.


### create project
```django-admin startproject prj_pdf```


### create app


```
cd prj_pdf
python manage.py startapp app_card
```


### run server
`python manage.py runserver`


### install libraries


### Links and resources

Here we have links to some useful documents and examples.

* Weasyprint Official Site
https://weasyprint.org/

* Python PDF Generation from HTML with WeasyPrint
https://dev.to/bowmanjd/python-pdf-generation-from-html-with-weasyprint-538h
Jonathan Bowman
Posted on Oct 17, 2020

* PDF output using Weasyprint not showing images (Django)
https://stackoverflow.com/questions/48988707/pdf-output-using-weasyprint-not-showing-images-django

