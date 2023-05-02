class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ['.com', '.bg', '.net', '.org']

while True:
    email = input()
    if email == "End":
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    extension = domain.split('.')[-1]
    if extension not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following:{' ,'.join(valid_domains)}")

    print("Email is valid")
