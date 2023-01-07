
import shelve


class Storit(object):

    def __init__(self, store_name):
        self.store_name = store_name
        self._db = None

    def __setitem__(self, key, value):
        with shelve.open(self.store_name) as db:
            db[str(key)] = value

    def __getitem__(self, key):
        try:
            with shelve.open(self.store_name) as db:
                return db[str(key)]
        except(KeyError):
            return None

    def __delitem__(self, key):
        with shelve.open(self.store_name) as db:
            del db[str(key)]

    def __contains__(self, key):
        with shelve.open(self.store_name) as db:
            return str(key) in db

    def __enter__(self):
        self._db = shelve.open(self.store_name)
        return self._db

    def __exit__(self, type, value, traceback):
        if self._db:
            self._db.close()
            self._db = False

    def keys(self):
        with shelve.open(self.store_name) as db:
            return list(db.keys())

    def delete_if_exists(self, key):
        """Returns True if key existed, false otherwise"""
        with shelve.open(self.store_name) as db:
            if str(key) in db:
                del db[str(key)]
                return True
            return False


def _test():
    stor = Storit('subs')
    stor['yoda'] = 'do or do not, there is not try...'
    var = stor['yoda']
    print(var)
    for i in 'one two three four five'.split():
        stor[i] = 'data'
    print(stor.keys())
    if 'five' in stor:
        print('yesss')


if __name__ == '__main__':
    _test()
