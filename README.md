# Django ModelChoices helper

Should be used like so:

```python

class MyStagedModel(models.Model):

    # Can be initialized with a tuple
    NUMBER_CHOICES = ModelChoices(
        (1, "One"),
        (2, "Two"),
        (3, "Three")
    )

    # with a dict
    NUMBER_CHOICES = ModelChoices({
        1: "One",
        2: "Two",
        3: "Three"
    })

    # with a list
    NUMBER_CHOICES = ModelChoices("Zero", "One", "Two", "Three")

    number_status = models.IntegerField(choices=NUMBER_CHOICES, default=NUMBER_CHOICES.Zero)

    def __unicode__(self):
        return "<MyStagedModel object in status: %s>" % NUMBER_CHOICES[self.number_status]


msm = MyStagedModel.objects.get(pk=some_id)
msm.number_status = MyStagedModel.NUMBER_CHOICES.Three
msm.save()

print msm
# would print:
"<MyStagedModel object in status: Three>"

```

### It supports

```python
"""
    iteration for Django
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

