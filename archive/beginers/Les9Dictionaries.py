# Dictionaries

d = {"Ukraine": "Kyiv", "Minsk": "Belarus", "Tel-Aviv": "Israel"}
for k, v in d.items():
    print("key= " + str(k) + " : value= " + str(v))

# Task 1

print("\n----- Task 1----------")
dic = ["First", 10, 20, 30, "Second", 101, 202, "Third", 5, 6, 7, "Fourth", 11]


def is_num(num):
    if num * 0 == 0:
        return True
    else:
        return False


def list_to_map(list_val):
    index = 0
    dict_res = {}
    current_key = ""
    while index < len(list_val):
        if is_num(list_val[index]):
            dict_res[current_key].append(list_val[index])
        else:
            dict_res[list_val[index]] = []
            current_key = list_val[index]
        index += 1
    return dict_res


def list_to_map_with_type(list_val):
    index = 0
    dict_res = {}
    current_key = ""
    while index < len(list_val):
        if isinstance(list_val[index], str):
            dict_res[list_val[index]] = []
            current_key = list_val[index]
        else:
            dict_res[current_key].append(list_val[index])
        index += 1
    return dict_res


print(list_to_map_with_type(dic))
print(list_to_map(dic))

# Task 2 - count number of words in the text
my_text = "hello bye how are things hello hello melon bicycle table elephant melon yes hello"
print(len(my_text.split(" ")))  # spaces are used by default
print(my_text[0].lower())
dic2 = {"hello": 20}


def count_words(text):
    dic2_res = {}
    list_words = text.split()
    for word in list_words:
        if word in dic2_res:
            dic2_res[word] = dic2_res[word] + 1
        else:
            dic2_res[word] = 1
    return dic2_res


# very elegant solution
def count_words_v2(my_text_var):
    dict_res = {}
    for word in my_text_var.split():
        dict_res[word] = dict_res.get(word, 0) + 1
    return dict_res


print(count_words(my_text))
print(count_words_v2(my_text))
