# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class UnitAttribute(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)
		
	def asDict(self):
		data = {
			"resourceName"			: self[0],
			"UV"			: self[1],
			"ascription"		: self[2],
			"higth"			: self[3],
			"maxHP"			: self[4],
            "speed"			: self[5],
            "moveLenth"			: self[6],
            "attackType"			: self[7],
            "attackStandard"			: self[8],
            "attackDeviation"			: self[9],
            "longRange"			: self[10],
            "longRangeStandrad"			: self[11],
            "longRangeDeviation"			: self[12],
            "attackTypeName"			: self[13],
            "defense"			: self[14],
            "magicDefense"			: self[15],
            "luck"			: self[16],
            "speedCount"			: self[17],
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["resourceName"], dictData["UV"], dictData["ascription"], dictData["higth"], dictData["maxHP"], dictData["speed"], dictData["moveLenth"], dictData["attackType"], dictData["attackStandard"], dictData["attackDeviation"], dictData["longRange"], dictData["longRangeStandrad"], dictData["longRangeDeviation"], dictData["attackTypeName"], dictData["defense"], dictData["magicDefense"], dictData["luck"], dictData["speedCount"]])
		return self
		
class UnitAttributePickler:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return UnitAttribute().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, UnitAttribute)

unit_attribute_inst = UnitAttributePickler()

class UnitAttributeList(dict):
	"""
	"""
	def __init__(self):
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		for data in dictData["values"]:
			self[data[0]] = data
		return self
		
class UnitAttributeListPickler:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return UnitAttributeList().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, UnitAttributeList)

unit_attribute_list_inst = UnitAttributeListPickler()