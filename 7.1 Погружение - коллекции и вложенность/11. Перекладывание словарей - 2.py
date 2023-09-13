order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []
for i in order:
  count=int (i["skolko"])
  specie=i["poroda"].title()
  avg_size=int(i["sred_razmer"]//10)
  order_converted.append({"count": count,"specie": specie, "avg_size": avg_size})

for item in order_converted:
  for key, value in item.items():
      print(key, value)