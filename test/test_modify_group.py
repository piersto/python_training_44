from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    app.group.modify_first_group(Group(name='New Name'))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    app.group.modify_first_group(Group(header='New Header'))
