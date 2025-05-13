import requests
from requests.auth import HTTPBasicAuth
import json
import random
import string
from datetime import datetime
import logging

class APIRequestUtility:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint, method='GET', headers=None, params=None, data=None, auth=None):
        url = f"{self.base_url}{endpoint}"
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, auth=auth)
            elif method == 'POST':
                response = requests.post(url, headers=headers, params=params, json=data, auth=auth)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, params=params, json=data, auth=auth)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, params=params, auth=auth)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            return response
        except Exception as e:
            print(f"Error occurred: {e}")


class APIResponseValidator:
    @staticmethod
    def validate_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, f"Expected {expected_status_code}, but got {response.status_code}"
    
    @staticmethod
    def validate_json_schema(response, schema):
        try:
            json_response = response.json()
            # You can use a library like `jsonschema` for schema validation
            from jsonschema import validate
            validate(instance=json_response, schema=schema)
        except Exception as e:
            print(f"JSON Schema validation failed: {e}")
            raise e
    
    @staticmethod
    def validate_field_value(response, field, expected_value):
        json_response = response.json()
        assert json_response.get(field) == expected_value, f"Expected {field} to be {expected_value}, but got {json_response.get(field)}"

class APIAuthentication:
    @staticmethod
    def get_basic_auth(username, password):
        return HTTPBasicAuth(username, password)

    @staticmethod
    def get_bearer_token(token):
        return {'Authorization': f'Bearer {token}'}




class DataGenerationUtility:
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    @staticmethod
    def random_date(start_date="2020-01-01", end_date="2025-01-01"):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    @staticmethod
    def random_number(min_value=1, max_value=1000):
        return random.randint(min_value, max_value)
    

  

class APIDataDrivenUtility:
    @staticmethod
    def read_json_data(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    
    @staticmethod
    def get_test_data(file_path, test_case):
        data = APIDataDrivenUtility.read_json_data(file_path)
        return data.get(test_case, {})
  




class APIUtilsLogger:
    @staticmethod
    def setup_logger():
        logger = logging.getLogger("APIUtilsLogger")
        handler = logging.FileHandler("api_test.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def log_request_response(logger, request, response):
        logger.info(f"Request: {request.method} {request.url} - {request.body}")
        logger.info(f"Response: {response.status_code} - {response.text}")
