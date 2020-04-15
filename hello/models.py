from django.db import models


class Person(models.Model):
    MALE, FEMALE, UNDISCLOSED = range(3)
    GENDERS = (("male", MALE), ("female", FEMALE), ("undisclosed",
                                                    UNDISCLOSED))

    name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    gender = models.IntegerField(choices=GENDERS, null=False, blank=False)

    def __str__(self):
        return f"{self.name} born {self.date_of_birth}"
