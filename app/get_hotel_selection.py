from app.mandarin_locations import mo_dict
from flask import request

def get_hotel_selection():
    hotel_location = request.form['hotel_location']
    hotel_location = hotel_location.replace(" ",'').title().split(',')
    hotel_location = [key for key,val in mo_dict.items() for hotel in hotel_location if hotel in key]
    hotel_code = [val for key,val in mo_dict.items() for hotel in hotel_location if hotel in key]
    my_hotel_selection = dict(zip(hotel_location, hotel_code))
    print( 'Your selected hotels: ',list(my_hotel_selection.keys()) )
    return my_hotel_selection
