# coding: utf8

response.static_version = '1.0.0'

# This populates the creature type table with the basic types required for the engine to run a game if they do not already exist. You can comment this once they exist.
#if db(db.creature_type.id > 0).count() == 0:
#   db.creature_type.insert(cid=1, zombie=False, name="Human", immortal=False)
#   db.creature_type.insert(cid=2, zombie=True, name="Zombie", immortal=False)
#   db.creature_type.insert(cid=3, zombie=True, name="Original Zombie", immortal=True)