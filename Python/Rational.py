class Rational:
	def __init__(self, x:int,y:int):
		self.x = x
		self.y = y

	def __str__(self):
		return f"{self.x}/{self.y}"

	def simplify(x:int, y:int):
		gcd = gcd(x,y)
		if gcd != 1:
			return Rational(x/gcd, y/gcd)			

	def gcd(a:int, b:int):
		while(y):
			x, y = y, x % y
		return abs(x)

	def __add__(self, that):
		return Rational(self.x*that.y+self.y+that.x, self.y*that.y)

	def __sub__(self, that):
		return Rational(self.x*that.y-self.y+that.x, self.y*that.y)

	def __mul__(self, that):
		return Rational(self.x*that.x, self.y*that.y)
