import sys

# Читаем все строки из stdin и убираем лишние пробелы
lines = sys.stdin.read().splitlines()

# Обрабатываем и выводим строки (каждую в обратном порядке)
for line in lines:
    print(line[::-1])