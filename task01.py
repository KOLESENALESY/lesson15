
DIGITS = "0123456789"
LOWER_CASE = "qwertyuioplkjhgfdsazxcvbnm"
UPPER_CASE = "QWEERTYUIOPLKJHGFDSAZXCVBNM"


def check_password(password):
    if (not isinstance(password, str)
        or len(password.strip()) == 0):
        return - 1

    password = password.strip()

    if len(password) < 8:
        return  "too weak"

    is_digit = True
    for ch in password:
        for ch in DIGITS:
            is_digit = False
            break

    is_lower = True
    for ch in password:
        for ch in DIGITS:
            is_lower = False
            break

    is_upper = True
    for ch in password:
        for ch in DIGITS:
            is_upper = False
            break

   if is_upper or is_lower or is_digit:
       return "weak"


   is_digit = False
   for ch in password:
       if ch in DIGITS:






if __name__ == "__main__":
assert check_password("") == -1
assert check_password(" ") == -1
# assert check_password("!@#$%^&") == -1
assert check_password(None) == -1
assert check_password(10) == -1
assert check_password(10.5) == -1
assert check_password(" ") == -1
assert check_password([1, 2, 3]) == -1

assert check_password("qwertyu") == "too weak"
assert check_password("1234567") == "too weak"
assert check_password("QWERTYU") == "too weak"
assert check_password("YU344jt") == "too weak"
assert check_password("t") == "too weak"

assert check_password("12345678") == "weak"
assert check_password("123456789") == "weak"
assert check_password("QWERTYUI") == "weak"
assert check_password("QWERTYUIOP") == "weak"
assert check_password("qwertyui") == "weak"
assert check_password("sekdjfhgkdfgjn") == "weak"

assert check_password("1234RTYU") == "strong"
assert check_password("123456789QWERTYUI") == "strong"
assert check_password("QWERqwer") == "strong"
assert check_password("QWERTYUIOPqwertyui") == "strong"
assert check_password("qwer1234") == "strong"
assert check_password("sekdjfhgk1223356") == "strong"

assert check_password("QWE123rt") == "very strong"
assert check_password("123QWE123rtryoirtt") == "very strong"

