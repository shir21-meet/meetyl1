'''
class dog(object):
	def __init__(self, name, age, favorite_food, color, sound ):
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
		self.color = color
	def eat(self, favorite_food):
		print (self.name + "is eating" +  favorite_food)
	def description (self):
		print (self.name + " is " + self.age + " years old and his favorite_food is " + self.favorite_food)
	def make_a_sound (self, sound):
		print ("bark ")*3
animal1 = dog("raxy", "5", "balogne", "brown", "bark")
animal1.eat (" balogne ")
animal1.description()
animal1.make_a_sound("bark ")
'''
class Person (object):
	def __init__(self, name, age, favorite_food, gender, city ):
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
		self.gender = gender
		self.city = city
	def eat(self, favorite_food):
		print (self.name + " is eating" +  favorite_food)

person1 = Person("roni", "26", "banna", "none", "tel-aviv")
person1.eat (" banna ")


		
		