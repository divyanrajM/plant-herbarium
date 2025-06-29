from django.shortcuts import render, get_object_or_404
from .models import Plant, TherapeuticUse
from django.db.models import Q

def plant_list(request):
    query = request.GET.get("q")
    family = request.GET.get("family")
    therapeutic = request.GET.get("therapeutic")

    plants = Plant.objects.all()

    if query:
        plants = plants.filter(Q(name__icontains=query) | Q(scientific_name__icontains=query))

    if family:
        plants = plants.filter(family__icontains=family)

    if therapeutic:
        plants = plants.filter(therapeutic_uses__name__icontains=therapeutic)

    families = Plant.objects.values_list("family", flat=True).distinct()
    uses = TherapeuticUse.objects.all()

    return render(request, "plants/plant_list.html", {
        "plants": plants,
        "families": families,
        "uses": uses,
    })

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, "plants/plant_detail.html", {"plant": plant})
