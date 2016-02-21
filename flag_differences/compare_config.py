'''
Author: King Mui
Date: Feb 21, 2016

Specifications:
	This script will compare two configuration files and spit out a difference.txt file that contains the same flag but with different values.

Note to self:
	get_similar_flags(self, precedence) takes either "ecm" or "custom". This will determine the precedence in the differences.txt output.

How to use?! ORDER MATTERS FOLKS: 
	python compare_config.py ecm_properties custom_properties

Questions?
	Sametime King Mui or email him. 

'''
import sys
ecm = [line[:-1] for line in open(sys.argv[1], "r+")]
custom = [line[:-1] for line in open(sys.argv[2], "r+")]
differences = open("differences.txt", "w")

class Parser(object):
	def __init__(self, ecm_properties, custom_properties):
		self.ecm_properties = ecm_properties
		self.custom_properties = custom_properties
		self.output_properties = []

	def create_dictionary(self, argv):
		intermediate_dictionary = {}
		for line in argv:
			equal_flag = False
			index = 0
			for i in line:
				if i == "=":
					equal_flag = True
					index = line.index('=')
			if equal_flag:
				intermediate_dictionary[line[0:index]] = line[index+1:].rstrip().lower()
		return intermediate_dictionary

	#precedence is whether we want the value from ecm.properties or custom.properties
	def get_similarflags(self, precedence):
		self.ecm_dictionary = self.create_dictionary(self.ecm_properties)
		self.custom_dictionary = self.create_dictionary(self.custom_properties)
		for custom_key in self.custom_dictionary:
			for ecm_key in self.ecm_dictionary: 
				if custom_key == ecm_key:
					if self.ecm_dictionary[ecm_key] != self.custom_dictionary[custom_key]:
						if precedence == "ecm":
							self.output_properties.append(ecm_key + "=" + self.ecm_dictionary[ecm_key])
						if precedence == "custom":
							self.output_properties.append(custom_key + "=" + self.custom_dictionary[custom_key])

	def create_differencefile(self, precedence):
		self.get_similarflags(precedence)
		for line in self.output_properties:
			with open("differences.txt", "a") as differences:
				differences.write(line + "\n")
#Order Matters
foo = Parser(ecm, custom)
foo.create_differencefile('ecm')
differences.close()
