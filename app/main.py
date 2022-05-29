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
    # get random signature fan and store the url and fan destination name in a file
    fan = get_signature_fan()
    with open('app/static/answer.txt', 'w') as f:
        f.write(str(fan))
    # return home page with random fan image
    return render_template('home.html', fan_image=fan[0])

@app.route('/results', methods=['GET', 'POST'])
def results():

    path='app/static/imgs/'

    # remove previous results if any
    if os.path.exists(path+'mo_stay.png'):
        os.remove(path+'mo_stay.png')
        print('\nPrevious result is deleted !\n')

    # run function to get hotel selections
    my_hotel_selection = get_hotel_selection()

    # retrieve the fan url and destination name
    with open('app/static/answer.txt', 'r') as f:
        fan_file = f.read()
        fan_file = fan_file.split(",")
        fan_answer = fan_file[1].replace("')", '').replace("'",'').replace('-',' ').title()
        fan_image = fan_file[0].replace("('", '').replace("'",'')

    # if hotel selection is not empty
    if my_hotel_selection:
        try:
            for hotel_location,hotel_code in my_hotel_selection.items():
                get_mostay(hotel_location,hotel_code)
                combine_images([path+'1.png',path+'2.png',path+'3.png'], path +'mo_'+ hotel_location +'.png',hotel_location)
                combine_images([path+hotel_location+'_image.png',path +'mo_'+ hotel_location +'.png'], path + 'mo_' + hotel_location +'.png',hotel_location)
                combine_images(glob.glob(path+'mo_*.png'),path+'mo_stay.png',stack='v')

                calendar = '/static/imgs/mo_stay.png'

                return render_template('results.html', calendar=calendar, answer=fan_answer, image=fan_image)

        # if page is not available before scraping
        except StaleElementReferenceException:
            print(f'\n\nError retrieving ** {hotel_location} ** page has not loaded before taking screenshot. Please try again\n\n')
            flash(f'Error retrieving ** {hotel_location} ** page has not loaded before taking screenshot. Please try again')

        return render_template('no-results.html', answer=fan_answer, image=fan_image)

    # if location is invalid    
    else:
        flash('Requested destination is not valid. Please check the spelling or refer to Mandarin Oriental locations.')
        return render_template('no-results.html', answer=fan_answer, image=fan_image)
