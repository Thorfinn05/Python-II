import csv

new_data = [
    ["South Africa", "949", "575", "331", "9", "34"],
    ["New Zealand", "987", "513","424", "9", "41"]
]
f = open("details.csv", "a", newline="")
write = csv.writer(f)
write.writerows(new_data)