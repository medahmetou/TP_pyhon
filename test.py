# -*- coding: utf-8 -*-
"""
TD2 Python - حلول بعدة طرق (من الأصعب إلى الأسهل)
كل تمرين له عدة دوال: exNN_m1 (الأصعب) ... exNN_mK (الأسهل)
شغّل الملف مباشرة لرؤية النتائج في آخر الملف.
"""
import math
import re
import unicodedata
from collections import Counter
from functools import reduce
from itertools import accumulate
from operator import mul
from datetime import date
from statistics import mean


# =====================================================================
# التمرين 1: عرض جملة + حساب 17 + 35 * 2
# المفهوم المهم: أولوية العمليات (الضرب قبل الجمع) => 17 + 70 = 87
# =====================================================================

def ex1_m1():
    # الأصعب: eval يحوّل نصاً إلى عملية حسابية ويحسبها (احذر: لا تستعمله مع مدخلات المستخدم)
    print("J'apprends Python !")
    expr = "17 + 35 * 2"
    print(f"{expr} = {eval(expr)}")


def ex1_m2():
    # متوسط: متغيرات + f-string
    phrase = "J'apprends Python !"
    resultat = 17 + 35 * 2
    print(phrase)
    print(f"Résultat : {resultat}")


def ex1_m3():
    # الأسهل: print مباشرة
    print("J'apprends Python !")
    print(17 + 35 * 2)


# =====================================================================
# التمرين 2: جدول الضرب لعدد معيّن
# =====================================================================

def ex2_m1(n):
    # الأصعب: comprehension داخل join (سطر واحد، نص واحد)
    print("\n".join(f"{n} x {i} = {n * i}" for i in range(1, 11)))


def ex2_m2(n):
    # متوسط: حلقة for + f-string
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def ex2_m3(n):
    # الأسهل: حلقة while (تحتاج عدّاداً تزيده بنفسك)
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i += 1


# =====================================================================
# التمرين 3: رمز PIN = 2024 (اطلب الإدخال حتى يكون صحيحاً)
# (الدوال تستعمل input، لذلك استدعاؤها معلّق في آخر الملف)
# =====================================================================

def ex3_m1():
    # الأصعب: عامل walrus ( := ) يسند القيمة ويقارنها في نفس السطر
    while (saisie := input("Code PIN : ")) != "2024":
        print("Code incorrect, réessayez.")
    print("Accès autorisé")


def ex3_m2():
    # متوسط: حلقة لا نهائية + break عند النجاح
    while True:
        saisie = input("Code PIN : ")
        if saisie == "2024":
            print("Accès autorisé")
            break
        print("Code incorrect, réessayez.")


def ex3_m3():
    # الأسهل: شرط الحلقة على المتغير نفسه
    saisie = ""
    while saisie != "2024":
        saisie = input("Code PIN : ")
        if saisie != "2024":
            print("Code incorrect, réessayez.")
    print("Accès autorisé")


# =====================================================================
# التمرين 4: العدد التام (يساوي مجموع قواسمه الحقيقية، مثل 6 = 1+2+3)
# =====================================================================

def ex4_m1(n):
    # الأصعب والأسرع: نبحث فقط حتى sqrt(n) ونأخذ كل قاسم مع نظيره n//d
    if n < 2:
        return False
    s = 1  # 1 قاسم دائماً
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            s += d
            if d != n // d:  # لا نجمع الجذر مرتين (مثل 4 في 16)
                s += n // d
    return s == n


def ex4_m2(n):
    # متوسط: sum + generator
    return n > 1 and sum(d for d in range(1, n) if n % d == 0) == n


def ex4_m3(n):
    # الأسهل: حلقة وعدّاد
    somme = 0
    for d in range(1, n):
        if n % d == 0:
            somme += d
    return n > 1 and somme == n


# =====================================================================
# التمرين 5: العاملي n!
# =====================================================================

def ex5_m1(n):
    # الأصعب: reduce يطبّق الضرب تراكمياً على 1..n
    return reduce(mul, range(1, n + 1), 1)


def ex5_m2(n):
    # متوسط: العودية (الدالة تستدعي نفسها). الحالة الأساسية: 0! = 1
    if n <= 1:
        return 1
    return n * ex5_m2(n - 1)


def ex5_m3(n):
    # أسهل: حلقة
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def ex5_m4(n):
    # الأسهل: مكتبة math
    return math.factorial(n)


# =====================================================================
# التمرين 6: أكبر عدد من ثلاثة
# =====================================================================

def ex6_m1(a, b, c):
    # الأصعب: reduce مع lambda (يعمل مع أي عدد من القيم)
    return reduce(lambda x, y: x if x > y else y, (a, b, c))


def ex6_m2(a, b, c):
    # متوسط: تعبير شرطي متداخل
    return a if a >= b and a >= c else (b if b >= c else c)


def ex6_m3(a, b, c):
    # أسهل: if / elif
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def ex6_m4(a, b, c):
    # الأسهل: الدالة الجاهزة
    return max(a, b, c)


# =====================================================================
# التمرين 7: العدد الأولي
# =====================================================================

def ex7_m1(n):
    # الأصعب والأسرع: كل الأعداد الأولية > 3 على شكل 6k±1
    if n < 2:
        return False
    if n < 4:
        return True            # 2 و 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def ex7_m2(n):
    # متوسط: all() + isqrt
    return n > 1 and all(n % d != 0 for d in range(2, math.isqrt(n) + 1))


def ex7_m3(n):
    # الأسهل: نجرّب كل القواسم
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


# =====================================================================
# التمرين 8: PGCD (خوارزمية إقليدس: pgcd(a,b) = pgcd(b, a % b))
# =====================================================================

def ex8_m1(a, b):
    # الأصعب: عودية في سطر واحد
    return a if b == 0 else ex8_m1(b, a % b)


def ex8_m2(a, b):
    # متوسط: إقليدس بحلقة (tuple unpacking)
    while b:
        a, b = b, a % b
    return a


def ex8_m3(a, b):
    # الأسهل منطقياً لكنه بطيء: نبحث عن أكبر قاسم مشترك بالتجريب
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d


def ex8_m4(a, b):
    # الجاهز
    return math.gcd(a, b)


# =====================================================================
# التمرين 9: عدد -> نص بالفرنسية (123 -> "cent vingt-trois")
# قواعد: 70=soixante-dix, 80=quatre-vingts, 90=quatre-vingt-dix,
#        21=vingt et un, 71=soixante et onze, deux cents (s فقط إن انتهى العدد)
# =====================================================================

UNITES = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit",
          "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize",
          "dix-sept", "dix-huit", "dix-neuf"]
DIZAINES = {2: "vingt", 3: "trente", 4: "quarante", 5: "cinquante", 6: "soixante"}


def _moins_de_100(n, final=True):
    if n < 20:
        return UNITES[n]
    if n < 70:
        d, u = divmod(n, 10)
        if u == 0:
            return DIZAINES[d]
        if u == 1:
            return DIZAINES[d] + " et un"
        return DIZAINES[d] + "-" + UNITES[u]
    if n < 80:                       # 70..79 = soixante + (10..19)
        r = n - 60
        return "soixante et onze" if r == 11 else "soixante-" + UNITES[r]
    r = n - 80                       # 80..99 = quatre-vingt + (0..19)
    if r == 0:
        return "quatre-vingts" if final else "quatre-vingt"
    return "quatre-vingt-" + UNITES[r]


def ex9_m2(n):
    # متوسط: من 0 إلى 999 فقط
    c, r = divmod(n, 100)
    parts = []
    if c == 1:
        parts.append("cent")
    elif c > 1:
        parts.append(UNITES[c] + " cent" + ("s" if r == 0 else ""))
    if r or c == 0:
        parts.append(_moins_de_100(r))
    return " ".join(parts)


def _moins_de_1000(n, final=True):
    c, r = divmod(n, 100)
    parts = []
    if c == 1:
        parts.append("cent")
    elif c > 1:
        parts.append(UNITES[c] + " cent" + ("s" if r == 0 and final else ""))
    if r:
        parts.append(_moins_de_100(r, final))
    return " ".join(parts)


def ex9_m1(n):
    # الأصعب: يدعم حتى 999 999 999 999 (نقسّم العدد إلى مجموعات)
    if n == 0:
        return "zéro"
    if n < 0:
        return "moins " + ex9_m1(-n)
    parts = []
    for valeur, nom in [(10**9, "milliard"), (10**6, "million"), (1000, "mille")]:
        q, n = divmod(n, valeur)
        if q:
            if nom == "mille":
                parts.append("mille" if q == 1 else _moins_de_1000(q, final=False) + " mille")
            else:
                parts.append(_moins_de_1000(q) + " " + nom + ("s" if q > 1 else ""))
    if n:
        parts.append(_moins_de_1000(n))
    return " ".join(parts)


def ex9_m3(n):
    # الأسهل: مكتبة جاهزة  ->  pip install num2words
    from num2words import num2words
    return num2words(n, lang="fr")


# =====================================================================
# التمرين 10: عدد أيام الشهر (مع السنة الكبيسة)
# كبيسة: تقبل القسمة على 4 وليست على 100، أو تقبل القسمة على 400
# =====================================================================

def ex10_m1(annee, mois):
    # الأصعب: نطرح تاريخ أول الشهر من تاريخ أول الشهر التالي
    debut = date(annee, mois, 1)
    suivant = date(annee + (mois == 12), mois % 12 + 1, 1)
    return (suivant - debut).days


def ex10_m2(annee, mois):
    # متوسط: قاموس + دالة السنة الكبيسة
    bissextile = annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)
    jours = {1: 31, 2: 29 if bissextile else 28, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return jours[mois]


def ex10_m3(annee, mois):
    # أسهل: if / elif
    if mois in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mois in (4, 6, 9, 11):
        return 30
    elif annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        return 29
    else:
        return 28


def ex10_m4(annee, mois):
    # الجاهز
    import calendar
    return calendar.monthrange(annee, mois)[1]


# =====================================================================
# التمرين 11: عدد الحروف المتحركة
# =====================================================================

def ex11_m1(s):
    # الأصعب: نزيل التشكيل (é -> e) ثم نعدّ بـ sum + generator
    sans_accent = unicodedata.normalize("NFD", s.lower())
    sans_accent = "".join(c for c in sans_accent if not unicodedata.combining(c))
    return sum(1 for c in sans_accent if c in "aeiou")


def ex11_m2(s):
    # متوسط: تعبير نمطي regex
    return len(re.findall(r"[aeiouàâäéèêëîïôöùûü]", s, re.IGNORECASE))


def ex11_m3(s):
    # الأسهل: حلقة وعدّاد
    voyelles = "aeiouàâäéèêëîïôöùûü"
    compteur = 0
    for c in s.lower():  # lower() يوحّد الحروف الكبيرة والصغيرة (É -> é)
        if c in voyelles:
            compteur += 1
    return compteur


# =====================================================================
# التمرين 12: عكس نص
# =====================================================================

def ex12_m1(s):
    # الأصعب: عودية (آخر حرف + عكس الباقي)
    return s if len(s) <= 1 else s[-1] + ex12_m1(s[:-1])


def ex12_m2(s):
    # reduce: نضيف كل حرف في بداية النتيجة
    return reduce(lambda acc, c: c + acc, s, "")


def ex12_m3(s):
    # حلقة
    r = ""
    for c in s:
        r = c + r
    return r


def ex12_m4(s):
    # reversed + join
    return "".join(reversed(s))


def ex12_m5(s):
    # الأسهل: slicing بخطوة -1
    return s[::-1]


# =====================================================================
# التمرين 13: متتالية فيبوناتشي حتى N (كل الحدود <= N)
# =====================================================================

def ex13_m1(N):
    # الأصعب: generator (يعطي القيم واحدة واحدة بـ yield)
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


def ex13_m2(N):
    # متوسط: حلقة + تبديل متعدد
    suite, a, b = [], 0, 1
    while a <= N:
        suite.append(a)
        a, b = b, a + b
    return suite


def ex13_m3(N):
    # الأسهل: متغير مؤقت بدل التبديل المتعدد
    suite = []
    a = 0
    b = 1
    while a <= N:
        suite.append(a)
        temp = a + b
        a = b
        b = temp
    return suite


# =====================================================================
# التمرين 14: عدد مرات ظهور عنصر في قائمة
# =====================================================================

def ex14_m1(lst, x):
    # الأصعب: Counter يحسب تكرار كل العناصر دفعة واحدة
    return Counter(lst)[x]


def ex14_m2(lst, x):
    # متوسط: sum + generator
    return sum(1 for e in lst if e == x)


def ex14_m3(lst, x):
    # أسهل: حلقة
    c = 0
    for e in lst:
        if e == x:
            c += 1
    return c


def ex14_m4(lst, x):
    # الجاهز
    return lst.count(x)


# =====================================================================
# التمرين 15: ترتيب قائمة تصاعدياً أو تنازلياً
# =====================================================================

def ex15_m1(lst, decroissant=False):
    # الأصعب: Quicksort عودي (نختار pivot ونقسم إلى أصغر وأكبر)
    if len(lst) <= 1:
        return lst[:]
    p = lst[0]
    petits = [x for x in lst[1:] if x <= p]
    grands = [x for x in lst[1:] if x > p]
    res = ex15_m1(petits) + [p] + ex15_m1(grands)
    return res[::-1] if decroissant else res


def ex15_m2(lst, decroissant=False):
    # متوسط: ترتيب الفقاعات Bubble sort (نبدّل الجارين إن كانا بترتيب خاطئ)
    l = lst[:]  # نسخة كي لا نغيّر الأصل
    n = len(l)
    for i in range(n):
        for j in range(n - i - 1):
            faux = l[j] < l[j + 1] if decroissant else l[j] > l[j + 1]
            if faux:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def ex15_m3(lst, decroissant=False):
    # أسهل: sorted ترجع قائمة جديدة
    return sorted(lst, reverse=decroissant)


def ex15_m4(lst, decroissant=False):
    # أسهل: .sort() تعدّل القائمة نفسها
    l = lst[:]
    l.sort(reverse=decroissant)
    return l


# =====================================================================
# التمرين 16: مربعات الأعداد من 1 إلى N
# =====================================================================

def ex16_m1(N):
    # الأصعب (ذكي): مربع n = مجموع أول n عدد فردي (1, 1+3, 1+3+5 ...)
    return list(accumulate(range(1, 2 * N, 2)))


def ex16_m2(N):
    # متوسط: map + lambda
    return list(map(lambda x: x ** 2, range(1, N + 1)))


def ex16_m3(N):
    # أسهل: list comprehension
    return [x ** 2 for x in range(1, N + 1)]


def ex16_m4(N):
    # الأسهل: حلقة + append
    res = []
    for x in range(1, N + 1):
        res.append(x * x)
    return res


# =====================================================================
# التمرين 17: متوسط عناصر قائمة
# =====================================================================

def ex17_m1(lst):
    # الأصعب: المتوسط المتحرك (نحدّثه عند كل عنصر دون حساب المجموع)
    moy = 0
    for i, x in enumerate(lst, start=1):
        moy += (x - moy) / i
    return moy


def ex17_m2(lst):
    # متوسط: مكتبة statistics
    return mean(lst)


def ex17_m3(lst):
    # أسهل: sum / len
    return sum(lst) / len(lst)


def ex17_m4(lst):
    # الأسهل منطقياً: حلقة يدوية
    total = 0
    n = 0
    for x in lst:
        total += x
        n += 1
    return total / n


# =====================================================================
# التمرين 18: Celsius <-> Fahrenheit
#   F = C * 9/5 + 32      C = (F - 32) * 5/9
# =====================================================================

CONVERSIONS = {
    ("C", "F"): lambda t: t * 9 / 5 + 32,
    ("F", "C"): lambda t: (t - 32) * 5 / 9,
}


def ex18_m1(t, de, vers):
    # الأصعب: قاموس دوال (يسهل إضافة وحدات أخرى مثل Kelvin)
    return CONVERSIONS[(de.upper(), vers.upper())](t)


def ex18_m2(t, unite):
    # متوسط: دالة واحدة، تحدّد الاتجاه حسب الوحدة المعطاة
    if unite.upper() == "C":
        return t * 9 / 5 + 32
    elif unite.upper() == "F":
        return (t - 32) * 5 / 9
    raise ValueError("unité inconnue (C ou F)")


def celsius_vers_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_vers_celsius(f):
    return (f - 32) * 5 / 9


# =====================================================================
# التمرين 19: عدد أرقام عدد صحيح
# =====================================================================

def ex19_m1(n):
    # الأصعب: عودية (كل استدعاء يحذف رقماً بالقسمة //10)
    n = abs(n)
    return 1 if n < 10 else 1 + ex19_m1(n // 10)


def ex19_m2(n):
    # متوسط: اللوغاريتم (انتبه: قد يخطئ مع الأعداد الضخمة جداً بسبب float)
    n = abs(n)
    return 1 if n == 0 else int(math.log10(n)) + 1


def ex19_m3(n):
    # أسهل: حلقة while
    n = abs(n)
    c = 1
    while n >= 10:
        n //= 10
        c += 1
    return c


def ex19_m4(n):
    # الأسهل: نحوّله إلى نص ونأخذ طوله
    return len(str(abs(n)))


# =====================================================================
# التمرين 20: ترتيب كلمات جملة أبجدياً
# =====================================================================

def _cle(mot):
    # يحذف التشكيل ويحوّل لحروف صغيرة ليُرتَّب "école" قرب "e"
    s = unicodedata.normalize("NFD", mot)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def ex20_m1(phrase):
    # الأصعب: regex لاستخراج الكلمات بدون علامات الترقيم + مفتاح ترتيب يتجاهل التشكيل
    return sorted(re.findall(r"\w+", phrase), key=_cle)


def ex20_m2(phrase):
    # متوسط: sorted مع key يتجاهل حالة الحروف
    return sorted(phrase.split(), key=str.lower)


def ex20_m3(phrase):
    # الأسهل: split ثم sort (الحرف الكبير يسبق الصغير!)
    mots = phrase.split()
    mots.sort()
    return mots


# =====================================================================
# التمرين 21: جمع مصفوفتين
# =====================================================================

def ex21_m1(A, B):
    # الأصعب: comprehension متداخل + zip
    return [[a + b for a, b in zip(ligA, ligB)] for ligA, ligB in zip(A, B)]


def ex21_m2(A, B):
    # متوسط: comprehension بالفهارس
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ex21_m3(A, B):
    # أسهل: حلقتان متداخلتان + التحقق من تساوي الحجم
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Les matrices doivent avoir la même taille")
    C = []
    for i in range(len(A)):
        ligne = []
        for j in range(len(A[0])):
            ligne.append(A[i][j] + B[i][j])
        C.append(ligne)
    return C


def ex21_m4(A, B):
    # الأسهل لمن يعرف المكتبة: numpy  ->  pip install numpy
    import numpy as np
    return (np.array(A) + np.array(B)).tolist()


# =====================================================================
# التمرين 22: البحث عن عنصر وعرض موقعه أو رسالة خطأ
# =====================================================================

def ex22_m1(lst, x):
    # الأصعب: next() مع generator ونعطي قيمة افتراضية None
    pos = next((i for i, e in enumerate(lst) if e == x), None)
    print(f"{x} trouvé à la position {pos}" if pos is not None else f"Erreur : {x} introuvable")


def ex22_m2(lst, x):
    # متوسط: for ... else  (else تنفذ فقط إذا انتهت الحلقة بدون break)
    for i, e in enumerate(lst):
        if e == x:
            print(f"{x} trouvé à la position {i}")
            break
    else:
        print(f"Erreur : {x} introuvable")


def ex22_m3(lst, x):
    # أسهل: index داخل try / except
    try:
        print(f"{x} trouvé à la position {lst.index(x)}")
    except ValueError:
        print(f"Erreur : {x} introuvable")


def ex22_m4(lst, x):
    # الأسهل: in ثم index
    if x in lst:
        print(f"{x} trouvé à la position {lst.index(x)}")
    else:
        print(f"Erreur : {x} introuvable")


# =====================================================================
# التمرين 23: palindrome
# =====================================================================

def _nettoyer(s):
    # يحذف المسافات والترقيم والتشكيل ويجعل الحروف صغيرة
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if c.isalnum())


def ex23_m1(s):
    # الأصعب: عودية (نقارن الطرفين ثم الوسط)
    s = _nettoyer(s)
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and ex23_m1(s[1:-1])


def ex23_m2(s):
    # متوسط: مؤشران من الطرفين
    s = _nettoyer(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def ex23_m3(s):
    # الأسهل: نقارن النص بعكسه
    s = _nettoyer(s)
    return s == s[::-1]


# =====================================================================
# التمرين 24: العدد النرجسي / Armstrong (153 = 1^3 + 5^3 + 3^3)
# =====================================================================

def ex24_m1(n):
    # الأصعب: رياضياً بدون نص (divmod يستخرج آخر رقم)
    k = len(str(n))
    total, reste = 0, n
    while reste > 0:
        reste, chiffre = divmod(reste, 10)
        total += chiffre ** k
    return total == n


def ex24_m2(n):
    # متوسط: sum + generator
    s = str(n)
    return sum(int(c) ** len(s) for c in s) == n


def ex24_m3(n):
    # الأسهل: حلقة على الأرقام
    s = str(n)
    k = len(s)
    total = 0
    for c in s:
        total += int(c) ** k
    return total == n


def narcissiques_jusqua(N):
    # كل الأعداد النرجسية حتى N
    return [n for n in range(1, N + 1) if ex24_m2(n)]


# =====================================================================
# تجربة كل شيء
# =====================================================================
if __name__ == "__main__":
    print("--- Ex1 ---");  ex1_m1(); ex1_m2(); ex1_m3()
    print("--- Ex2 ---");  ex2_m1(7); ex2_m2(7); ex2_m3(7)
    # print("--- Ex3 ---"); ex3_m1()   # ألغِ التعليق لتجربتها (تطلب input)
    print("--- Ex4 ---", [ex4_m1(n) for n in (6, 28, 12)], ex4_m2(496), ex4_m3(8128))
    print("--- Ex5 ---", ex5_m1(5), ex5_m2(5), ex5_m3(5), ex5_m4(5))
    print("--- Ex6 ---", ex6_m1(3, 9, 5), ex6_m2(3, 9, 5), ex6_m3(3, 9, 5), ex6_m4(3, 9, 5))
    print("--- Ex7 ---", [ex7_m1(n) for n in (1, 2, 17, 21, 97)],
          [ex7_m2(n) for n in (1, 2, 17, 21, 97)], [ex7_m3(n) for n in (1, 2, 17, 21, 97)])
    print("--- Ex8 ---", ex8_m1(48, 18), ex8_m2(48, 18), ex8_m3(48, 18), ex8_m4(48, 18))
    print("--- Ex9 ---")
    for n in (0, 21, 71, 80, 123, 280, 999, 1000, 2024, 80000, 1234567):
        print(n, "->", ex9_m1(n))
    print(ex9_m2(123))
    print("--- Ex10 ---", ex10_m1(2024, 2), ex10_m2(2023, 2), ex10_m3(1900, 2), ex10_m4(2000, 12))
    print("--- Ex11 ---", ex11_m1("Éducation"), ex11_m2("Éducation"), ex11_m3("Éducation"))
    print("--- Ex12 ---", ex12_m1("python"), ex12_m2("python"), ex12_m3("python"),
          ex12_m4("python"), ex12_m5("python"))
    print("--- Ex13 ---", list(ex13_m1(100)), ex13_m2(100) == ex13_m3(100))
    print("--- Ex14 ---", ex14_m1([1, 2, 2, 3, 2], 2), ex14_m2([1, 2, 2, 3, 2], 2),
          ex14_m3([1, 2, 2, 3, 2], 2), ex14_m4([1, 2, 2, 3, 2], 2))
    L = [5, 2, 9, 1, 7, 2]
    print("--- Ex15 ---", ex15_m1(L), ex15_m1(L, True), ex15_m2(L), ex15_m2(L, True),
          ex15_m3(L), ex15_m4(L, True))
    print("--- Ex16 ---", ex16_m1(6), ex16_m2(6), ex16_m3(6), ex16_m4(6))
    print("--- Ex17 ---", ex17_m1([10, 20, 30]), ex17_m2([10, 20, 30]),
          ex17_m3([10, 20, 30]), ex17_m4([10, 20, 30]))
    print("--- Ex18 ---", ex18_m1(100, "C", "F"), ex18_m2(212, "F"),
          celsius_vers_fahrenheit(37), fahrenheit_vers_celsius(98.6))
    print("--- Ex19 ---", ex19_m1(12345), ex19_m2(12345), ex19_m3(12345), ex19_m4(12345), ex19_m3(0))
    ph = "Zèbre pomme École banane Arbre"
    print("--- Ex20 ---", ex20_m1(ph), ex20_m2(ph), ex20_m3(ph))
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("--- Ex21 ---", ex21_m1(A, B), ex21_m2(A, B), ex21_m3(A, B))
    print("--- Ex22 ---")
    ex22_m1([4, 8, 15], 8); ex22_m2([4, 8, 15], 99); ex22_m3([4, 8, 15], 15); ex22_m4([4, 8, 15], 3)
    t = "Esope reste ici et se repose"
    print("--- Ex23 ---", ex23_m1(t), ex23_m2(t), ex23_m3(t), ex23_m3("python"))
    print("--- Ex24 ---", ex24_m1(153), ex24_m2(153), ex24_m3(154), narcissiques_jusqua(10000))