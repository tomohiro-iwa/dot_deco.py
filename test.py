import dot


lstm = """
%s [
	shape = box,
	width = 1,
	height = 1,
	pos = "%d,%d!"
];
"""

word = """
%s [
	shape = plaintext,
	width = 0.5,
	height = 1,
	pos = "%d,%d!"
];
"""

oper =  """
%s [
	shape = ellipse,
	width = 1,
	height = 1,
	pos = "%d,%d!"
];
"""

g = ""

g += word % ("word00", 100, 500)
g += word % ("word01", 200, 500)
g += word % ("word02", 300, 500)
g += lstm % ("encoder00",  100,400 )
g += lstm % ("encoder01",  200,400 )
g += lstm % ("encoder02",  300,400 )
g += "encoder00 -> encoder01 \n"
g += "encoder01 -> encoder02 \n"
g += "word00 -> encoder00 \n"
g += "word01 -> encoder01 \n"
g += "word02 -> encoder02 \n"

g += word % ("word10", 100, 300)
g += word % ("word11", 200, 300)
g += word % ("word12", 300, 300)
g += lstm % ("encoder10",  100,200 )
g += lstm % ("encoder11",  200,200 )
g += lstm % ("encoder12",  300,200 )
g += "encoder10 -> encoder11 \n"
g += "encoder11 -> encoder12 \n"
g += "word10 -> encoder10 \n"
g += "word11 -> encoder11 \n"
g += "word12 -> encoder12 \n"


g += oper % ("concat", 400,300)
g+= "encoder02 -> concat \n"
g+= "encoder12 -> concat \n"
g+= "concat -> decoder0 \n"

g += word % ("word0", 400, 0)
g += word % ("word1", 300, 0)
g += word % ("word2", 200, 0)
g += lstm % ("decoder0", 400,  100)
g += lstm % ("decoder1", 300,  100)
g += lstm % ("decoder2", 200,  100)
g += "decoder0 -> decoder1 \n"
g += "decoder1 -> decoder2 \n"
g += "decoder0 -> word0 \n"
g += "decoder1 -> word1 \n"
g += "decoder2 -> word2 \n"

dot.dot(g)
