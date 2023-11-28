from django.shortcuts import render,get_object_or_404
from .models import Areas,Apartment, Profile
import folium
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

@csrf_exempt
def ussd(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        agent = Profile.objects.filter(pk=1).values()

        response = ""

        if text == "":
            response = "CON Select area to find agent \n"
            # response .= "1. My Account \n"
            response += "1. Ikeja"
            response += "2. Ikorodu"
            response += "3. Agege"

        elif text == "1":
            response = "CON Agents in Ikeja \n"
            response = f"1. {agent[0].get('first_name')} {agent[0].get('last_name')}"

        elif text == "1*1":
            response = f"END My Phone number is {agent[0].get('mobile_number')}"

        elif text == "2":
            response = "CON Agents in Ikorodu \n"
            response = f"1. {agent[0].get('first_name')} {agent[0].get('last_name')}"

        elif text == "1*2":
            response = f"END My Phone number is {agent[0].get('mobile_number')}"

        elif text == "3":
            response = "CON Agents in Ikorodu \n"
            response = f"1. {agent[0].get('first_name')} {agent[0].get('last_name')}"

        elif text == "1*3":
            response = f"END My Phone number is {agent[0].get('mobile_number')}"

        return HttpResponse(response)


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
