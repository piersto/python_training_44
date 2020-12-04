from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname='Pierre',
                                                    middlename='Nikola',
                                                        lastname='Gotier'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(lastname='Kovalevsky')
    contact.id = list_of_contacts_old[0].id
    app.contact.modify_first_contact(contact)
    assert len(list_of_contacts_old) == app.contact.count()
    list_of_contacts_new = app.contact.list_of_contacts()
    list_of_contacts_old[0] = contact
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname='Contact to be modified'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(middlename='II', birthday='15')
    contact.id = list_of_contacts_old[0].id
    app.contact.modify_first_contact(contact)
    assert len(list_of_contacts_old) == app.contact.count()
    list_of_contacts_new = app.contact.list_of_contacts()
    list_of_contacts_old[0] = contact
    assert sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)


def test_modify_contact_birth_month(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact('Contact to be modified'))
    list_of_contacts_old = app.contact.list_of_contacts()
    contact = Contact(birth_month='April')
    contact.id = list_of_contacts_old[0].id
    app.contact.modify_first_contact(contact)
    assert len(list_of_contacts_old) == app.contact.count()
    list_of_contacts_new = app.contact.list_of_contacts()
    list_of_contacts_old[0] = contact
    assert  sorted(list_of_contacts_old, key=Contact.id_or_max) == sorted(list_of_contacts_new, key=Contact.id_or_max)
