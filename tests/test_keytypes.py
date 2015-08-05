# encoding: utf-8
"""
Ensure different types of key, including mutable and immutable, works
"""

# std imports
import unittest

# local
import sqlitedict2

class KeyTypeTest(unittest.TestCase):
    fname = 'tests/db/sqlitedict2-mutable-test.sqlite'
    def test_list_key(self):
        """Use mutable object as key"""
        d = sqlitedict2.SqliteDict(fname, autocommit=True)
        d[[1,2]] = 3
        self.assetEqual(d[self.d[[1,2]]], 3)
        d[[1,2,3]] = 4
        self.assetInequal(d[self.d[[1,2]]], 3)
        self.assetEqual(d[self.d[[1,2]]], 4)
        
