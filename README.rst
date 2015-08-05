=================================================================
sqlitedict2 -- another persistent ``dict``, backed-up by SQLite and pickle
=================================================================

This is a fork of [sqlitedict](https://github.com/piskvorky/sqlitedict/)
The difference between the two projects is this use pickle.dumps(key) 
as the key, so both keys and values can be any picklable objects. 

Refer sqlitedict for steps of installation and usage.
