# Generate a PDF from a django html page.

In this mini example project we show how to create a pdf file,
we take as input an html page and generate a new pdf file.

The main idea is create an html page as pretty as you want,
you can use css style, fill data programatically, etc.
Just make your html as you want.

The next step is use weasyprint library to generate the pdf.
Simple like that.

You can take any of these two approaches:

* Create a pdf object and load it to the browser, so the user can see and download it.

* Create a pdf object, put it in a bytes object, next save the pdf as a file in Downloads folder. Here we do not show the pdf on the browser. This approach is very good when you need to generate pdf files in
backend, attach as email, etc.

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


### create a virtual environment and activate it

As a good practice create a virtual environment for your projects.
To do that execute the next commands

```
sudo apt-get install python3-venv
python3 -m venv env
source env/bin/activate
```

### install libraries

Open a terminal
Go to the project folder 
run the next command

```
python -m pip install -r requirements.txt
```


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

