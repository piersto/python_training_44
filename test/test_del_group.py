# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_group_by_index(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name='Test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
