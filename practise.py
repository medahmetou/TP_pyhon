# ex01
# def print_name(name):
#     print("your name is, " + name )

# print_name("Med")

# # exo2
# def read_name():
#     name = input("Enter your name: ")
#     return name

# def print_name(name):
#     print("your name is, " + name )

# name = read_name()
# print_name(name)

# exo3
# def read_number():
#     # number = int(input("Enter a number: "))
#     return int(input("Enter a number: "))

# def check_number(number):
#     result = number % 2
#     if result == 0:
#         return " even"
#     else:
#         return " odd"
    
# def print_number(vb):
#     print("The number is " , vb)

# print_number(check_number(read_number()))

# ex04
# def st_info():
#     age = int(input("Enter your age: "))
#     answer = input("Do you have a driving license? (yes/no): ")
#     has_drivingLicense = answer.lower() == "yes"
#     return age, has_drivingLicense

# def is_accepted(age, has_drivingLicense):
#     return age > 21 and has_drivingLicense

# def  print_result(is_accepted):
#     if (is_accepted == True) : 
#         print("hired")
#     else:
#         print("rejected.")

# # print_result(is_accepted(*st_info()))
# def main():
#     age, has_drivingLicense = st_info()
#     accepted = is_accepted(age, has_drivingLicense)
#     # print(age, has_drivingLicense, accepted)
#     print_result(accepted)

# if __name__ == "__main__":
#     main()

#exercice 1
# def disBounjour(n):
#   for i in range (1,n+1):
#     print("bonjour")
# n=int(input("saisir la valeur de n: "))
# disBounjour(n)


#exercice 2
def demandeEntier():
    n=input('saisir un entier: ')
    while(not(n.isdigit())):
      n=input('n\'est pas entier!! saisir un entier s.v.p: ')
    return n

def estEnter(entiersVal,a,b):
    return entiersVal >=a and entiersVal <=b

#exercice 3
# def affiche_heure(heurs,minutes): n
#   while(minutes>=60):
#     heurs+=1
#     minutes-=60
#   print("Dans une minutes, il sera ",heurs," heure(s),",minutes+1)
# heurs=int(input("saisir le(s) heur(s): "))
# minutes=int(input("saisir le(s) minute(s): "))
# affiche_heure(heurs,minutes)

#exercice 4
# def conversionHeur(heur):
#   minuts=int(heur*60)
#   seconds=(heur*60-minuts)*60
#   return str(minuts) + " minut(s)",str(seconds) + " second(s)"


# def conversionMinute(minuts):
#   heurs=minuts//60
#   minuts-=heurs*60
#   return str(heurs) + " heurs(s)",str(minuts) + " minut(s)"

#exercice 5
#A)
# def somme(n):
#   s=0
#   for i in range(n+1):
#     s+=(2*i+1)**(2*i)
#   return s
#B)
# def sommeR(n):
#   if n == 0:
#     return 1
#   else:
#     return (2*n+1)**(2*n)+sommeR(n-1)
# print(sommeR(1))

#exercice 6
#1) methode1
# def calculeTermeDuSuite(n):
#   fn=1
#   fMois1=1
#   fMois2=1
#   if(n == 0 or n ==1):
#     return 1
#   for i in range(2,n+1):
#     fn=fMois1+fMois2
#     fMois2=fMois1
#     fMois1=fn
#   return fn
#2) methode2
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         a, b = 1, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b
# def recursiveFn(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return recursiveFn(n-1)+recursiveFn(n-2)

#exercice 7
# def multiples3_5(a,b):
#     s=0
#     for i in range(a,b+1):
#         if(i % 3==0 and i % 5==0):
#             s+=i
#     return s

#exercice 8
# def encadrement(n):
#     k=0
#     while(True):
#         if (n >= 2**k  and n <= 2**(k+1)):
#             return k
#         k+=1
# print(encadrement(12))


#exercice 1
def disBounjour(n):
  for i in range (1,n+1):
    print("bonjour")
n=int(input("saisir la valeur de n: "))
disBounjour(n)


#exercice 2
def demandeEntier():
    n=input('saisir un entier: ')
    while(not(n.isdigit())):
      n=input('n\'est pas entier!! saisir un entier s.v.p: ')
    return n

def estEnter(entiersVal,a,b):
    return entiersVal >=a and entiersVal <=b

#exercice 3
def affiche_heure(heurs,minutes):
  while(minutes>=60):
    heurs+=1
    minutes-=60
  print("Dans une minutes, il sera ",heurs," heure(s),",minutes+1)
heurs=int(input("saisir le(s) heur(s): "))
minutes=int(input("saisir le(s) minute(s): "))
affiche_heure(heurs,minutes)

#exercice 4
def conversionHeur(heur):
  minuts=int(heur*60)
  seconds=(heur*60-minuts)*60
  return str(minuts) + " minut(s)",str(seconds) + " second(s)"


def conversionMinute(minuts):
  heurs=minuts//60
  minuts-=heurs*60
  return str(heurs) + " heurs(s)",str(minuts) + " minut(s)"

#exercice 5
#A)
def somme(n):
  s=0
  for i in range(n+1):
    s+=(2*i+1)**(2*i)
  return s
#B)
def sommeR(n):
  if n == 0:
    return 1
  else:
    return (2*n+1)**(2*n)+sommeR(n-1)
print(sommeR(1))

#exercice 6
#1) methode1
def calculeTermeDuSuite(n):
  fn=1
  fMois1=1
  fMois2=1
  if(n == 0 or n ==1):
    return 1
  for i in range(2,n+1):
    fn=fMois1+fMois2
    fMois2=fMois1
    fMois1=fn
  return fn
#2) methode2
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def recursiveFn(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursiveFn(n-1)+recursiveFn(n-2)

#exercice 7
def multiples3_5(a,b):
    s=0
    for i in range(a,b+1):
        if(i % 3==0 and i % 5==0):
            s+=i
    return s

#exercice 8
def encadrement(n):
    k=0
    while(True):
        if (n >= 2**k  and n <= 2**(k+1)):
            return k
        k+=1
print(encadrement(12))