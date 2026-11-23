from datetime import datetime
from PIL import Image, ImageFilter, ImageOps


filename = input("Введите имя файла для обработки (например, image1.jpg): ")

path = "Lab2_Media/data/input/" + filename

result = "Lab2_Media/data/output/result.jpg"

logs = "Lab2_Media/logs/history.txt"

filters = "Медианный фильтр + выравнивание гистограммы"

try:
    
    image = Image.open(path)
    image = image.convert("RGB")
    image = image.filter(ImageFilter.MedianFilter(size=3))#убираем шум
    image = ImageOps.equalize(image)#контраст
    image.save(result, "JPEG")

    print("Обработка выполнена успешно.")
    print("Результат сохранён здесь:")
    print(result)

    
    now = datetime.now()

    log_line = "[" + str(now) + "] Файл: " + filename + " | Фильтр: " + filters + " | Статус: Успешно\n"

    log_file = open(logs, "a", encoding="UTF-8")
    log_file.write(log_line)
    log_file.close()

except PermissionError:
    print("Ошибка: Нет прав на чтение файла " + filename + ". Обратитесь к администратору")

    now = datetime.now()

    log_line = "[" + str(now) + "] Файл: " + filename + " | Фильтр: " + filters + " | Статус: Ошибка доступа\n"

    log_file = open(logs, "a", encoding="UTF-8")
    log_file.write(log_line)
    log_file.close()

except FileNotFoundError:
    print("Ошибка: Файл не найден")

except OSError:
    print("Ошибка: Не удалось обработать файл изображения")
