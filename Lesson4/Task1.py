# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from decimal import Decimal, ROUND_CEILING

n = input('Введите число которое нужно округлить: ')
number = Decimal(n)
m = input('Введите число вида 0.000, количество нулей после точки показывает точность округления: ')
print(f'при d = {m},{n} = {number.quantize(Decimal(m), ROUND_CEILING)}')
