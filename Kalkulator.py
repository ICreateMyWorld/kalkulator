import logging
import operator

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='mylog.log', format='%(asctime)s %(filename)s %(message)s')

dzialania = {'1': operator.add, '2': operator.sub, '3': operator.mul, '4': print}
logger.critical('Dzień dobry')

print("Podaj działanie, posługując się odpowiednią liczbą: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

dzialanie = input()
if dzialanie not in dzialania:
    raise ValueError(f'Nie ma takiego dzialania: {dzialanie}')
liczba1 = int(input("Podaj pierwsza liczbe : "))
liczba2 = int(input("Podaj druga liczbe : "))

funkcja = dzialania[dzialanie]
wynik = funkcja(liczba1, liczba2)
logger.info(f"Użyta funkcja: {funkcja.__name__=}, Liczby: {liczba1=} {liczba2=}, Wynik: {wynik=}")
