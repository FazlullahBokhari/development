from basic import db,Puppy

## Create ##
db.create_all()
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)
my_puppy = Puppy('Rufus',5)
db.session.add_all([sam,frank,my_puppy])
db.session.commit()

## Read ##
all_puppies = Puppy.query.all() # return a list of puppies objects in the table!
print(all_puppies)

# Select by # ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name,puppy_one.id,puppy_one.age)

# filter
# produce some sql code
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

## update

first_puppy = Puppy.query.get(1)
first_puppy.age = 15
db.session.add(first_puppy)
db.session.commit()


## Delete

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
