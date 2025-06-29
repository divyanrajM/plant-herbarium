from django.db import models
class TherapeuticUse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Compound(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    smiles = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)
    family = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plants/')
    description = models.TextField()

    # ✅ This makes it pull data from DB
    therapeutic_uses = models.ManyToManyField(TherapeuticUse, blank=True)
    active_compounds = models.ManyToManyField(Compound, blank=True)

    def __str__(self):
        return self.name
