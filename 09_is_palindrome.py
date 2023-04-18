def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # could also reverse the whole string and compare it

    new_phrase = phrase.lower().replace(" ","")

    end = len(new_phrase)//2
    if len(new_phrase) %2 == 0:
         end -= 1

    backhalf_backwards = new_phrase[-1:end:-1]
    fronthalf = new_phrase[0:len(new_phrase)//2]

    return backhalf_backwards == fronthalf