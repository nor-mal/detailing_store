# detailing_store
E-commerce web app build with Python, Django, SQLite, JQuery and JS

This Django project runs in the development mode and the below setup guide assumes that it will be run on a local machine:

1. Create your virtual environment to install necessary packages to run the project
    `conda create --name yourenvname` - this will be a command to use if you are using Anaconda to manage your virtual environments 
2. Activate your virtual environment. 
    `conda activate yourenvname`
3. Install requried packages to run the project by using requirements.txt file.
    `conda install --file requirements.txt`
5. Install PayPal checkout server by typing:
    `pip install paypal-checkout-serversdk`dd
6. You will need to have Paypal sandbox account created to be able to set the below values (please visit https://developer.paypal.com/docs/api/overview/#create-sandbox-accounts):
   - Following changes would need in the project to be made to be able to test the paypal payments:
de
