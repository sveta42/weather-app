from flask import Flask, render_template, request, Response, redirect, url_for
from main import findcitylines
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
   if request.method == "POST":
      city = request.form.get('city')
      daily_temp = findcitylines(city)
      return render_template('forecast.html', daily_temp=daily_temp, city=city)
   return render_template('home.html')


if __name__ == '__main__':
   app.run()
