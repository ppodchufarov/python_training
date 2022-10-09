from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.make(Contact(firstname="test", home_number="1234567890"))
    app.contact.modify_first_contact(Contact(firstname="New contact"))


def test_modify_contact_home_number(app):
    if app.contact.count() == 0:
        app.contact.make(Contact(firstname="test", home_number="1234567890"))
    app.contact.modify_first_contact(Contact(home_number="8887888"))
