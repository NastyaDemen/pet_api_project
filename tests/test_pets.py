# import os.path
#
# import pytest
# import requests

from api import Pets

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_update_pet():
    status = pt.update_pet()[1]
    pet_name = pt.get_updated_pet()[1]
    assert status == 200
    assert pet_name == 'Molly_Taylor'


def test_failed_update_pet_empty_type():
    status = pt.failed_update_pet_empty_type()
    assert status == 422


def test_failed_update_pet_empty_name():
    status = pt.failed_update_pet_empty_name()
    assert status == 422


def test_like_pet():
    status = pt.like_pet()[0]
    likes = pt.get_liked_pet()[2]
    assert status == 200
    assert likes == 1


def test_delete_pet():
    status = pt.delete_pet()[0]
    assert status == 200


def test_get_deleted_pet():
    status = pt.get_deleted_pet()
    assert status == 404
