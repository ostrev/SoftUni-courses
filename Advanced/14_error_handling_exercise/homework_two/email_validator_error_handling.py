class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


def invalid_domain(domain, valid_domains):
    for valid in valid_domains:
        if domain.endswith(valid):
            return  False
    return  True


while True:
    email = input()

    if email == "END":
        break

    if "@" not in email:
        raise  MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    valid_domains = [".com", ".bg", ".org", ".net"]

    if invalid_domain(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")