def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)

print(1, 2, 3, kwd1 = 23, kwd2 = 89)