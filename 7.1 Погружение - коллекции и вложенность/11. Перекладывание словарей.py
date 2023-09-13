order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for elem in order:
    order_converted_dict = {}
    for key, value in elem.items():
        if key == "skolko":
            converted_key = "count"
            converted_value = int(value)
            order_converted_dict[converted_key] = converted_value
        elif key == "poroda":
            converted_key = "specie"
            converted_value = value.title()
            order_converted_dict[converted_key] = converted_value
        elif key == "sred_razmer":
            converted_key = "avg_size"
            converted_value = int(value / 10)
            order_converted_dict[converted_key] = converted_value

    order_converted.append(order_converted_dict)


# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)