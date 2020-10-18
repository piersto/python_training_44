# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.open_add_new_contact_page()

    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(firstname='First name',
                                             middlename='Middlename', lastname='Lastname',
                                             birthday='31', birth_month='December')
    app.contact.fill_in_contact_form(contact)
    list_of_contacts_new = app.contact.list_of_contacts()
    assert len(list_of_contacts_old) + 1 == len(list_of_contacts_new)
    list_of_contacts_old.append(contact)
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_add_empty_contact(app):
    app.contact.open_add_new_contact_page()
    app.contact.fill_in_contact_form(Contact(firstname='', middlename='', lastname=''))


