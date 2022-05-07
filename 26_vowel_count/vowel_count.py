def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    dictionary = "aeiou"
    lower_phrase = phrase.lower()
    vowel_dict = {}

    for letter in lower_phrase:
        if letter in vowel_dict:
            vowel_dict[letter] += 1
        elif letter in dictionary:
            vowel_dict[letter] = 1

    return vowel_dict

print(vowel_count("HOW ARE YOU? I am great!"))
