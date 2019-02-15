

class Serializable:
    class Meta:
        schema = {}
        expose = ()
        exposeAs = {}
        exposeOptions = {}

    def __init__(self, json):
        self.read(json)

    def write(self):
        obj = {}
        primitives = [bytes, int, str, bool, dict, float]
        for name, _type in self.Meta.schema.items():
            if name[-1] == '?':
                name = name[:-1]
                if name not in dir(self) or not getattr(self, name):
                    continue
            elif name not in dir(self):
                raise MissingPropertyException(
                    "Property `{}` is not defined in the Object `{}`".format(
                        name, self.__class__.__name__,
                    ),
                )

            if type(_type) != list and type(_type) != set:
                if _type in primitives:
                    obj[name] = getattr(self, name)
                elif issubclass(_type, Serializable):
                    obj[name] = getattr(self, name).write()
                else:
                    raise Exception(
                        "Type `{}` cannot be serialized!".format(_type),
                    )

            elif type(_type) == list:
                if _type[0] in primitives or _type[0] == list:
                    obj[name] = getattr(self, name)
                elif issubclass(_type[0], Serializable):
                    obj[name] = [x.write() for x in getattr(self, name)]
                else:
                    raise Exception(
                        "Type `[{}]` cannot be serialized!".format(_type[0]),
                    )

            elif type(_type) == set:
                obj[name] = getattr(self, name)
                if not obj[name] in _type:
                    raise Exception(
                        "Value {} not allowed in the enum {}".format(
                            obj[name], _type,
                        ),
                    )
        return obj

    def _get_att_name(self, name):
        _name = self.Meta.exposeAs[name]
        if _name[0] != '$':
            return _name
        return self._get_att_composed(_name[1:].split('.'))

    def _get_att_composed(self, chain):
        name = getattr(self, chain.pop(0))
        while chain:
            name = getattr(name, chain.pop(0))
        return name

    def read(self, json):
        # primitives = [bytes, int, str, bool, dict]
        for name, _type in self.Meta.schema.items():
            if name[-1] == '?':
                name = name[:-1]
                if name not in json.keys():
                    continue
            elif name not in json.keys():
                raise MissingPropertyException(
                    "Property `{}` not found in {}".format(
                        name, self.__class__.__name__,
                    ),
                )

            if type(_type) != list:
                setattr(
                    self,
                    name,
                    self._create_attribute(_type, json[name]),
                )
            elif type(_type) == list:
                setattr(
                    self,
                    name,
                    [self._create_attribute(_type[0], x) for x in json[name]],
                )
        return self

    def _create_attribute(self, _type, value):
        primitives = [bytes, int, float, str, bool, dict, list]
        if value is None:
            return None
        if _type in primitives:
            return _type(value)
        if issubclass(_type, Serializable):
            return _type(value)
        raise Exception('Unknown attribute!')


class MissingPropertyException(Exception):
    pass
