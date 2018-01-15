#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from Vector import Vec2

class Mat2():

    data = [1,0,0,1]

    def __init__(self):
        self.data = [1,0,0,1]

    def Translate(self, vec2, p ):
        vec2.x = vec2.x + p.x
        vec2.y = vec2.y + p.y
        return vec2

    def Rotate(self, vec2, degree ):
        tmpX = ( vec2.x * math.cos(degree * (math.pi / 180) ) ) -  ( vec2.y * math.sin(degree * (math.pi / 180) ) )
        vec2.y = ( vec2.x * math.sin(degree * (math.pi / 180) ) ) + ( vec2.y * math.cos(degree * (math.pi / 180) ) )
        vec2.x = tmpX

        return vec2

    def Scale(self, vec2, k):
        vec.x2 = vec2.x * k
        vec.y2 = vec2.y * k
        return vec2
