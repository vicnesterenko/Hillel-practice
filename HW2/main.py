import requests
from flask import Flask, request
from faker import Faker
import os

app = Flask(__name__)
fake = Faker()


@app.route('/requirements/')
def read_requirements():
    file_path = 'requirements.txt'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            requirements_content = file.read()
        return requirements_content
    else:
        return 'File not found'


@app.route('/generate-users/')
def generate_users():
    user_count = int(request.args.get('count', 100))

    users = []
    for _ in range(user_count):
        user = {
            'email': fake.email(),
            'name': fake.name()
        }
        users.append(user)

    return {'users': users}


@app.route('/space/')
def get_astronaut_count():
    url = 'http://api.open-notify.org/astros.json'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        astronaut_count = data['number']
        return f'Count of cosmonauts: {astronaut_count}'
    else:
        return 'Failed got data'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
