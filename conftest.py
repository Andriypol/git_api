import pytest
import os
import json
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath=f"{report_dir}/reports_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("Starting")
    yield
    print('End')

@pytest.fixture()
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        return data

