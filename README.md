# detailing_store
E-commerce web app created with Python, Django, JS and Bootstrap4 that integrates the following concepts:

 * usage of Django authentication system to handle the site access and user authorization – extending User object with one-to-one model,
 * using Django ORM to perform CRUD operations on SQLite database,
 * usage of Signals to perform actions triggered by the user,
 * usage of Sessions to pass data between the views,
 * PayPal API integration to process payments.

This Django project runs in the development mode and the below setup guide assumes that it will be run on a local machine:

1. Create your virtual environment to install necessary packages to run the project
    `conda create --name yourenvname` - this will be a command to use if you are using Anaconda to manage your virtual environments 
2. Activate your virtual environment. 
    `conda activate yourenvname`
3. Install requried packages to run the project by using requirements.txt file.
    `conda install --file requirements.txt`
4. Install PayPal checkout server by typing:
    `pip install paypal-checkout-serversdk`dd
5. You will need to have Paypal sandbox account created to be able to set the below values.
https://developer.paypal.com/docs/api/overview/#create-sandbox-accounts
6. Following setup would be needed in the project to be able to test the Paypal payments:
    - in the /detailing_store/settings.py file:<br/>
     `PAYPAL_RECEIVER_EMAIL = "Replace this text with your PayPal sandbox business email"`
    
    - in the detailing_store/shopping_basket/paypal.py file:<br/>
     `self.client_id = "Replace this text with your PayPal sandbox business CLIENT ID"`<br/>
     `self.client_secret = "Replace this text with your PayPal sandbox business CLIENT SECRET"`
     
    - in the shopping_basket/templates/shopping_basket/checkout.html file:<br/>
     `<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=GBP&disable-funding=sofort"></script>`<br/>
     Replace YOUR_CLIENT_ID with your PayPal sandbox client ID.
     
7. Now with your env active you should be able to successfully run the project by using usual django command:<br/>
    `python manage.py runserver`

8. Create admin user if you would like to have access to admin dashboard:
    `python manage.py createsuperuser`<br/>
    Standard users can be added by clicking Sign up button on the main page.

9. The database is preloaded with a 20 fake products so the migrations would not be needed.  


Runing project screenshot:

![alt text](https://github.com/Nor-Mal/detailing_store/blob/main/project%20screenshot.png)

Database vi

