from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Replace this text with your PayPal sandbox business CLIENT ID"
        self.client_secret = "Replace this text with your PayPal sandbox business CLIENT SECRET"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
