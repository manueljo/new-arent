from django.shortcuts import render,get_object_or_404
from .models import Areas,Apartment, Profile
import folium

# Create your views here.


def index(request):
    areas = Areas.objects.all()
    if request.method == 'POST':
        area = request.POST.get('area')
        apartment_area = Areas.objects.get(name=area)
        apartments = Apartment.objects.filter(area=apartment_area).values()
        cordinate = [apartment_area.location.latitude, apartment_area.location.longitude]
        folium_map = folium.Map(location=cordinate, zoom_start=14).add_child(folium.LatLngPopup())

        locate = []

        for apartment in apartments:
            point = apartment.get('location')
            locate.append(point.latitude)
            locate.append(point.longitude)
            # cordinates.append(locate)
            
            #https://room-locator-production.up.railway.app
            
            folium.Marker(locate, popup=f"<a href='/apartment/{apartment['id']}/' target='_blank'>View apartment</a><br> "+apartment['name'],tooltip='click me!!').add_to(folium_map)
            
            locate = []

        mapping = folium_map._repr_html_()
        
        context = {'mapping':mapping,'areas':areas}
        return render(request, "index.html#map-partial", context)

    context = {'areas':areas}
    return render(request, 'index.html', context)


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {'profile':profile}
    return render(request, 'profiles.html', context)


def apartment(request,pk):
    room_detail = Apartment.objects.get(id=pk)
    agent = Profile.objects.get(user=room_detail.agent)

    context = {'room':room_detail,'agent':agent}
    return render(request, "apartment.html", context)