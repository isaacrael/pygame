class Book(object):
	''' Class for the Book object.
	'''

	def __init__(self, title="", author=""):
		''' Sets up a Book. title and author should be strings, but are
			not required.
		'''
		self.title = title
		self.author = author

	def __str__(self):
		''' Formatting for printing a book. Returns the following:
			{title} by {author}
			No further formatting is done, so if you want title style
			capitalization, do it yourself.
		'''
		return "{title} by {author}".format(title=self.title, author=self.author)
