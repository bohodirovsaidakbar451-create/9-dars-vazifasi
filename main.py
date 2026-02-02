#--------------------[ Vazifa 1 ]------------------------------------#

# sonlar = [1,2,3,4,5,6,7,8,9]
# qaytar = list(map(lambda a: a*3, sonlar))
# print(qaytar)

#--------------------[ Vazifa 2 ]------------------------------------#

# sonlar = [1,2,3,4,5,6,7,8,9]
# qaytar = list(map(lambda a: a*a, sonlar))
# print(qaytar)

#--------------------[ Vazifa 3 ]------------------------------------#

# satr = ["a","b","s","d","v","k"]
# qaytar = list(map(str.upper, satr))
# print(qaytar)

#--------------------[ Vazifa 4 ]------------------------------------#

# ismlar = ["SaidAkbar","Javohir","Alijon","Valibek","Doston","Abdurahim"]
# qaytar = list(map(lambda a: len(a), ismlar))
# print(qaytar)

#--------------------[ Vazifa 5 ]------------------------------------#

# def ssonlar_musbat(a):
#     if a < 0:
#         return a*-1
#     else:
#         return a
#
# sonlar = [-5,-8,-7,8,-6,-2,4,3]
# qaytar = list(map(ssonlar_musbat, sonlar))
# print(qaytar)

#--------------------[ Vazifa 6 ]------------------------------------#

# def foiz_qoshish(a):
#     v = a * 0.15
#     return int(a + v)
#
# narxlar = [1000, 2000, 3000]
# qaytar = list(map(foiz_qoshish, narxlar))
# print(qaytar)

#--------------------[ Vazifa 7 ]------------------------------------#

# def juft_qa(a):
#     if a % 2 == 0:
#         return 0
#     else:
#         return a
#
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# qaytar = list(map(juft_qa, sonlar))
# print(qaytar)

#--------------------[ Vazifa 8 ]------------------------------------#

# satr = ["a","b","s","d","v","k"]
# qaytar = list(map(lambda a: a + "!", satr))
# print(qaytar)

#--------------------[ Vazifa 9 ]------------------------------------#


# sonlar = [1,2,3,4,5,6,7,8,9,10]
# qaytar = list(filter(lambda a: a % 2 == 0, sonlar))
# print(qaytar)

#--------------------[ Vazifa 10 ]------------------------------------#

# sonlar = [1,-2,3,4,-5,6,-7,8,-9,10]
# qaytar = list(filter(lambda a: a > 0, sonlar))
# print(qaytar)

#--------------------[ Vazifa 11 ]------------------------------------#

# matnlar = ["salom", "aliknoma", "laksffrk", "asd", "wee3"]
# qaytar = list(filter(lambda a: len(a) > 5, matnlar))
# print(qaytar)

#--------------------[ Vazifa 12 ]------------------------------------#

# sonlar = [6,5,15,10,9,87,45]
# qaytar = list(filter(lambda a: a % 5 == 0, sonlar))
# print(qaytar)

#--------------------[ Vazifa 13 ]------------------------------------#

# ismlar = ["SaidAkbar","Javohir","Alijon","Valibek","Doston","Abdurahim"]
# qaytar = list(filter(lambda a: a[0] == "A", ismlar))
# print(qaytar)

#--------------------[ Vazifa 14 ]------------------------------------#


# sonlar = [-1,-2,-6,-9,0,1,2,3,4,5]
# qaytar = list(filter(lambda a: a >= 0, sonlar))
# print(qaytar)

#--------------------[ Vazifa 15 ]------------------------------------#

# satrlar = ["Menga python yoqadi", "Aslida php yoqadi"]
# qaytar = list(filter(lambda a: "python" in a, satrlar))
# print(qaytar)