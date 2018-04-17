class Database():
	def __init__(self,username,msg):
		self.username = username
		self.msg = msg

class Store():
	Data = []
	def __init__(self,data):
		self.data = data
		return self.Data.append(self.data)
	def getall(self):
		return self.Data
