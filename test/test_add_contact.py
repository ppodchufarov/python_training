# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.make(Contact(firstname="qwertyu", home_number="1234567890"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.make(Contact(firstname="", home_number=""))
    app.session.logout()
