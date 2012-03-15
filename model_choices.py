
class ModelChoices(object):

    """
        This is to be used for Django models choices parameters.
            >>> NUMBER_CHOICES = ModelChoices(              \
                (1, "One"),                                 \
                (2, "Two"),                                 \
                (3, "Three")                                \
            )

            >>> NUMBER_CHOICES = ModelChoices({             \
                1: "One",                                   \
                2: "Two",                                   \
                3: "Three"                                  \
            })

            >>> NUMBER_CHOICES = ModelChoices("Zero", "One", "Two", "Three")

        It supports iteration for Django
            >>> for x in NUMBER_CHOICES:
            ...     print x
            (0, 'Zero')
            (1, 'One')
            (2, 'Two')
            (3, 'Three')

        .. and easy lookup for developers.
            >>> NUMBER_CHOICES.One
            1
            >>> NUMBER_CHOICES[1]
            'One'

            >>> NUMBER_CHOICES.Two
            2
            >>> NUMBER_CHOICES[2]
            'Two'
    """

    def __init__(self, *args, **kwargs):
        self._choices = []
        self._choices_map = {}

        if len(args) == 1 and type(args[0]) is dict:
            for k, v in args[0].items():
                self.add_choice(k, v)
        else:
            for i, arg in enumerate(args):
                if type(arg) is str:
                    k = i
                    v = arg
                else:
                    k = arg[0]
                    v = arg[1]

                self.add_choice(k, v)

    def add_choice(self, k, v):
        setattr(self, v, k)
        self._choices.append((k, v))
        self._choices_map[k] = v

    def __iter__(self):
        return iter(self._choices)

    def __getitem__(self, key):
        return self._choices_map[key]


