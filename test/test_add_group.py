# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name='Name group', header='Group header', footer='Group footer'))


def test_add_empty_group(app):
    app.group.create_group(Group(name="", header=" header", footer=""))
