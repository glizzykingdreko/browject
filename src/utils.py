class Dict2Object:
    """
    @DynamicAttrs
    Class to transform a dict into a python object.
    """

    def __init__(self, in_dict: dict):
        assert isinstance(in_dict, dict)
        for key, val in in_dict.items():
            key = translate_string(key)
            if isinstance(val, (list, tuple, set)):
                setattr(
                    self,
                    key,
                    [Dict2Object(x) if isinstance(x, dict) else x for x in val],
                )
            else:
                setattr(self, key, Dict2Object(val) if isinstance(val, dict) else val)

    def __repr__(self):
        return "{%s}" % str(
            ", ".join("'%s': %s" % (k, repr(v)) for (k, v) in self.__dict__.items())
        )
    
    def to_dict(self):
        return self.__dict__


def translate_string(string: str) -> str:
    string = string.replace("-", "_")
    string = string.replace(" ", "_")
    return string
