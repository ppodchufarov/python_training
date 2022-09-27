from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New contact"))
    app.session.logout()


def test_modify_contact_home_number(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home_number="8887888"))
    app.session.logout()
