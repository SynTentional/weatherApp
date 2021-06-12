from flask import Flask, render_template, request

import json

import urllib.request

app = Flask(__name__)

##########################################
#               Routes                  #
#########################################

@app.route('/', methods =['POST','GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default city oakland
        city = 'Oakland'

    api = '9a2693e4405c473fec33321dffd376cf'

    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial' + '&appid=' + api).read()
    # convert JSON data
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'f',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city),
    }
    print(data)

    # Allow anonymous users to input their mood
    # Corresponding to the weather

    return render_template('index.html', data = data)


if __name__ == '__main__':
    app.run(debug = True)