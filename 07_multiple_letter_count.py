def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    #can make dict comprehension here by passing in 0 as second arg to .get

    freqs = {}

    for letter in phrase:
        if freqs.get(letter) == None:
            freqs[letter] = 1
        else:
            freqs[letter] += 1

    return freqs