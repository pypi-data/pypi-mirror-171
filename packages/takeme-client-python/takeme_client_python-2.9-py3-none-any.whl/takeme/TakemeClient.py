from takeme.TakemeRequestor import TakemeRequestor
from takeme.RsaUtil import RsaUtil


class TakemeClient:

    ACCESS_LEVEL_SHARED = "Shared"
    ACCESS_LEVEL_VIEW_ONLY = "View Only"

    REQUEST_STATUS_PENDING = "Pending"
    REQUEST_STATUS_APPROVE = "Approve"
    REQUEST_STATUS_REJECT = "Reject"

    def __init__(self, corporate_code, secret_key, is_production=False):
        self.request_takeme = TakemeRequestor(corporate_code, secret_key, is_production)

    def non_auth_call_file(self, file, data, endpoint):
        response = self.request_takeme.call_api_file_without_bearer(endpoint, file, data)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.json()

    def non_auth_call(self, body, endpoint):
        response = self.request_takeme.call_api_without_bearer(endpoint, body)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.json()

    def non_auth_call_with_pin(self, body, endpoint, pin):
        encrypted_pin = RsaUtil.encrypt(pin)
        response = self.request_takeme.call_api_without_bearer_and_pin(endpoint, body, encrypted_pin)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.json()

    def auth_call(self, body, endpoint, jwt):
        response = self.request_takeme.call_api_with_bearer(endpoint, body, jwt)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.json()

    def auth_call_with_pin(self, body, endpoint, jwt, pin):
        encrypted_pin = RsaUtil.encrypt(pin)
        response = self.request_takeme.call_api_with_bearer_and_pin(endpoint, body, jwt, encrypted_pin)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.json()

    def user_signup(self, full_name, email, phone_number, channel="wa"):
        endpoint = "uaa/signup"

        if channel == "sms":
            endpoint = "uaa/signup/sms"

        body = {
            "full_name": full_name,
            "email": email,
            "phone_number": phone_number
        }

        self.non_auth_call(body, endpoint)

    def user_activation(self, email, phone_number, activation_code):
        endpoint = "uaa/activation"
        body = {
            "email": email,
            "phone_number": phone_number,
            "activation_code": activation_code,
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def user_prelogin(self, phone_number, channel="wa"):
        endpoint = "uaa/prelogin"

        if channel == "sms":
            endpoint = "uaa/prelogin/sms"

        body = {
            "phone_number": phone_number,
        }

        self.non_auth_call(body, endpoint)

    def user_login(self, phone_number, login_code):
        endpoint = "uaa/login"
        body = {
            "phone_number": phone_number,
            "login_code": login_code,
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data").get("jwt")

    def user_save_pin(self, pin, jwt):
        endpoint = "user/save-pin"
        body = {
            "pin": RsaUtil.encrypt(pin)
        }

        self.auth_call(body, endpoint, jwt)

    def user_pre_forgot_pin(self, new_pin, jwt, channel="wa"):
        endpoint = "user/pre-forgot-pin"

        if channel == "sms":
            endpoint = "user/pre-forgot-pin/sms"

        body = {
            "pin": RsaUtil.encrypt(new_pin)
        }

        self.auth_call(body, endpoint, jwt)

    def user_confirm_forgot_pin(self, otp, jwt):
        endpoint = "user/forgot-pin"
        body = {
            "confirm_pin_code": otp
        }

        self.auth_call(body, endpoint, jwt)

    def user_change_pin(self, old_pin, new_pin, jwt):
        endpoint = "user/change-pin"
        body = {
            "old_pin": RsaUtil.encrypt(old_pin),
            "new_pin": RsaUtil.encrypt(new_pin)
        }

        self.auth_call(body, endpoint, jwt)

    def user_detail(self, jwt):
        endpoint = "user/check"
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_main_balance(self, jwt):
        endpoint = "user/check"
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data").get("main_balance")

    def user_balance(self, jwt):
        endpoint = "user/check"
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data").get("list_balance")

    def user_balance_statement(self, balance_id, jwt, offset=1, limit=10):
        endpoint = "balance/" + balance_id + "?" + "page=" + str(offset) + "&limit=" + str(limit)
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_transaction_history(self, jwt, offset=1, limit=10):
        endpoint = "transaction/?" + "page=" + str(offset) + "&limit=" + str(limit)
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_inquiry_bank_account(self, account_number, bank_code, jwt):
        endpoint = "transaction/account-holdername"
        body = {
            "account_number": account_number,
            "bank_code": bank_code
        }

        response = self.auth_call(body, endpoint, jwt)

        if not response.get("data").get("account_name"):
            raise ValueError("Invalid account number")
        else:
            return response.get("data")

    def set_bank_account(self, account_number, bank_code, jwt):
        response = self.user_inquiry_bank_account(account_number, bank_code, jwt)

        bank_account = {
            "name": response.get("account_name"),
            "account_number": response.get("account_number"),
            "bank_code": response.get("bank_name")
        }

        return bank_account

    def transfer_to_bank(self, bank_account, amount, pin, jwt, external_id="", source_balance=""):
        endpoint = "transaction/transfer/wallet"
        body = {
            "to_bank_account": bank_account,
            "type": "TRANSFER_TO_BANK",
            "notes": "",
            "amount": amount,
            "balance": source_balance,
            "external_id": external_id,
        }

        response = self.auth_call_with_pin(body, endpoint, jwt, pin)

        return response.get("data")

    def user_bulk_inquiry_bank_account(self, list_bulk, jwt):
        endpoint = "transaction/account-holdername/bulk"
        body = {
            "list_bulk": list_bulk
        }

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_view_bulk_inquiry_bank_account(self, bulk_id, jwt):
        endpoint = "transaction/account-holdername/bulk/%s" % (bulk_id)
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_create_bulk_transfer(self, list_bank_account, reference, jwt, source_balance=""):
        endpoint = "transaction/transfer/bank/bulk"
        body = {
            "reference": reference,
            "list_bulk": [],
            "balance": source_balance
        }

        for x in list_bank_account:
            body["list_bulk"].append({
                "to_bank_account": {
                    "name": x["account_name"],
                    "bank_code": x["bank_name"],
                    "account_number": x["account_number"],
                },
                "type": "TRANSFER_TO_BANK",
                "notes": "Transfer",
                "amount": x["amount"],
                "external_id": x["external_id"],
            })

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_bulk_transfer(self, bulk_id, pin, jwt):
        endpoint = "transaction/transfer/bank/bulk/" + bulk_id

        body = {}

        response = self.auth_call_with_pin(body, endpoint, jwt, pin)

        return response.get("data")

    def user_view_bulk_transfer(self, bulk_id, jwt):
        endpoint = "transaction/transfer/bank/bulk/%s" % (bulk_id)
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")


    def corporate_view_bulk_transfer(self, bulk_id):
        endpoint = "transaction/transfer/bank/bulk/%s" % (bulk_id)
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def user_create_balance(self, name, jwt):
        endpoint = "user/balance"
        body = {
            "name": name,
        }

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_create_request_access_balance(self, balance_id, access_level, jwt):
        endpoint = "user/request-balance"
        body = {
            "balance": balance_id,
            "access": access_level,
        }

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_view_request_access_balance_as_requester(self, status, jwt):
        endpoint = "user/request-balance/requester?status=" + status
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_view_request_access_balance_as_owner(self, status, jwt):
        endpoint = "user/request-balance/owner?status=" + status
        body = None

        response = self.auth_call(body, endpoint, jwt)

        return response.get("data")

    def user_submit_request_access_balance(self, request_id, status, pin, jwt):
        endpoint = "user/request-balance/%s" % (request_id) + "/" + status
        body = {}

        response = self.auth_call_with_pin(body, endpoint, jwt, pin)

        return response.get("data")

    def aggregate_balance(self):
        endpoint = "corporate/aggregate-balance"
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_inquiry_bank_account(self, account_number, bank_code):
        endpoint = "corporate/account-holdername"
        body = {
            "account_number": account_number,
            "bank_code": bank_code
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_create_bulk_transfer(self, list_bank_account, reference, source_balance=""):
        endpoint = "corporate/transfer/bank/bulk"
        body = {
            "reference": reference,
            "list_bulk": [],
            "balance": source_balance,
        }

        for x in list_bank_account:
            body["list_bulk"].append({
                "to_bank_account": {
                    "name": x["account_name"],
                    "bank_code": x["bank_name"],
                    "account_number": x["account_number"],
                },
                "type": "TRANSFER_TO_BANK",
                "notes": "Transfer",
                "amount": x["amount"],
                "external_id": x["external_id"],
            })

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_save_pin(self, pin):
        endpoint = "corporate/save-pin"
        body = {
            "pin": RsaUtil.encrypt(pin)
        }

        self.non_auth_call(body, endpoint)

    def corporate_pre_forgot_pin(self, new_pin, channel="wa"):
        endpoint = "corporate/pre-forgot-pin"

        if channel == "sms":
            endpoint = "corporate/pre-forgot-pin/sms"

        body = {
            "pin": RsaUtil.encrypt(new_pin)
        }

        self.non_auth_call(body, endpoint)

    def corporate_confirm_forgot_pin(self, otp):
        endpoint = "corporate/forgot-pin"
        body = {
            "confirm_pin_code": otp
        }

        self.non_auth_call(body, endpoint)

    def corporate_change_pin(self, old_pin, new_pin):
        endpoint = "corporate/change-pin"
        body = {
            "old_pin": RsaUtil.encrypt(old_pin),
            "new_pin": RsaUtil.encrypt(new_pin)
        }

        self.non_auth_call(body, endpoint)

    def corporate_topup_user(self, phone_number, amount, pin, source_balance="", target_balance="", external_id=""):
        endpoint = "corporate/topup-user"
        body = {
            "phone_number": phone_number,
            "amount": amount,
            "source_balance_id": source_balance,
            "target_balance_id": target_balance,
            "external_id": external_id,
        }

        self.non_auth_call_with_pin(body, endpoint, pin)

    def corporate_deduct_user(self, phone_number, amount, pin, source_balance="", target_balance="", external_id=""):
        endpoint = "corporate/deduct-user"
        body = {
            "phone_number": phone_number,
            "amount": amount,
            "source_balance_id": source_balance,
            "target_balance_id": target_balance,
            "external_id": external_id,
        }

        self.non_auth_call_with_pin(body, endpoint, pin)

    def corporate_bulk_inquiry_bank_account(self, list_bulk):
        endpoint = "corporate/account-holdername/bulk"
        body = {
            "list_bulk": list_bulk
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_view_bulk_inquiry_bank_account(self, bulk_id):
        endpoint = "corporate/account-holdername/bulk/%s" % (bulk_id)
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_fetch_user_balance(self, list_user_id):
        endpoint = "corporate/user-balance"
        body = {
            "users": list_user_id
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_create_balance(self, name):
        endpoint = "corporate/balance"
        body = {
            "name": name,
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_share_balance(self, balance_id, access_level, share_to, pin):
        endpoint = "corporate/balance/share"
        body = {
            "balance": balance_id,
            "access": access_level,
            "share_to": share_to
        }

        response = self.non_auth_call_with_pin(body, endpoint, pin)

        return response.get("data")

    def corporate_revoke_balance(self, balance_id, revoke_from, pin):
        endpoint = "corporate/balance/revoke"
        body = {
            "balance": balance_id,
            "revoke_from": revoke_from
        }

        response = self.non_auth_call_with_pin(body, endpoint, pin)

        return response.get("data")

    def corporate_create_request_access_balance(self, balance_id, access_level):
        endpoint = "corporate/request-balance"
        body = {
            "balance": balance_id,
            "access": access_level,
        }

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_view_request_access_balance_as_requester(self, status):
        endpoint = "corporate/request-balance/requester?status=" + status
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_view_request_access_balance_as_owner(self, status):
        endpoint = "corporate/request-balance/owner?status=" + status
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def corporate_submit_request_access_balance(self, request_id, status, pin):
        endpoint = "corporate/request-balance/%s" % (request_id) + "/" + status
        body = {}

        response = self.non_auth_call_with_pin(body, endpoint, pin)

        return response.get("data")

    def corporate_main_balance(self):
        endpoint = "corporate/check"
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data").get("main_balance")

    def corporate_balance(self):
        endpoint = "corporate/check"
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data").get("list_balance")

    def corporate_balance_statement(self, balance_id, offset=1, limit=10):
        endpoint = "balance/" + balance_id + "?" + "page=" + str(offset) + "&limit=" + str(limit)
        body = None

        response = self.non_auth_call(body, endpoint)

        return response.get("data")

    def verify_user(self, akta, npwp, nib, identity, nik, legal_name, legal_address, user_id):
        endpoint = "user/verify"

        files = {
            'akta_image': akta,
            'npwp_image':npwp,
            'nib_image': nib,
            'identity_image': identity,
        }

        payload = {
            'nik': nik,
            'legal_name': legal_name,
            'legal_address': legal_address,
            'user_id': user_id,
        }

        response = self.non_auth_call_file(files, payload, endpoint)

        akta.close()
        npwp.close()
        nib.close()
        identity.close()

        return response.get("data")


