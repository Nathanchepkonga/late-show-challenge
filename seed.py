# seed.py

from app import db, Episode, Guest, Appearance

# Drop all tables and create new ones (This will delete all data - use with caution)
db.drop_all()
db.create_all()

# Creating Episode entries
episode1 = Episode(date="2024-10-20", number=1)
episode2 = Episode(date="2024-10-21", number=2)
episode3 = Episode(date="2024-10-22", number=3)

# Adding Episode entries to the session
db.session.add_all([episode1, episode2, episode3])

# Creating Guest entries
guest1 = Guest(name="Nathan Chepkonga", occupation="Software Developer")
guest2 = Guest(name="Jane Doe", occupation="Data Scientist")
guest3 = Guest(name="John Smith", occupation="Product Manager")

# Adding Guest entries to the session
db.session.add_all([guest1, guest2, guest3])

# Committing the initial Episode and Guest entries to the database
db.session.commit()

# Creating Appearance entries
appearance1 = Appearance(rating=5, episode_id=episode1.id, guest_id=guest1.id)
appearance2 = Appearance(rating=4, episode_id=episode2.id, guest_id=guest2.id)
appearance3 = Appearance(rating=3, episode_id=episode3.id, guest_id=guest3.id)

# Adding Appearance entries to the session
db.session.add_all([appearance1, appearance2, appearance3])

# Committing the Appearance entries to the database
db.session.commit()

print("Database seeded successfully!")
