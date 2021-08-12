from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AcftcPBhlvoYgaCYHZvJjJ2BtInnUAdFbeqsL9i54_1vuzw4NfscVdIh9YvGwQ7iu-tRSjyIvcL5SQLz"
        self.client_secret = "EDEf1Lp4LHQWfS6EXrnWOBGYShsD8ESUUr2Km086IB9lbFcewNhfe_lCi0Am1xT5uVqHHFe6z0ZuNe0V"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
