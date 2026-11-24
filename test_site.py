import re
from playwright.sync_api import Page, expect

def test_home(page: Page):
    page.goto("http://localhost:5000/")
    # controllo con il titolo usando una regex (quindi anche parte del titolo va bene)
    expect(page).to_have_title(re.compile("La Mia App Flask"))

def test_insert_data(page: Page) -> None:
    page.goto("http://localhost:5000/")
    page.get_by_role("button", name="Toggle navigation").click()
    page.get_by_role("link", name="Data").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("Autore")
    page.get_by_role("textbox", name="Message").click()
    page.get_by_role("textbox", name="Message").fill("Messaggio playwright per pytest")
    page.get_by_role("button", name="Invia messaggio").click()
    expect(page.get_by_role("main")).to_contain_text("Messaggio playwright per pytest")
