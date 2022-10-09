from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.make(Contact(firstname="test", home_number="1234567890"))
    app.contact.delete_first_contact()
