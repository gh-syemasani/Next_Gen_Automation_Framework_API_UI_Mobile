class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://example.com/login"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("id", "submit").click()

    def is_login_successful(self):
        return "Dashboard" in self.driver.page_source

