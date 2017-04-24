items = "223,254,233".split(",")

for count, item in enumerate(items, start=1):
    print(count, " - ", item)

print('there were {0} items printed'.format(count))
