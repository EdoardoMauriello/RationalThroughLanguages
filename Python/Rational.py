class Rational:
	## Constructor
	def __init__(self, x:int,y:int):
		self.x = x
		self.y = y

	## Default string representation
	# @return string representation of the rational number
	# @note This is called when you print the object
	def __str__(self):
		return f"{self.x}/{self.y}"

	## Simplify the rational number
	# @return simplified rational number
	def simplify(x:int, y:int):
		gcd = gcd(x,y)
		if gcd != 1:
			return Rational(x/gcd, y/gcd)

	def simplify(self):
		gcd = self.gcd(self.x, self.y)
		if gcd != 1:
			return Rational(self.x/gcd, self.y/gcd)

	def gcd(a:int, b:int):
		while(b):
			a, b = b, a % b
		return abs(a)

	def __add__(self, that):
		return Rational(self.x*that.y+self.y+that.x, self.y*that.y)

	def __sub__(self, that):
		return Rational(self.x*that.y-self.y+that.x, self.y*that.y)

	def __mul__(self, that):
		return Rational(self.x*that.x, self.y*that.y)
