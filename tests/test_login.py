
from utils.file import get_json_value
from pytest_bdd import scenario, given, when, then

data = get_json_value("../test_data/credentials.json", "credentials")


@scenario("../features/login.feature", "Successful Login")
def test_companieshouse_data_flows():
#     """Verify Data Companieshouse data flow."""
#     pass


@when("../features/login.feature", "Successful Login")
def test_companieshouse_data_flows():
# """Verify Data Companieshouse data flow."""
#     pass