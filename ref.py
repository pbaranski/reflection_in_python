from pydoc import locate

my_class = locate('my_package.my_module.MyClass')


class Man:
    def __init__(self, *args):
        self._age = None
        self._namex = None
        self._surnamex = None
        self.set_values(*args)

    def set_values(self, *data):
        class_vars = sorted(list(vars(self).keys()))
        if data is not None:
            for collection in data:
                #if parameters are passed as arguments
                if type(collection) not in [list, dict] and len(class_vars) > 0:
                            setattr(self, class_vars.pop(0), collection)
                # check if parameter passed and are not empty collection
                elif collection is not None and len(collection) > 0:
                    if type(collection) == dict:
                        #data = dict with items for fields and values
                        for field, value in collection.items():
                            #for property (getters and setters)
                            field_prop = locate('ref.Man.{}'.format(field))
                            if type(field_prop) == property:
                                field_prop.__set__(self, value)
                            else:
                                #for plain functions
                                getattr(self, field)(value)
                    #if list is passed as first argument
                    elif type(collection) == list:
                        #values are assigned to class variables sorted alphabetically
                            dict_val = dict(zip(class_vars, collection))
                            for field, value in dict_val.items():
                                setattr(self, field, value)


    def name(self, value=None):
        if value is not None:
            self._namex = value
        return self._namex

    @property
    def surname(self):
        return self._surnamex

    @surname.setter
    def surname(self, value):
        self._surnamex = value


if __name__ == '__main__':
    man = Man({'name': 'jan', 'surname': 'nowak'})
    print(man.name())
    print(man.surname)
    man.name('adam')
    man.surname = 'kowalski'
    print(man.name())
    print(man.surname)