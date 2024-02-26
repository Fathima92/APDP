# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):
		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""
	def localize(self, msg):
		return msg

class TamilLocalizar:
	def __init__(self):
		self.translations = {"car": "ஊர்தி", "bike": "இரு சக்கர வண்டி",
							"cycle":"மிதிவண்டி"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

def Factory(language ="English"):

	"""Factory Method"""
	localizers = {
		"French": FrenchLocalizer,
		"English": EnglishLocalizer,
		"Spanish": SpanishLocalizer,
		"Tamil": TamilLocalizar,

	}

	return localizers[language]()

if __name__ == "__main__":

	f = Factory("French")
	e = Factory("English")
	s = Factory("Spanish")
	t = Factory("Tamil")

	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
		print(t.localize(msg))
