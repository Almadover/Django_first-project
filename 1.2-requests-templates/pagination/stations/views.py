from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

# with open(, newline='', encoding='utf-8') as f:
#     stantions = []
#     for row in csv.DictReader(f):
#         stantions.append({'Name': row.get('Name'), 'Street': row.get('Street'), 'District': row.get('District') })
#     print(stantions)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        list_data = [item for item in reader]

    page_number = int(request.GET.get('page', 1))

    paginator = Paginator(list_data, 10)
    page = paginator.get_page(page_number)
    bus_stations = page.object_list

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
