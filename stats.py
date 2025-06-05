
def num_of_words(text):
    count = 0
    text = text.split()

    for word in text:
        count += 1
    return count

def count_of_each_character(text):
    new_dict = {}

    for character in text:
        character = character.lower()
        if character in new_dict:
            new_dict[character] += 1
        else:
            new_dict[character] = 1
    
    return new_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(dict):
    dict_list = []

    for item in dict:
        new_dict = {}
        num = dict[item]

        new_dict.update({"char": item, "num": num})
        dict_list.append(new_dict)
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list