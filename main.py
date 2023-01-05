import csv
import requests
from faker import Faker
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/generate-users/<int:num>')
def generate(num):
    result = {}
    fake = Faker()
    for _ in range(num):
        name = fake.name()
        mail = f"{name.replace(' ', '.').lower()}@example.net"
        result[name] = mail
    return result


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        f = file.read()
    return f


@app.route('/mean/')
def mean():
    with open('hw.csv') as f:
        result = {}
        reader = csv.reader(f)
        headers = next(reader)
        i = h = w = 0
        for row in reader:
            if row:
                h += float(row[1])
                w += float(row[2])
                i = int(row[0])
        result[headers[1].replace('Inches', 'cm')] = round(h / i * 2.54, 2)
        result[headers[2].replace('Pounds', 'kg')] = round(w / i * 0.453592, 2)
    return f"Средний рост и средний вес с выборки {i} человек - {result}"


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    result = r.json()
    return f"Количество космонавтов в настоящий момент - {result['number']}"


if __name__ == "__main__":
    app.run()
