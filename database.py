from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize marshmallow
ma = Marshmallow(app)

# Project Datenbank
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    javascript = db.Column(db.Boolean(100))
    webdesign = db.Column(db.Boolean)
    textilarbeit = db.Column(db.Boolean)
    produktdesign = db.Column(db.Boolean)
    holzarbeit = db.Column(db.Boolean)
    druck = db.Column(db.Boolean)
    software = db.Column(db.Boolean)
    goldschmied = db.Column(db.Boolean)
    description = db.Column(db.String(200))

def __init__(self, name, email, javascript, webdesign, textilarbeit,
             produktdesign, holzarbeit, druck, software, goldschmied, description):
    self.name = name
    self.email = email
    self.javascript = javascript
    self.webdesign = webdesign
    self.textilarbeit = textilarbeit
    self.produktdesign = produktdesign
    self.holzarbeit = holzarbeit
    self.druck = druck
    self.software = software
    self.goldschmied = goldschmied
    self.description = description

# Project Schema
class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'javascript', 'webdesign', 'textilarbeit',
                  'produktdesign', 'holzarbeit', 'druck', 'software', 'goldschmied', 'description')

# Initialize project schema
product_schema = ProjectSchema()
products_schema = ProjectSchema(many=True)

#User Datenbank
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    javascript = db.Column(db.Boolean(100))
    webdesign = db.Column(db.Boolean)
    textilarbeit = db.Column(db.Boolean)
    produktdesign = db.Column(db.Boolean)
    holzarbeit = db.Column(db.Boolean)
    druck = db.Column(db.Boolean)
    software = db.Column(db.Boolean)
    goldschmied = db.Column(db.Boolean)

def __init__(self, name, email, javascript, webdesign, textilarbeit,
             produktdesign, holzarbeit, druck, software, goldschmied):
    self.name = name
    self.email = email
    self.javascript = javascript
    self.webdesign = webdesign
    self.textilarbeit = textilarbeit
    self.produktdesign = produktdesign
    self.holzarbeit = holzarbeit
    self.druck = druck
    self.software = software
    self.goldschmied = goldschmied

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'javascript', 'webdesign', 'textilarbeit',
                  'produktdesign', 'holzarbeit', 'druck', 'software', 'goldschmied')

# Initialize project schema
user_schema = UserSchema()
user_schema = UserSchema(many=True)




# GET, POST Methoden
# Methode um ein neues Projekt anzulegen
@app.route('/project', methods=['POST'])
def add_project():
    name = request.json['name']
    email = request.json['email']
    javascript = request.json['javascript']
    webdesign = request.json['webdesign']
    textilarbeit = request.json['textilarbeit']
    produktdesign = request.json['produktdesign']
    holzarbeit = request.json['holzarbeit']
    druck = request.json['druck']
    software = request.json['software']
    goldschmied = request.json['goldschmied']
    description = request.json['description']

    new_project = Product(name, email, javascript, webdesign, textilarbeit,
                          produktdesign, holzarbeit, druck, software, goldschmied, description)

    db.session.add(new_project)
    db.session.commit()

    return ProjectSchema.jsonify(new_project)

#Methode um einen neuen User anzulegen
@app.route('/anmelden', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    javascript = request.json['javascript']
    webdesign = request.json['webdesign']
    textilarbeit = request.json['textilarbeit']
    produktdesign = request.json['produktdesign']
    holzarbeit = request.json['holzarbeit']
    druck = request.json['druck']
    software = request.json['software']
    goldschmied = request.json['goldschmied']

    new_user = Product(name, email, javascript, webdesign, textilarbeit,
                          produktdesign, holzarbeit, druck, software, goldschmied)

    db.session.add(new_user)
    db.session.commit()

    return UserSchema.jsonify(new_user)