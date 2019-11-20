class User():	
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = []
		self.posts = []
	def add_friends(self, email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friends ")
	def remove_friends(self, email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " as a friends ")
	def post(self,text):
		self.posts.append(text)
		print(self.name + " has postsed : " + text)
	def get_userInfo(self):
		print(" name: " + str(self.name))
		print(" email: " + str(self.email))
		print(" password: " + str(self.password))
		print("friends: " + str(self.friends_list))
		print(" posts: " + str(self.posts))

User1= User("Shir", "shir15@meet.mit.edu" , "shir1234")
User2= User("Yousef", "Yousef15@meet.mit.edu", "Yousef1234" )
User1.add_friends("Yousef15@meet.mit.edu")
User2.post("hi shir")
User1.get_userInfo()
