def decorator(func):
    with open (str(func.__name__)+'.txt', 'w') as file:
        file.write(str(func))
        file.close()
