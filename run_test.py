import pytest
import os

if __name__ == "__main__":
    os.makedirs("reports", exist_ok=True)
    pytest.main(["test_main.py", "--junitxml=reports/tests.xml"])