def test_google_title(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

# import pytest

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         page = item.funcargs.get("page")
#         if page:
#             page.screenshot(path="failure.png")