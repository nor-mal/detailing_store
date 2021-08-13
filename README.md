# detailing_store
E-commerce web app build with Python, Django, SQLite, JQuery and JS

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
    - in the /detailing_store/settings.py
    `PAYPAL_RECEIVER_EMAIL = "Replace this text with your PayPal sandbox business email"`
    - in the detailing_store/shopping_basket/paypal.py
     `self.client_id = "Replace this text with your PayPal sandbox business CLIENT ID"`
     `self.client_secret = "Replace this text with your PayPal sandbox business CLIENT SECRET"`
    - in the shopping_basket/templates/shopping_basket/checkout.html
     `<script src="https://www.paypal.com/sdk/js?client-id=**YOUR_CLIENT_ID**&currency=GBP&disable-funding=sofort">
    // Required. Replace YOUR_CLIENT_ID with your sandbox client ID.
    </script>`