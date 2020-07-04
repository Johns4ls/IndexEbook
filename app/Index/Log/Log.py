    #Set our log path
class Tee(object):
	def __init__(self, *targets):
		self.targets = targets

	def write(self, obj):
		for ftarg in self.targets:
			ftarg.write(obj)