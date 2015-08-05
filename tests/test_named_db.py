# std import
import tempfile
import unittest

# local
import sqlitedict2
from test_temp_db import TempSqliteDictTest
from test_core import TestCaseBackport
from accessories import norm_file


class InMemorySqliteDictTest(TempSqliteDictTest):

    def setUp(self):
        self.d = sqlitedict2.SqliteDict(filename=':memory:', autocommit=True)

    def tearDown(self):
        self.d.terminate()


class NamedSqliteDictTest(TempSqliteDictTest):

    def setUp(self):
        db = norm_file('tests/db/sqlitedict2-with-def.sqlite')
        self.d = sqlitedict2.SqliteDict(filename=db)


class CreateNewSqliteDictTest(TempSqliteDictTest):

    def setUp(self):
        db = norm_file('tests/db/sqlitedict2-with-n-flag.sqlite')
        self.d = sqlitedict2.SqliteDict(filename=db, flag="n")

    def tearDown(self):
        self.d.terminate()


class StartsWithEmptySqliteDictTest(TempSqliteDictTest):

    def setUp(self):
        db = norm_file('tests/db/sqlitedict2-with-w-flag.sqlite')
        self.d = sqlitedict2.SqliteDict(filename=db, flag="w")

    def tearDown(self):
        self.d.terminate()



class SqliteDictAutocommitTest(TempSqliteDictTest):

    def setUp(self):
        db = norm_file('tests/db/sqlitedict2-autocommit.sqlite')
        self.d = sqlitedict2.SqliteDict(filename=db, autocommit=True)

    def tearDown(self):
        self.d.terminate()
