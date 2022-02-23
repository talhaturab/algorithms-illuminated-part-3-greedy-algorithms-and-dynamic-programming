from audioop import reverse

from numpy import sort


dict = {
    "a" : []
}

if "a" in dict:
    dict["a"].append((10, 17))
    dict["a"].append((5, 9))
    dict["a"].append((10, 18))
    dict["a"].append((20, 1))

for weight, length in sorted(dict['a'], reverse=True, key=lambda x: x[0]):
    print(weight, length)

# dict["a"].sort()
# print(dict["a"])

# for element in dict:
#     if len(dict[element]) > 1:
#         for item in sorted(dict[element], reverse=True, key=lambda x: x[0]):
#             print(item)

