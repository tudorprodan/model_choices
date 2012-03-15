```python

# can be defined as a tuple
NUMBER_CHOICES = ModelChoices(
    (1, "One"),
    (2, "Two"),
    (3, "Three")
)

# as a dict
NUMBER_CHOICES = ModelChoices({
    1: "One",
    2: "Two",
    3: "Three"
})

# list
NUMBER_CHOICES = ModelChoices("Zero", "One", "Two", "Three")

"""
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

```
