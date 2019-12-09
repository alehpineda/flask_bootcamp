# create entries in the db

from models import db, Puppy, Owner, Toy

# creting two puppies

lluvia = Puppy('Lluvia')
travieso = Puppy('Travieso')

# add puppies to db
db.session.add_all([lluvia, travieso])
db.session.commit()

# check
print(Puppy.query.all())

lluvia = Puppy.query.filter_by(name='Lluvia').first()
travieso = Puppy.query.filter_by(name='Travieso').first()

#Create owner object
alex = Owner('Alex', lluvia.id)
ale = Owner('Ale', travieso.id)

# give lluvia some toys
toy1 = Toy('Chew Toy', lluvia.id)
toy2 = Toy('Ball', lluvia.id)

# give travieso some toys
toy3 = Toy('Chew Toy', travieso.id)
toy4 = Toy('Ball', travieso.id)

db.session.add_all([alex, ale, toy1, toy2, toy3, toy4])
db.session.commit()


# grab lluvia and travieso

lluvia = Puppy.query.filter_by(name='Lluvia').first()
travieso = Puppy.query.filter_by(name='Travieso').first()

print(lluvia)
print(lluvia.report_toys())
print(travieso)
print(travieso.report_toys())