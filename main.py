import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from forms import currencies_list, currencies_list2
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APPKEY')
Bootstrap5(app)

api_key = os.environ.get('API_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    answer = '-'
    default = 0
    if request.method == 'POST':
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{request.form.get("curr")}/{request.form.get("curr_conversion")}/{float(request.form.get("amount"))}'
        response = requests.get(url)
        answer = response.json()['conversion_result']
        rate = response.json()['conversion_rate']
        default = request.form.get("amount")
        if request.form.get("curr") in currencies_list:
            currencies_list.remove(request.form.get('curr'))
        currencies_list.insert(0, request.form.get("curr"))

        if request.form.get("curr_conversion") in currencies_list2:
            currencies_list2.remove(request.form.get('curr_conversion'))
        currencies_list2.insert(0, request.form.get("curr_conversion"))
        return render_template('index.html', currencies_list=currencies_list, currencies_list2=currencies_list2, answer=answer, default=default, rate=rate)
    return render_template('index.html', currencies_list=currencies_list, currencies_list2=currencies_list2, answer=answer, default=default)


if __name__ == "__main__":
    app.run(debug=True)
