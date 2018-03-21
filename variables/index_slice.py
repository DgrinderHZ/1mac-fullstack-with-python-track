"""
indexing : <string>[index]
index = ..., -1, 0, 1, ...

slicing/selecting : <string>[start : end]

"""
my_string = "DgrinderHZ"

print my_string[0]
print my_string[-1]

hz = my_string[-2:]

print hz

def udacity(my_string):
	""" returns Udacity """
	return "U" + my_string[2:]

my_string = "audacity"

print udacity(my_string)