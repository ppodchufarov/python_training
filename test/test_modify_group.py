from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="edit", header="edit", footer="edit"))
    app.session.logout()
