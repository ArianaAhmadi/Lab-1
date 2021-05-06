Question 1
print('Input your first and last name')
a = input()
b = a.find(' ')
print(a[b:], a[:b])

Question 2
a=int(input())
if a==0:
  print('Zero')
elif a%2!=0:
  print('Odd')
else:
  print('Even')

Question 3
a=int(input())
for i in range(1, 31+1):
  if a==i:
    print('January', a)
for j in range(32, 59+1):
  if a==j:
    print('February', a)
for k in range(60, 90+1):
  if a==k:
    print('March', a)
for l in range(91, 120+1):
  if a==l:
    print('April', a)
for m in range(121, 151+1):
  if a==m:
    print('May', a)
for n in range(152, 181+1):
  if a==n:
    print('June', a)
for o in range(182, 212+1):
  if a==o:
    print('July', a)
for p in range(213, 243+1):
  if a==p:
    print('August', a)
for q in range(244, 273+1):
  if a==q:
    print('September', a)
for r in range(274, 304+1):
  if a==r:
    print('October', a)
for s in range(305, 334+1):
  if a==s:
    print('November', a)
for t in range(335, 365+1):
  if a==t:
    print('December', a)


Question 4
n=int(input())
i=0
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end='')
    print('')



Question 5
print('Input the maximum number')
n=int(input())
i=0
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end='')
    print('')

Question 6
a=int(input())
if a==1:
  print('Day 1, Monday')
elif a==2
  print('Day 2, Tuesday')
  elif a==3
  print('Day 3, Wednesday')
  elif a==4
  print('Day 4, Thursday')
  elif a==5
  print('Day 5, Friday')
  elif a==6
  print('Day 6, Saturday')
  elif a==7
  print('Day 7, Sunday')
else:
  print()