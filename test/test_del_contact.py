# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be deleted'))
    app.contact.delete_first_contact()

