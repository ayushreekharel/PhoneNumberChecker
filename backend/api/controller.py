import phonenumbers
import pycountry
from phonenumbers import geocoder,carrier
from api.models import Details

class NumberController:
    def __init__(self):
        pass
    def getNumberDetails(self,country,phoneNumber):
        if not Details.objects.filter(country=country,number=phoneNumber).exists():
            db=Details(country=country,number=phoneNumber)
            db.save()
        if not country or not phoneNumber : return False
        country=pycountry.countries.get(alpha_2=country.upper()) or pycountry.countries.get(alpha_3=country.upper()) or pycountry.countries.get(name=country)
        
        parsed_number=phonenumbers.parse(phoneNumber,country.alpha_2)
        print('-----')
        print(parsed_number)
        number_details={
            'is_valid': phonenumbers.is_valid_number(parsed_number),
            'is_possible':phonenumbers.is_possible_number(parsed_number),
            'type':phonenumbers.number_type(parsed_number),
            'region_code':phonenumbers.region_code_for_number(parsed_number),
            'international_format':phonenumbers.format_number(parsed_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            'national_format':phonenumbers.format_number(parsed_number,phonenumbers.PhoneNumberFormat.NATIONAL),
            'description_for_number':geocoder.description_for_number(parsed_number,'en'),
            'carrier':carrier.name_for_number(parsed_number,'en'),
            #'metadata':phonenumbers._get_metadata_for_region(country.alpha_2)
        }
        return country,number_details