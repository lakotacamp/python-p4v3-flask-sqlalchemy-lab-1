# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# -add a view that takes one parameter, an integer that
#  represents an id
# -The route should have the form /earthquakes/<int:id>
# -The view should query the database to get the earthquake
#  with that id, and return a response containing the model
#  attributes and values (id, location, maginutde, year)
#  formatted as an JSON string.
# -The response should include an error message if no row is
#  found.

@app.route('/earthquakes/<int:id>')
def earthquakes_by_id(id):
    earthquakes = Earthquake.query.filter(Earthquake.id == id).first()

    if earthquakes:
        body = earthquakes.to_dict()
        status = 200
    else:
        body = {'message': f'Earthquake {id} not found.'}
        status = 404
    return make_response(body,status)

# -add a view that takes one parameter, a float that represents a magnitude
# -The route should have the form /earthquakes/magnitude/<float:magnitude>.
# -The view should query the database to get all earthquakes having a magnitude
#  greater than or equal to the parameter value, and return a JSON response 
#  containing the count of matching rows along with a list containing the data for each row.

@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquakes_by_magnitude(magnitude):
    earthquake = []
    for quake in Earthquake.query.filter(Earthquake.magnitude >= magnitude).all():
        earthquake.append(quake.to_dict())
    body = {'count':len(earthquake),
            'quakes':earthquake
    }
    status = 200
    return make_response(body, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
