def cache(func_ref):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]
        result = func_ref(number)
        log[number] = result

        return result
    wrapper.log = log
    return wrapper