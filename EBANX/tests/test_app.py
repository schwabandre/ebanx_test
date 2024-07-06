import unittest
from app import app 

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.app.post('/reset')

    def test_reset(self):
        response = self.app.post('/reset')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "System reset successful"})

    def test_get_balance_non_existing_account(self):
        response = self.app.get('/balance?account_id=1234')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Account not found"})

    def test_create_account_with_initial_balance(self):
        response = self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"destination": {"id": "100", "balance": 10}})

    def test_deposit_into_existing_account(self):
        self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        response = self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"destination": {"id": "100", "balance": 20}})

    def test_get_balance_existing_account(self):
        self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        response = self.app.post('/balance?account_id=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"balance": 10})

    def test_withdraw_from_non_existing_account(self):
        response = self.app.post('/event', json={"type": "withdraw", "origin": "200", "amount": 10})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Insufficient funds or account not found"})

    def test_withdraw_from_existing_account(self):
        self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        response = self.app.post('/event', json={"type": "withdraw", "origin": "100", "amount": 5})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"origin": {"id": "100", "balance": 5}})

    def test_transfer_from_existing_account(self):
        self.app.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
        response = self.app.post('/event', json={"type": "transfer", "origin": "100", "amount": 5, "destination": "200"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"origin": {"id": "100", "balance": 5}, "destination": {"id": "200", "balance": 5}})

    def test_transfer_from_non_existing_account(self):
        response = self.app.post('/event', json={"type": "transfer", "origin": "200", "amount": 5, "destination": "300"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Insufficient funds or account not found"})

if __name__ == '__main__':
    unittest.main()
