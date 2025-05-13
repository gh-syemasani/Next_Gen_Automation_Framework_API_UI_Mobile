import pytest
import utils.API_Utils as APIRequestUtility
import utils.API_Utils as APIResponseValidator  
import utils.API_Utils as APIUtilsLogger
import requests

# Example Test Case
@pytest.mark.parametrize("endpoint, expected_status", [("/api/users", 200), ("/api/nonexistent", 404)])
def test_api_responses(endpoint, expected_status):
    api_util = APIRequestUtility("https://jsonplaceholder.typicode.com")
    response = api_util.send_request(endpoint)
    APIResponseValidator.validate_status_code(response, expected_status)
    APIUtilsLogger.log_request_response(APIUtilsLogger.setup_logger(), response.request, response)

