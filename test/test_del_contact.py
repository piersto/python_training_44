# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be deleted'))
    list_of_contact_old = app.contact.list_of_contacts()
    app.contact.delete_first_contact()
    list_of_contacts_new = app.contact.list_of_contacts()
    assert len(list_of_contact_old) - 1 == len(list_of_contacts_new)


