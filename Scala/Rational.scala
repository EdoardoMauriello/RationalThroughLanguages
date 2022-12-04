class Rational(x:Int,y:Int){
	val den=y
	val num=x
	
	override def toString:String=
		if(y==1) x.toString else x + "/" +y
		
	def +(that:Rational):Rational=
		new Rational(this.num*that.den+that.num*this.den, this.den*that.den)
		
	def ++():Rational=
		this + new Rational(1,1)
		
	def -(that:Rational):Rational=
		new Rational(this.num*that.den-that.num*this.den, this.den*that.den)
		
	def unary_-():Rational=
		new Rational(-num,den)
}