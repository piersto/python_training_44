from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact(firstname='Pierre',
                                                    middlename='Nikola',
                                                        lastname='Gotier'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(lastname='Kovalevsky')
    contact.id = list_of_contacts_old[0].id
    # contact.firstname = list_of_contacts_old[0].firstname
    app.contact.modify_first_contact(contact)
    list_of_contacts_new = app.contact.list_of_contacts()
    assert len(list_of_contacts_old) == len(list_of_contacts_new)
    list_of_contacts_old[0] = contact
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact(firstname='Contact to be modified'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(middlename='II', birthday='15')
    contact.id = list_of_contacts_old[0].id
    app.contact.modify_first_contact(contact)
    list_of_contacts_new = app.contact.list_of_contacts()
    assert len(list_of_contacts_old) == len(list_of_contacts_new)
    list_of_contacts_old[0] = contact
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_modify_contact_birth_month(app):
    if app.contact.count() == 0:
        app.contact.fill_in_contact_form(Contact('Contact to be modified'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(birth_month='April')
    contact.id = list_of_contacts_old[0].id
    app.contact.modify_first_contact(contact)
    list_of_contacts_new = app.contact.list_of_contacts()
    assert len(list_of_contacts_old) == len(list_of_contacts_new)
    list_of_contacts_old[0] = contact
    assert  sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)
