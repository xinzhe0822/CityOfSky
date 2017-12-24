# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *

class ClientManager(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        self.gameBegin=True
        self.turnFlag=True

        self.initGame()
        self.client.SetAllUnit(unit)

    def initGame(self):
        self.turnUnit.resourceName='Chess Unit'
        """
        self.turnUnit.UV.first=2
        self.turnUnit.UV.second=1
        """
        self.turnUnit.ascription=0
        self.turnUnit.higth=0.5
        self.turnUnit.maxHP=10
        self.turnUnit.speed=3
        self.turnUnit.moveLenth=4
        self.turnUnit.attackType=0
        self.turnUnit.attackStandard=5
        self.turnUnit.attackDeviation=2
        self.turnUnit.defense=2
        self.turnUnit.magicDefense=0
        self.turnUnit.luck=2
        self.turnUnit.speedCount=0

        inserUnit(self,self.turnUnit)

        """
        self.turnUnit.UV.first=2
        self.turnUnit.UV.second=8
        
        self.turnUnit.ascription=1
        self.turnUnit.speedCount=0

        inserUnit(self,self.turnUnit)
        """
        self.gameBegin=False

    def inserUnit(self,newUnit):
        newUnit.speedCount+=100/float(newUnit.speed)
        i=0
        while i<len(self.unit):
            if newUnit.speedCount<self.unit[i].speedCount:
                self.unit.insert(i,newUnit)
                break
            elif self.gameBegin and newUnit.speedCount==self.unit[i].speedCount:
                if random.random()<0.5:
                    self.unit.insert(i,newUnit)
                    break
            i+=1
        if i==0 or i==len(self.unit):
            self.unit.append(newUnit)
        