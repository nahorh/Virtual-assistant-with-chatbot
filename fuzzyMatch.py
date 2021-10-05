from fuzzywuzzy import fuzz


def match(orignal, recognized):
    ratio = fuzz.token_set_ratio(orignal, recognized)
    # print(ratio)
    if ratio >= 90:
        return True
    else:
        return False


# print(match('tell me the weather of ', 'tell me the weather of nasik'))

# print(match('open start youtube','open start word'))
