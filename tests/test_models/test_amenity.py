#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amt = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amt.__dict__)

    def test_two_amenities_unique_ids(self):
        amt1 = Amenity()
        amt2 = Amenity()
        self.assertNotEqual(amt1.id, amt2.id)

    def test_two_amenities_different_created_at(self):
        amt1 = Amenity()
        sleep(0.05)
        amt2 = Amenity()
        self.assertLess(am1.created_at, amt2.created_at)

    def test_two_amenities_different_updated_at(self):
        amt1 = Amenity()
        sleep(0.05)
        amt2 = Amenity()
        self.assertLess(amt1.updated_at, amt2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        amt = Amenity()
        amt.id = "123456"
        amt.created_at = amt.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        amt = Amenity(None)
        self.assertNotIn(None, amt.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amt = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amt.id, "345")
        self.assertEqual(amt.created_at, dt)
        self.assertEqual(amt.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amt = Amenity()
        sleep(0.05)
        first_updated_at = amt.updated_at
        amt.save()
        self.assertLess(first_updated_at, amt.updated_at)

    def test_two_saves(self):
        amt = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        amt.save()
        second_updated_at = amt.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amt.save()
        self.assertLess(second_updated_at, amt.updated_at)

    def test_save_with_arg(self):
        amt = Amenity()
        with self.assertRaises(TypeError):
            amt.save(None)

    def test_save_updates_file(self):
        amt = Amenity()
        amt.save()
        amid = "Amenity." + amt.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amt = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amt = Amenity()
        amt.middle_name = "Clinton"
        amt.my_number = 98
        self.assertEqual("Holberton", amt.middle_name)
        self.assertIn("my_number", amt.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amt = Amenity()
        amt_dict = amt.to_dict()
        self.assertEqual(str, type(amt_dict["id"]))
        self.assertEqual(str, type(amt_dict["created_at"]))
        self.assertEqual(str, type(amt_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        amt = Amenity()
        amt.id = "123456"
        amt.created_at = amt.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(amt.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amt = Amenity()
        self.assertNotEqual(amt.to_dict(), amt.__dict__)

    def test_to_dict_with_arg(self):
        amt = Amenity()
        with self.assertRaises(TypeError):
            amt.to_dict(None)


if __name__ == "__main__":
