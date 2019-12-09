from crud_basics import db, Puppy

# create all the tables from model
db.create_all()

sam = Puppy('Sammy', 3)
rufus = Puppy('Rufus', 2)
lluvia = Puppy('Lluvia', 7)
travieso = Puppy('Travieso', 5)

print(lluvia.id)
print(travieso.id)

db.session.add_all([sam, rufus, lluvia, travieso])

db.session.commit()

print(lluvia.id)
print(travieso.id)
