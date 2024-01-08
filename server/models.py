from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

#  -add a new model class named Earthquake that inherits
    #from both db.Model and SerializerMixin
#  -A string named __tablename__ assigned to the value "earthquakes"
#  -A column named id to store an int that is the primary key
#  -A column named magnitude to store a float
#  -A column named location to store a string
#  -A column named year to store an int
#  -A __repr__ method to return a string that formats the attributes id, magnitude, location, and year as a comma-separated sequence as shown:
#       <Earthquake 1, 9.5, Chile, 1960>
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}'
