domains = ['com', 'bg', 'net', 'org']


class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    adress = input()
    if adress == 'End':
        break
    if '@' not in adress:
        raise MustContainAtSymbolError('Email must contain @')
    name, email = adress.split("@")
    if len(name)<=4:
        raise NameTooShortError('Name must be more than 4 characters')
    _, domain = email.split(".")
    if domain not in domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print("Email is valid")