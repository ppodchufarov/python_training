

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def make(self, contact):
        wd = self.app.wd
        self.open_to_home_page()
        # open contact creation page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation (press 'Enter')
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # closing the pop-up window
        wd.switch_to.alert.accept()

    def modify_first_contact(self, new_contact_date):
        wd = self.app.wd
        self.open_to_home_page()
        self.select_first_contact()
        # follow edit contact form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_date)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.open_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("home", contact.home_number)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
