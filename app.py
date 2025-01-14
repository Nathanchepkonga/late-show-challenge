from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
##app.json.compact = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    # Use fully qualified path for the relationship
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            ## 'appearances': [appearance.to_dict() for appearance in self.appearances]  # Uncomment to include appearances
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    # Use fully qualified path for the relationship
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation,
          ##  'appearances': [appearance.to_dict() for appearance in self.appearances]  # Uncomment to include appearances
        }

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)

    # Relationships
    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    @db.validates('rating')
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5')
        return rating

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id,
            'episode': self.episode.to_dict(),
            'guest': self.guest.to_dict()
        }

#### 2. **Resources and Endpoints**

class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if episode is None:
            return {'error': 'Episode not found'}, 404
        return jsonify(episode.to_dict())

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()
        except ValueError as e:
            return {'errors': [str(e)]}, 400
        return jsonify(appearance.to_dict()), 201

#### 4. **Adding Resources to the API**

api.add_resource(EpisodeList, '/episodes')
api.add_resource(EpisodeDetail, '/episodes/<int:id>')
api.add_resource(GuestList, '/guests')
api.add_resource(AppearanceResource, '/appearances')

if __name__ == '__main__':
    app.run(debug=True)
