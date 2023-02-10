'''
and
or
not
(and)
A           b           c       result
true      true         true       true
F           f           t          f
t           f            f         f
f           f           f          f
t          t            f          f

(or)
A        B            C          Result
T       T             T            T
T       f             F            T
F       F             T            T
F       F             F            F 

'''


print((10 > 5) and (20 < 100) and (100 > 0) and (400 < 200))


print((10 < 5) or (20 > 100) or (100 > 0) or (400 < 200))

print(10 >= 50 or 200 <= 50 or 1000 < 0 )

print(20 > 40 and 70 > 50 or 40 > 200  )