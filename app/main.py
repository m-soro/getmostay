from flask import Flask, render_template, url_for, flash
from app.get_mostay import get_mostay
from app.combine_images import combine_images
from app.get_hotel_selection import get_hotel_selection
from app.get_signature_fan import get_signature_fan
from selenium.common.exceptions import StaleElementReferenceException
import os.path
import glob
import os

app = Flask(__name__)

app.secret_key = '87e4ge839562141xfar0jpj'

@app.route('/')
def home_view():
    fan = get_signature_fan()
    return render_template('home.html', fan=fan)

@app.route('/results', methods=['GET', 'POST'])
def results():

    path='app/static/imgs/'

    if os.path.exists(path+'mo_stay.png'):
        os.remove(path+'mo_stay.png')
        print('\nPrevious result is deleted !\n')

    my_hotel_selection = get_hotel_selection()

    try:
        for hotel_location,hotel_code in my_hotel_selection.items():
            get_mostay(hotel_location,hotel_code)
            combine_images([path+'1.png',path+'2.png',path+'3.png'], path +'mo_'+ hotel_location +'.png',hotel_location)
            combine_images([path+hotel_location+'_image.png',path +'mo_'+ hotel_location +'.png'], path + 'mo_' + hotel_location +'.png',hotel_location)

    except StaleElementReferenceException:
        print(f'Error retrieving ** {hotel_location} ** page has not loaded before taking screenshot. Please try again')
        flash(f'\n\nError retrieving ** {hotel_location} ** page has not loaded before taking screenshot. Please try again')

    try:
        combine_images(glob.glob(path+'mo_*.png'),path+'mo_stay.png',stack='v')

    except ValueError:
        print('\n   No results, please try again !\n')
        flash('No results, please try again !')


    calendar = '/static/imgs/mo_stay.png'

    return render_template('results.html', calendar=calendar)
