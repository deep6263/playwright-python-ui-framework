import pytest

@pytest.mark.smoke
def test_framework_setup():
    """
    Smoke test to verify that the testing framework is set up correctly.
    This test will always pass if the framework is functioning properly.
    """
    assert True