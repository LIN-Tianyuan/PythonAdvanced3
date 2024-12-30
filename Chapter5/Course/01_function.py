"""
def welcome():
    print("Bienvenue au parc d'attactions, veuillez montrer votre ticket.")
    return None


def check(people):
    return

welcome()
"""


def check_age(age):
    if age > 18:
        return 'SUCCESS'
    return None


result = check_age(19)
if not result:
    print("Can not enter.")