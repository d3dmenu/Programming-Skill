import math
#!/usr/bin/python

########################################
# File: Hello_Skill
# Building: print("Hello, Skill !!!")
########################################

########################################
# File: Nsum1
# Building: SumNumber()
########################################
def SumNumber():
	result = 0
	x = int(input())
	for i in range(1, x + 1): result += i
	print(result)

########################################
# File: Corner_Digits
# Building: Corner_Digits()
########################################
def Corner_Digits():
	num = int(input())
	print(num[0], end="")
	print(num[-1])

#######################################
# File: Closest_Prime
# Build: key = int(input())
# 			GetPrime(key)
########################################
def GetPrime(key):
  result, pDevice = 99999, []
  for num in range(key-20, key+20):
     if num > 1:
         for i in range(2,num):
             if (num % i) == 0:break
         else: pDevice.append(num)
  for j in range(len(pDevice)):
    value = abs(pDevice[j] - key)
    if value < result: result = value
  print(result)

#######################################
# File: 2_Robot1000
# Build: string = str(input())
#       terminal(string)
########################################
def terminal(key):
  x, y = 0, 0
  key.upper()
  for i in range(len(key)):
    if key[i] == "N": y += 1
    elif key[i] == "S": y -= 1
    elif key[i] == "E": x += 1
    elif key[i] == "W": x -= 1
    elif key[i] == "Z": x, y = 0, 0 
  print(x, y)

#######################################
# File: 2_SwapBits
# Build: x = int(input())
#       SwapBit(x)
########################################
def SwapBit(value):
  num = str(bin(value)[2:])
  if len(num) % 2 != 0:num = "0" + str(num)
  var = list(num)
  for i in range(0, len(num), 2):
    var[i], var[i+1] = var[i+1], var[i]
  var = int("".join(var))
  print(int(str(var), 2))

#######################################
# File: 2_Gradding
# Build: main():
########################################
def grader(score): 
    if score >= 80: print ("A")
    elif score >= 75: print ("B+")
    elif score >= 70: print ("B")
    elif score >= 65: print ("C+")
    elif score >= 60: print ("C")
    elif score >= 55: print ("D+")
    elif score >= 50: print ("D")
    else : print ("F")
def main():
  result = 0
  for i in range(4):
    score = int(input())
    result += score
  grader(result)

#######################################
# File: 2_Tax
# Build: main():
########################################
def tax():
  value = int(input())
  while value > 0:
    data = [10000001, 10000000, 5000001, 5000000, 1000001, 1000000, 100001]
    result = 0
    if value >= data[0]: result += (value-data[0]+1)*32//100

    if data[2] <= value < data[1]: result += (value-data[2]+1)*20//100
    elif data[2] <= value >= data[1]: result += (data[1]-data[2]+1)*20//100

    if data[4] <= value < data[3]: result += (value-data[4]+1)*12//100
    elif data[4] <= value >= data[3]: result += (data[3]-data[4]+1)*12//100

    if data[6] <= value < data[5]: result += (value-data[6]+1)*6//100
    elif data[6] <= value >= data[5]: result += (data[5]-data[6]+1)*6//100
    print(result)
    value = int(input())

########################################
# File: 3_PlusMinus
# Build: main():
########################################
def main():
  n = int(input())
  text = list(map(str, input().split(" ")))
  result = int(text[0])
  for i in range(1, len(text)-1):
    if text[i] == "+": result += int(text[i+1])
    if text[i] == "-": result -= int(text[i+1])
  print(result)

########################################
# File: 3_Domino
# Build: main():
########################################
def main():
  data = [1, 2, 3]
  n = int(input())
  if n <= 3: print(n)
  else:
    for i in range(2, n-1): data.append(data[i]+data[i-1])
    print(data[-1])

########################################
# File: 3_Truck
# Build: main():
########################################
def sudo():
  n, w = map(int, input().split())
  while n != 0 and w != 0:
    data =  [int(i) for i in input().split()]
    temp, count = 0, 0
    for j in range(n):
      if temp < data[j]:
        temp = w
        count += 1
      temp -= data[j]
    print(count)
    n, w = map(int, input().split())

#######################################
# File: 3_Robot1000S
# Build:   key = str(input())
#          num = int(input())
########################################
def Robot1000S(key, k):
  n, s, w, e, data = 0, 0, 0, 0, [0, 0, 0, 0]
  if len(key) == k: print(0)
  else:
      for i in key:
          if i == "N": n += 1
          elif i == "S": s += 1
          elif i == "W": w += 1
          elif i == "E": e += 1
      if n >= s: data[3] = n; data[0] = s
      else: data[3] = s; data[0] = n
      if w >= e: data[2] = w; data[1] = e
      else: data[2] = e; data[1] = w
      x, y = (data[0] + data[1]) - k, data[2] + data[3]
      if x < 0: print(abs(y+x)*2)
      else: print(abs(x - y)*2)

#######################################
# File: 4_Mask
# Build:   key = str(input())
#          num = int(input())
########################################
def Mask():
  data, arr = [], [0, 0, 0, 0]
  n = int(input())
  for i in range(4): 
      team = []
      for j in range(n):
          value = int(input())
          team.append(value)
      data.append(team)
  t1, t2 = max(data[0]), max(data[1])
  t3, t4 = max(data[2]), max(data[3])
  if max(t1, t2) > max(t3, t4):
      arr[0], arr[2] = max(t1, t2),min(t1, t2)
      arr[1], arr[3] = max(t3, t4),min(t3, t4)
  if max(t1, t2) < max(t3, t4):
      arr[0], arr[2] = max(t3, t4),min(t1, t2)
      arr[1], arr[3] = max(t1, t2),min(t3, t4)
  data = data[0] + data[1] + data[2] + data[3]
  for i in range(4): arr[i] = data.index(arr[i])+1
  print(arr[0], arr[1], arr[2], arr[3])

########################################
# File: 4_Cola
# Build: Cola()
########################################
def Cola():
  n = int(input())
  print(n//2+n)

########################################
# File: 4_Element
# Building in C++ 
# https://drive.google.com/file/d/1gJ4MlDpLjEEbTiz9HttFB3Pml0Pf02uW/view?usp=sharing
########################################

########################################
# File: 4_Robot2000
# Build: key = str(input())
########################################
def Robot2000():
  def setPattern(x):
    while(Pattern[0] != x):
        Pattern.append(Pattern[0])
        Pattern.remove(Pattern[0])
    return Pattern
  Pattern, result, current = ["N", "E", "S", "W"], "", "N"
  #key = str(input())
  for i in range(len(key)):
      if key[i] == "Z":
          result += "Z"
          current = "N"
      else:
          if current != key[i]:
              Pattern = setPattern(current)
              value = Pattern.index(key[i])-Pattern.index(current)
              current = key[i]
              result += ("R" * value) + "F"
          else: result += "F"
  print(result)

########################################
# File: 5_Alcatraz
# Build: key = str(input())
########################################
def Altacatraz():
  data = []
  x, y, n = map(int, input().split())
  for i in range(n):
      value = int(input())
      result, count = 0, 0
      while True:
          count += 1
          result += x
          if result < value: result -= y
          else: break
      data.append(count)
  print(sum(data))

########################################
# File: 5_BuggyRobot
# Build: key = str(input())
########################################
def BuggyRobot():
  result, count = 0, 0
  n, m, k = map(int, input().split())
  while True:
      result += n
      count += n
      if result < k:
          result -= m
          count += m
      else: break
  value = result - k
  count -= value
  print(count)

########################################
# File: 5_Chick
# Build: key = str(input())
########################################
def chick():
  data, result, scan = [1], 1, 0
  n = int(input())
  if n == 0: print(0)
  else:
      for i in range(n):
          if i >= 6: result -= data[i-6]
          if i > 0:
              scan = result
              result *= 3
              data.append(result-scan)
      print(result)

########################################
# File: 5_Bird
# Build: Bird()
########################################
def Bird():
  data, value = [], []
  n, t = map(int, input().split())
  for i in range(n):
      x = int(input())
      data.append(x)
  data = data + data
  for j in range(n): 
      result = 0
      for k in range(j, j+t):
          result += data[k]
      value.append(result)
  print(max(value))

########################################
# File: 5_WinterIsComing
# Build: WinterIsComing()
########################################
def WinterIsComing():
  n, current = map(int, input().split())
  object, live, data = [], current, [1, 0, -1]
  for num in range(n):
      value = int(input())
      object.append(value)
  for i in range(len(object)):
      if object[i] in data: live -= 1
      else:
          for j in range(2, object[i]):
              if (object[i] % j) == 0: 
                  live -= 1
                  break
          else: live = current
      if live < 0: print('NO'); break
  if live >= 0 and n != 0: print('YES')

########################################
# File: 5_The Thief of Baramos
# Download: https://drive.google.com/file/d/17mjtNDMkMJstgh9L9SjLcRmenT2PRz7J/view?usp=sharing
########################################

########################################
# File: 5_Ghosticket
# Build: Ghosticket()
########################################
def Ghosticket():
  data, result1, result2 = [], 0, 0
  n, k = map(int, input().split())
  for i in range(n):
      ticket = int(input())
      data.append(ticket)
  for o in range(k): result2 += max(data)-o
  for j in range(k):
      value = 0
      for k in range(n):
          if data[k] > value:
              value, index = data[k], k
      result1 += value
      data[index] = value-1
  print(result1) if result1 > result2 and n != 0 else print(result2)

########################################
# File: 5_GameOfDead
# Build: GameOfDead()
########################################
def GameOfDead():
  index = -1
  x, y = map(int, input().split())
  if y == 1: print(x)
  else:
      data = [x for x in range(1, x + 1)]
      while len(data) != 1:
          index += y
          if index <= len(data)-1: data[index] = -99
          else:
              distance = index - (len(data)-1)
              index = (distance -1) - y
              data = [x for x in data if x != -99]
      print(data[0])

########################################
# File: 7_Flower
# Build: Flower()
########################################
def Flower():
  def const(i, j, index, size):
    vector = [i-index, i+index, j-index, j+index]
    for e in range(len(vector)):
      if vector[e] < 0: vector[e] = 0
      if vector[e] > size: vector[e] = size
    for i in range(vector[0], vector[1]+1):
      for j in range(vector[2], vector[3]+1):
        if data[i][j] == 0: data[i][j] = -1
  data, result = [], 0
  x = int(input())
  for c in range(x):
    value = [int(c) for c in input().split()]
    data.append(value)
  for i in range(x):
    for j in range(x):
      index = data[i][j]
      if index: const(i, j, index, x-1)
  for num in range(x): result += data[num].count(0)
  print(result)

########################################
# File: 8_Anagram
# Build: Anagram()
########################################
def Anagram():
  n = int(input())
  for i in range(n):
      text = str(input())
      check = str(input())
      text, check = sorted(list(text.upper())), sorted(list(check.upper()))
      print("ANAGRAM") if text == check else print("NOT ANAGRAM")


########################################
# File: 8_Reverse
# Build: Reverse()
########################################
def Reverse():
  n = int(input())
  for c in range(n):
      text = str(input())
      m = int(input())
      for i in range(m):
          x, y = map(int, input().split())
          value = text[x-1:y]
          value, text = list(value), list(text)
          value = value[::-1]
          for j in range(abs(x-y-1)): text[x-1+j] = value[j]
      print("".join(map(str, text)))
