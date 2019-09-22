from .baseapi import BaseAPI
from pypaystack import utils

 
class Transfer(BaseAPI):

    def verify_account(self, account_number=None, bank_code=None):
        """
        Gets all your transactions
        
        args:
        pagination -- Count of data to return per call 
        """
        assert (account_number and  bank_code)
        url = self._url("https://api.paystack.co/bank/resolve?account_number={}&bank_code={}".format(
            account_number, bank_code
        ))

        return self._handle_request('GET', url)

    def create_recipient(self, account_number=None, bank_code=None, name=None):
        
        payload = {
            "type": "nuban",
            "name": name,
            # "description": "Customer1029 bank account",
            "account_number": account_number,
            "bank_code": bank_code,
            "currency": "NGN",
            }
        url = self._url("https://api.paystack.co/transferrecipient")
        return self._handle_request('POST', url, payload)


    def initialize(self, amount, recipient_code):
        """
        Initialize a transfer and returns the response
        
        amount -- Amount to charge
        recipient_code
        """
        amount = utils.validate_amount(amount)

        payload = {
            "amoun": amount,
            "recipient_code": recipient_code,
        }

        url = self._url("POST", "https://api.paystack.co/transfer", payload)

    def charge(self, payload):
        """
        -d '{
            "currency": "NGN",
            "source": "balance",
            "transfers": [
            {
            "amount": 50000,
            "recipient": "RCP_db342dvqvz9qcrn"
            },
            {
            "amount": 50000,
            "recipient": "RCP_db342dvqvz9qcrn"
            }
            """
        url = self._url("https://api.paystack.co/transfer/bulk")
        return self._handle_request('POST', url, payload)
