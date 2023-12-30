"""salom hammaga 
bu kodlar davRoni muvvofaqiyatga yetishidan oldin yozilgan kodlar
demak man boshladim"""
"""<<<birinchi mani kodlarim >>>"""

#bu kod siz kutayotgan uchun ishlatiladi , sevgan qizingizni
#hayron qoldirish vaqti keldi
 
#ism = input("qani ismingizni kiritingchi: ")
#if ism.lower() != 'madina':
#    print(f"kechirasan {ism} , men seni kutmayapman")
#else:
#    print("man sani sevaman Madinam")
    
"""ushbu kod juda oddiy ammo man uchun bu hali yangilik"""

#talaba_1 = {'talabaning ismi': 'hakimov davron' , 
#            'yili':2005,
#            'yoshi':19}
#talaba = talaba_1.get('kuni' ,'bundan malumot mavjud emas')
#print(talaba)

"""MANI SINFDOSHLARIM VA KRSDOSHLARIM HAQIDA OZGINA MA,LUMOON MAN HAQIMDAYAM BOR"""

student_1 = {'ism':'davron',
             'familiya':'hakimov',
             'yosh':19,
             'fakultet':'IT business'}
student_2 = {'ism':'fotima',
             'familiya':'qurbonova',
             'yosh':18,
             'fakultet':'arxitektura'}
student_3 = {'ism':'nodir',
             'familiya':'hakimov',
             'yosh':16,
             'fakultet':'IT'}

studentlar = [student_1,student_2 ,student_3]
for student in studentlar:
    print(f"{student['ism'].title()}"
          f"{student['familiya'].title()}",
          f"bu student {student['yosh']}da va {student['fakultet']}da o'qiydi")














