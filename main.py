from faker import Faker

fake = Faker()

print(fake.name(),
	fake.address(),
	fake.date_of_birth(minimum_age = 23),
	fake.city(),
	fake.job(),
	sep = "\n")
