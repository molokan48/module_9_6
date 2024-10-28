def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j : j + i + 1]


a = all_variants("abc")
for i in a:
    print(i)
# print(text[0:1])
# print(text[1:2])
# print(text[2:3])
# print(text[0:2])
# print(text[1:3])
# print(text[0:3])
#
# b = all_variants('123456789')
# for i in b:
#     print(i)