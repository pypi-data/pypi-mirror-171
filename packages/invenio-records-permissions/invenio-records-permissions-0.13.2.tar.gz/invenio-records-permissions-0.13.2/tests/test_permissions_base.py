# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020 CERN.
# Copyright (C) 2019-2020 Northwestern University.
#
# Invenio-Records-Permissions is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

from elasticsearch_dsl import Q
from flask_principal import Identity
from invenio_access.permissions import any_user

from invenio_records_permissions.api import permission_filter
from invenio_records_permissions.generators import AnyUser, Disable
from invenio_records_permissions.policies import BasePermissionPolicy


def test_base_permission_policy_generators(app):
    policy = BasePermissionPolicy

    for action in ['search', 'read', 'update', 'delete']:
        generators = policy(action=action).generators
        assert len(generators) == 0

    assert isinstance(policy(action='random').generators[0], Disable)


class TestPermissionPolicy(BasePermissionPolicy):
    can_create = [AnyUser()]
    can_search = [AnyUser()]
    can_read = [AnyUser()]
    can_foo_bar = [AnyUser()]
    can_baz = []


def test_permission_policy_generators(app):
    policy = TestPermissionPolicy

    assert isinstance(policy(action='create').generators[0], AnyUser)
    assert isinstance(policy(action='search').generators[0], AnyUser)
    assert isinstance(policy(action='read').generators[0], AnyUser)
    assert isinstance(policy(action='foo_bar').generators[0], AnyUser)
    assert len(policy(action='update').generators) == 0
    assert len(policy(action='delete').generators) == 0
    assert isinstance(policy(action='random').generators[0], Disable)


def test_permission_policy_needs_excludes(role_w_superuser_access_need):
    create_perm = TestPermissionPolicy(action='create')
    list_perm = TestPermissionPolicy(action='search')
    read_perm = TestPermissionPolicy(action='read')
    update_perm = TestPermissionPolicy(action='update')
    delete_perm = TestPermissionPolicy(action='delete')
    foo_bar_perm = TestPermissionPolicy(action='foo_bar')

    assert create_perm.needs == {role_w_superuser_access_need, any_user}
    assert create_perm.excludes == set()

    assert list_perm.needs == {role_w_superuser_access_need, any_user}
    assert list_perm.excludes == set()

    assert read_perm.needs == {role_w_superuser_access_need, any_user}
    assert read_perm.excludes == set()

    assert update_perm.needs == {role_w_superuser_access_need}
    assert update_perm.excludes == set()

    assert delete_perm.needs == {role_w_superuser_access_need}
    assert delete_perm.excludes == set()

    assert foo_bar_perm.needs == {role_w_superuser_access_need, any_user}
    assert foo_bar_perm.excludes == set()


def test_permission_policy_query_filters(superuser_identity):
    # Any user
    any_user_identity = Identity(1)
    any_user_identity.provides.add(any_user)
    perm = TestPermissionPolicy(action="baz", identity=any_user_identity)

    assert [] == perm.query_filters

    # Superuser
    perm = TestPermissionPolicy(action="baz", identity=superuser_identity)

    assert [Q()] == perm.query_filters


def test_permission_filter(mocker):
    """Test permission_filter func."""

    # permission is None
    permission = None
    filter_ = permission_filter(permission)
    assert Q() == filter_

    # permission.query_filters returns []
    permission = mocker.Mock(query_filters=[])
    filter_ = permission_filter(permission)
    assert Q() == filter_

    # permission.query_filters returns [Q]
    permission = mocker.Mock(query_filters=[Q("term", fieldA="valueA")])
    filter_ = permission_filter(permission)
    assert Q("term", fieldA="valueA") == filter_

    # permission.query_filters returns [Q1, Q2]
    permission = mocker.Mock(query_filters=[Q(), Q("term", fieldA="valueA")])
    filter_ = permission_filter(permission)
    assert Q() == filter_
