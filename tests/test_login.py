def test_google_title(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()


def test_sample():
    assert True