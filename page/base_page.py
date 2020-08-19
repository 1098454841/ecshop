

class BasePage():
    def open(self):
        self.driver.get(self.url)
    def switch_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
