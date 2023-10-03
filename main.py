#
# while True:
#     try:
#         x = int(input())
#         x += 4
#         print(x)
#         break
#     except ValueError:
#         print("Лучше введите число")

try:
    with open('text.txt', 'r') as f:
        f.read()

except FileNotFoundError:
    print('Файл не найден')