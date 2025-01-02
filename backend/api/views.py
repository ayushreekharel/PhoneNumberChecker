from django.shortcuts import render
from django.http import JsonResponse
import json
from phonenumbers import geocoder,carrier
from django.views.decorators.csrf import csrf_exempt
from api.controller import NumberController
# Create your views here.
from api.models import Details

def get_input(request):
    
    if request.method=='GET':
        #data=json.loads(request.body)
        country=request.GET.get('country')
        print(country)
        phone_number=request.GET.get('number')
        print(phone_number)
        # if not Details.objects.filter(country=country,number=phone_number).exists():
        #     db=Details(country=country,number=phone_number)
        #     db.save()
        s1=NumberController()
        country,number_details=s1.getNumberDetails(country,phone_number)


        response_data = {
                'country': {
                    'name': country.name,
                    'alpha_2': country.alpha_2,
                    'alpha_3':country.alpha_3,
                    'official_name': country.official_name,
                },
                'phone_number_details': number_details,
            }
        print(response_data)
        return JsonResponse(response_data)
        
    else:
        return JsonResponse({'error':'Invalid request method'},status=405)