from django.db import models


class Sex_options(models.TextChoices):
    Male = "Male"
    Female = "Female"
    Not_informed = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()

    sex = models.CharField(
        max_length=20, choices=Sex_options.choices, default=Sex_options.Not_informed
    )

    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT, related_name="pets"
    )
    traits = models.ManyToManyField("traits.Trait", related_name="pets")
