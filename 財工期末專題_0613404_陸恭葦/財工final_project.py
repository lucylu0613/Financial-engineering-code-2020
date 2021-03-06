# -*- coding: utf-8 -*-
"""財工final project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zKYgCpvca8InXokez7TZB283Y_c1PFuz
"""

import pandas as pd
import math

option =[[6900,820,835,8.6,9.1],
         [7000,690,740,12,12.5],
         [7100,630,645,17,18],
         [7200,540,550,26,27],
         [7300,445,470,38.5,39.5],
         [7400,372,397,55,56],
         [7500,304,307,78,79],
         [7600,231,235,109,110],
         [7700,173,174,148,149],
         [7800,120,121,195,196],
         [7900,80,81,250,258],
         [8000,48.5,49,323,332],
         [8200,15.5,16.5,493,505],
         [8600,1,2,825,855]] #履約價/call買價/call賣價/put買價/put賣價
TAIEX = [7757,7758] #前面買價後面賣價
Tai_futures =[7756,7760]#前面買價後面賣價
Tai = pd.Series(TAIEX)
Tai_f = pd.Series(Tai_futures)
option = pd.Series(option)
rf= 0.01844
t=1/12

# theorem 2 for call
def th2_call():
  for i in range(len(option)-1):
    for j in range(i+1,len(option)):
      if(option[j][1]-option[i][2]>2):
        print("There would be an arbitrage with Theorem2-call:")
        print('Buying one call option',option[i][0],"cost",option[i][2])
        print("selling one call option",option[j][0])
        print('(for 1~2 is strike price is low to high, c: call price; X: strike price)')
        print('At the maturity, if St<=X1, the profit is c2-c1-2',option[j][1]-option[i][2]-2)
        print("At the maturity, if X1<St<X2, the profit is c2-c1+St-X1",option[j][1]-option[i][2],"-St -",option[i][0]-2)
        print("At the maturity, if St>=X2, the profit is c2-c1+X2-X1",option[j][1]-option[i][2]+option[j][0]-option[i][0]-2)

# theorem 2 for put
def th2_put():
  for i in range(len(option)-1):
    for j in range(i+1,len(option)):
      if(option[i][3]-option[j][4]>2):
        print("There would be an arbitrage with Theorem2-put:")
        print('selling one call option',option[i][0],"get",option[i][3])
        print("buying one put option",option[j][0])
        print('(for 1~2 is strike price is low to high, p: put price; X: strike price)')
        print('At the maturity, if St<=X1, the profit is p1-p2+X2-X1',option[i][3]-option[j][4]+option[j][0]-option[i][0]-2)
        print("At the maturity, if X1<St<X2, the profit is p1-p2+X2-St",option[i][3]-option[j][4]+option[j][0],"-St",-2)
        print("At the maturity, if St>=X3, the profit is p1-p2",option[i][3]-option[j][4]-2)

# theorem 3 for call
def th3_call():
  for i in range(len(option)):
    if option[i][1]-Tai[1]>2:
      print("There would be an arbitrage with Theorem3-call:")
      print("Buying the taiex and selling the call with strike price",option[i][0])
      print("If St>X, we get the strike price ;If St<X, we get the stock price at the maturity")
      prnit("At the maturity, if the St>X, the profit is c-S0+X-2",option[i][1]-Tai[1]+option[i][0]-2)
      print("At the maturity, if the St<X, the profit is c-S0+St-2",option[i][1]-Tai[1],"+St-2")

# theorem 3 for put
def th3_put():
  for i in range(len(option)):
    if option[i][3]-option[i][0]*math.exp(-rf*t)>1:
      print("There would be an arbitrage with Theorem3-put:")
      print("Selling the put with the strike price",option[i][0],"save the present value of strike price")
      print("If St>X, we get the strike price ;If St<X, we get the spot price at the maturity")
      prnit("At the maturity, if the St>X, the profit is p-PV(X)+X-1",option[i][3]-option[i][0]*exp(-rf*t)+option[i][0]-1)
      print("At the maturity, if the St<X, the profit is p-PV(X)+St-1",option[i][3]-option[i][0]*exp(-rf*t),"+St-1")

# theorem 4 for call
def th4():
  for i in range(len(option)):
    value = Tai[0]-option[i][0]*math.exp(-rf*t)
    if value>0:
      tmp =value
    else:
      tmp =0
    if tmp-option[i][2]>2:
      print("There would be an arbitrage with Theorem4 (call):")
      print("Buying call costs",option[i][2]," Saving gets PV(",option[i][0],")")
      print("Selling the taiex gets",Tai[0])
      print("At maturity, if St>X, the profit is S0-c-PV(X)-2",Tai[0]-option[i][2]-option[i][0]*math.exp(-rf*t)-2)
      print("At maturity, if St<X, the profit is S0-c-PV(X)+X-St-2",Tai[0]-option[i][2]-option[i][0]*math.exp(-rf*t)+option[i][0]-2,"-St")

# theorem 6 for put
def th6():
  for i in range(len(option)):
    value = option[i][0]*math.exp(-rf*t)-Tai[1]
    if value>0:
      tmp =value
    else:
      tmp =0
    if tmp-option[i][4]>2:
      print("There would be an arbitrage with Theorem6 (put):")
      print("Buying put costs",option[i][4]," Borrowing gets PV(",option[i][0],")")
      print("Buying the taiex costs",Tai[1])
      print("At maturity, if St>X, the profit is PV(X)-S0-p+St-X-2",option[i][0]*math.exp(-rf*t)-Tai[1]-option[i][4]-option[i][0]-2,"-St")
      print("At maturity, if St<X, the profit is PV(X)-S0-p-2",option[i][0]*math.exp(-rf*t)-Tai[2]-option[i][4]-2)

# check theorem 8
def th8():
  for i in range(len(option)-2):
    for j in range(i+1,len(option)-1):
      for k in range(j+1,len(option)):
        w =(option[k][0]-option[j][0])/(option[k][0]-option[i][0])
        w = w*10000000
        m = 1000000
        g = math.gcd(int(w),m)
        w =w/g
        m =m/g
        if m*option[j][1]-w*option[i][2]-(m-w)*option[k][2]>3:
          print("There would be an arbitrage with Theorem8-call:")
          print("Selling",m,"units of strike price",option[j][0],"get",m*option[j][1])
          print("Buying ",w," units of strike price ",option[i][0]," cost ",w*option[i][2])
          print("Buying ",(m-w)," units of strike price ",option[k][2]," cost ",(m-w)*option[k][2])
					#print("w:",w,"m:",m)
          #print("for 1~3: strike price low to high")
					#print("At maturity, if St<X1, the profit is m*c2-w*c1-(m-w)c3 ")
					#print("At maturity, if X1<St<X2, the profit is m*c2-w*c1-(m-w)c3+m(St-X1)")
				  #print("At maturity, if X2<St<X3, the profit is m*c2-w*c1-(m-w)c3+w(St-X1)-m*(X2-St)")
					#print("At maturity, if St>X3, the profit is m*c2-w*c1-(m-w)c3")

# theorem 9-2
def th9_2():
  for i in range(len(option)):
    if option[i][4]-option[i][1]-(Tai_f[1]-option[i][0])*math.exp(-rf*t)>3:
      print("There would be an arbitrage with Theorem9-2-1:")
      print("Selling call gets",option[i][1])
      print("Buying put costs",option[i][4])
      print("Buying futures costs",Tai_f[1])
      print("The profit is ",(option[i][4]-option[i][1])-(Tai_f[1]-option[i][0])*math.exp(-rf*t)-3)
  
  for i in range(len(option)):
    if (Tai_f[0]-option[i][0])*math.exp(-rf*t)-(option[i][3]-option[i][2])>3:
      print("There would be an arbitrage with Theorem9-2-1:")
      print("Selling call gets",option[i][1])
      print("Buying put costs",option[i][4])
      print("Buying futures costs",Tai_f[1])
      print("The profit is",(option[i][4]-option[i][1])-(Tai_f[1]-option[i][0])*math.exp(-rf*t)-3)

# main
# check theorem 2
print("-----check theorem 2-----") 
th2_call()
th2_put()
# check theorem 3
print("-----check theorem 3-----") 
th3_call()
th3_put()
# check theorem 4 (call lower bound)
print("-----check theorem 4-----") 
th4()
# check theorem 6 (put lower bound)
print("-----check theorem 6-----")
th6()
# check theorem 8
print("-----check theorem 8-----") 
th8()
# check theorem 9
print("-----check theorem 9-2-----")
th9_2()

