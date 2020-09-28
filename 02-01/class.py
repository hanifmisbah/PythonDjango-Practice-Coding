# property: ciri-ciri / hal yang dimiliki
# method / function: kemampuan, tugas, atau aktivitas yang akan dilakukan
# class: grup yg didalamnya terdapat atribut-atribut / bentuk abstrak / prototype
# inaharitance: penurunan dari class / sub-class

class Person:
	pass

class Person: 
	def say_hi(self):
		print('Hallo, wis madang durung???')

p = Person()
p.say_hi()

print(' ')
print('==========================')
print(' ')

class Person:
	def __init__(self, name): # sebagai inisiasi / method yang tidak perlu dipanggil
		self.name = name

	def say_hi(self):
		print('Hello, jenengku', self.name)

p = Person('Hamish')
p.say_hi()

print(' ')
print('==========================')
print(' ')

class Robot:
	population = 0

	def __init__(self, name): # init -> method berkerja pertama, 
		self.name = name
		print("(Initializing {})".format(self.name))

		Robot.population += 1

	def die(self): # self -> artinya untuk mengartikan dirinya sendiri
		print("{} is being destroyed!".format(self.name))

		Robot.population -= 1


		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(Robot.population))

	def say_hi(self):
		print("Greatings, my masters call me {}.".format(self.name))

	@classmethod
	def how_many(cls):
		print("We hve {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

print(' ')
print('==========================')
print(' ')

class SchoolMember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {}).'.format(self.name))

	def tell(self):
		print('Name:"{}" Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Initialized Teacher: {}).'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary:"{:d}"'.format(self.salary))	

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student: {}).'.format(self.name))
	
	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"{:d}"'.format(self.marks))	

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
	member.tell()