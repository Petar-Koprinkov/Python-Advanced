MIN_LENGTH = 4
DOMAINS = [".com", ".bg", ".org", ".net"]


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email.split("@")[0]) <= MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if f".{email.split('.')[-1]}" not in DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
