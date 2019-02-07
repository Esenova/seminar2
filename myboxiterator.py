class MyBoxIterator(object):
	def __init__(self, arg):
		super(MyBoxIterator, self).__init__()
		self.arg = arg
		
	def __iter__(self):
		return self
	
	def __next__(self):
		return self.arg