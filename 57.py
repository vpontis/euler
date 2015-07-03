from fractions import Fraction

levels = {}

def expandedSqrt(lvl):
    expanded = 1 + Fraction(1, 2)
    for i in range(1, lvl):
        levels[i] = expanded
        expanded = 1 + Fraction(1, 1 + expanded)
    return expanded


expandedSqrt(1000)

print sum(map(lambda x: len(str(x.numerator)) > len(str(x.denominator)), levels.values()))