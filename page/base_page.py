

class BasePage():
    def open(self):
        self.driver.get(self.url)
    def switch_window(self):
        self.driver.switch_window(handles[-1])
