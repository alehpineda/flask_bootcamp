from crud_basics import db, Puppy

# read
all_puppies = Puppy.query.all()
print(all_puppies)

# by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filters
puppy_lluvia = Puppy.query.filter_by(name='Lluvia')
# produce some sql code,
# the all() returns the __repr__ in a list
print(puppy_lluvia.all())
print(puppy_lluvia.all()[0])


# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

puppy_one = Puppy.query.get(1)
print(puppy_one.name, puppy_one.age)


# delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)
