from playwright.sync_api import Page , Locator


class BasePage:
    def __init__(self , page:Page):
        self.page = page

    def navigate(self , url:str = "/")-> None:
        self.page.goto(url)

    def click(self , locator:Locator)-> None:
        locator.click()

    def fill(self , locator:Locator , value:str)-> None:
        locator.fill(value)

    def get_text(self , locator:Locator)-> str:
        return locator.inner_text()
    
    def get_title(self)-> str:
        return self.page.title()

    def is_visible(self , locator:Locator)-> bool:
        return locator.is_visible()