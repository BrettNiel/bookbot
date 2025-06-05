
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