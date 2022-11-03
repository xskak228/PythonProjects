
# работа с JSON файлами
import json

with open("settings.json") as f:
    data = json.load(f)

    print(data["PrimeT"])
    data["PrimeT"] = True   # изменяем значение с ключом "standartDB_path"

    with open("settings.json", "w") as f:
        json.dump(data, f, indent=4)    # запись в JSON файл нового значения

