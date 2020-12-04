# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.open_add_new_contact_page()

    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(firstname='Ivan',
                                             middlename='Petrovich', lastname='Kovaliov',
                                             birthday='31', birth_month='December')
    app.contact.add_contact(contact)
    assert len(list_of_contacts_old) + 1 == app.contact.count()
    list_of_contacts_new = app.contact.list_of_contacts()
    list_of_contacts_old.append(contact)
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_add_empty_contact(app):
    app.contact.open_add_new_contact_page()
    app.contact.add_contact(Contact(firstname='', middlename='', lastname=''))


