# -*- coding: utf-8 -*-
"""0613404_homework4_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nbd4g3PVbQYhNucp8lPdYpkncl9lxDWK
"""

def duration(n,c,r,face):
  duration=0
  value =0
  for i in range(1,n+1):
    discount =1
    for j in range(1,i+1):
      discount = discount/(1+r)
    duration=duration+i*discount*c
    value = value+discount*c
    if(i==n):
      value = value+discount*face
      duration=duration+(n)*discount*face
  duration =duration/value
  return duration

n =int(input("請輸入期數"))
co =float(input("請輸入債息(%)"))
ro =float(input("請輸入利率(%)"))
face =float(input("請輸入face value"))
c=co/100*face
r=ro/100
ans1=duration(n,c,r,face)
print("Duration=",ans1)