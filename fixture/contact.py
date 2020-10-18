from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def fill_in_contact_form(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        self.specify_drop_downs(contact)
        self.submit_contact_form()
        self.app.return_on_home_page()

    def specify_drop_downs(self, contact):
        wd = self.app.wd
        self.select_in_drop_down('bday', contact.birthday)
        self.select_in_drop_down('bmonth', contact.birth_month)

    def select_in_drop_down(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('middlename', contact.middlename)
        self.change_field_value('lastname', contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # click modification button
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # specify new data
        self.fill_contact_form(new_contact_data)
        self.specify_drop_downs(new_contact_data)
        # click update button
        wd.find_element_by_name("update").click()
        # return to home page
        self.app.return_on_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def list_of_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        list_of_contacts = []
        for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
            lastname_text = element.find_element_by_css_selector('td:nth-child(2)').text
            firstname_text = element.find_element_by_css_selector('td:nth-child(3)').text
            id = element.find_element_by_name("selected[]").get_attribute('value')
            list_of_contacts.append(Contact(id=id, lastname=lastname_text, firstname=firstname_text))
        return list_of_contacts

