def vowel_filter(function):

    def wrapper():
        letters = function()
        return[x for x in letters if x.lower() in 'aeuio']
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

@vowel_filter
def get_other_letter():
    return ['n', 'U', 's']

print(get_other_letter())