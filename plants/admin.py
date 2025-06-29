from django.contrib import admin
from .models import Plant, TherapeuticUse, Compound

# Customize display for Plant
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'family')
    search_fields = ('name', 'scientific_name', 'family')
    list_filter = ('family', 'therapeutic_uses', 'active_compounds')
    filter_horizontal = ('therapeutic_uses', 'active_compounds')
    ordering = ['name']

# Display TherapeuticUse
@admin.register(TherapeuticUse)
class TherapeuticUseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Display Compound
@admin.register(Compound)
class CompoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'smiles')
    search_fields = ('name',)
