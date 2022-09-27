from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New contact"))


def test_modify_contact_home_number(app):
    app.contact.modify_first_contact(Contact(home_number="8887888"))
