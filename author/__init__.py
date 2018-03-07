class Elem:
	def __init__(self, name, options):
		self.name = name
		self.options = options

	def set(self, key, value):
		for i in range(len(self.options)):
			k, _ = self.options[i]
			if k == key:
				self.options[i] = (key, value)

	def toString(self, depth=0):
		s = "\t"*depth + self.name
		for k, v in self.options:
			if k:
				s += " -" + k
			if v:
				if not isinstance(v, list):
					v = [v]
				s += " {"
				lastIsElem = False
				for w in v:
					if isinstance(w, Elem):
						lastIsElem = True
						s += "\n" + w.toString(depth+1)
					else:
						lastIsElem = False
						s += str(w)
				if lastIsElem:
					s += "\n" + "\t"*depth
				s += "}"
		return s

def Job(options):
	return Elem("Job", options)

def Task(options):
	return Elem("Task", options)

def RemoteCmd(options):
	return Elem("RemoteCmd", options)

