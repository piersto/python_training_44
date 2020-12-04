# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact('Contact to be deleted'))
    list_of_contact_old = app.contact.list_of_contacts()
    app.contact.delete_first_contact()
    assert len(list_of_contact_old) - 1 == app.contact.count()
    list_of_contacts_new = app.contact.list_of_contacts()
    list_of_contact_old[0:1] = []
    assert list_of_contact_old == list_of_contacts_new


