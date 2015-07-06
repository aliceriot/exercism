#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    if (what.strip() == ""):
        return 'Fine. Be that way!'
    elif (what.upper() == what and what.lower() == what):
        if (what.strip()[-1] == '?'):
            return 'Sure.'
        return 'Whatever.'
    elif (what.upper() == what):
        return 'Whoa, chill out!'
    elif (what.strip()[-1] == '?'):
        return 'Sure.'
    elif (what.upper() == what and what.lower() != what):
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
    return
