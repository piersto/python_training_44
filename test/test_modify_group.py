from model.group import Group
from random import randrange


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Montreal group', footer='aoeu'))
    old_groups = app.group.get_group_list()
    group = Group(name='Mafia group')
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = app.group.get_group_list()
    group = Group(header='New Header')
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header_by_index(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header='New Header')
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)