class DiGraph:
	def __init__(self):
		self.items = []
		
	def add_item(self,data):
		self.items.append(data)
	
	def dict2item_str(self,data):
		txt = ""
		txt += data["name"] + "["
		if "shape" in data:
			txt += "shape=" + data["shape"] +","
		txt += "pos=\"%d,%d!\"" % (data["x"],data["y"])
		txt += "];"
		return txt
	
	def draw(self):
		txt = "digraph xxx {"
		for i in self.items:
			txt += self.dict2item_str(i)

		txt += "}"
		return txt


g = """
digraph graph_name {
	XXX
}

"""

def dot(txt):
	print(g.replace("XXX",txt))


