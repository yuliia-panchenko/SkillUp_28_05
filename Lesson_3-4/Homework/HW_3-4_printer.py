def connection(ip, port):
    def decorator(func):
        def inner(document):
            print(f'Connected to IP: {ip}:{port}')
            func(document)
            print('=====Close connection=====')
        return inner
    return decorator


@connection(ip='10.10.10', port=5555)
def hp(document):
    print('I am HP printer')
    print(f'Printing: {document}')


@connection(ip='10.11.11', port=5577)
def canon(document):
    print('I am Canon printer')
    print(f'Printing: {document}')


hp(document='Test data')
canon(document='New document')
