class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def invalid_domain(domain, valid_domains):
    result = True
    for domain_v in valid_domains:
        if domain.endswith(domain_v):
            result = False
            break
    return result


valid_domains = ['.com', '.bg', '.net', '.org']

while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if invalid_domain(domain, valid_domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print("Email is valid")
