from model.contact import Contact


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="edit", home_number="777"))
    app.session.logout()
