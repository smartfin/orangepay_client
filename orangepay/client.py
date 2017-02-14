import json
import requests


class OrangePayException(Exception):
    pass


class OrangePay():
    URL_INITIALIZE = 'https://pay.payorange-pay.com/index.php/api/v1/widget/transactions'
    URL_GET_INFO = 'https://pay.payorange-pay.com/index.php/api/v1/widget/transactions/{}'
    URL_GET_SHOP_BALANCE = 'https://pay.payorange-pay.com/index.php/api/v1/balance'

    def __init__(self, api_key, password_key):
        self._api_key = api_key
        self._password_key = password_key

    def start_transaction(self, transaction_data):
        response = requests.post(url=self.URL_INITIALIZE,
                                 auth=(self._api_key, self._password_key),
                                 data=transaction_data)

        data = response.json()

        if response.status_code != 201 or data['status'] != 'success':
            raise OrangePayException(
                '{}: {}'.format(response.status_code, json.dumps(data))
            )

        return data['data']

    def get_transaction_info(self, transaction_id):
        transaction_url = self.URL_GET_INFO.format(transaction_id)

        response = requests.get(url=transaction_url,
                                 auth=(self._api_key, self._password_key),
                                 )

        data = response.json()

        if response.status_code != 200 or data['status'] != 'success':
            raise OrangePayException(
                '{}: {}'.format(response.status_code, json.dumps(data))
            )

        return data['data']['transaction']

    def get_shop_balance(self):
        response = requests.get(url=self.URL_GET_SHOP_BALANCE,
                                auth=(self._api_key, self._password_key),
                                )

        data = response.json()

        if response.status_code != 201 or data['status'] != 'success':
            raise OrangePayException(
                '{}: {}'.format(response.status_code, json.dumps(data))
            )

        return data['data']['balance']