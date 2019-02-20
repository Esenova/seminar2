from myboxiterator import MyBoxIterator

class MyBox(object):
	def __init__(self, plov):
		self.plov = plov

	def get_len(self):
		return len(self.plov)

	def add(self, object):
		self.plov.append(object)
		return self.plov

	def remove(self, object):
		self.plov.remove(object)
		return self.plov

	def contains(self, object):
		if object in self.plov:
			return True
		else:
			return False

    	def __iter__(self, object):
		return MyBoxIterator(self.plov)
