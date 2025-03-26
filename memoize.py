import urllib.request

def cache(f):
    cache_data = {}
    def wrapper(*args):
        if args in cache_data:
            return cache_data[args]
        data = f(*args)
        cache_data[args] = data
        return data
    return wrapper

@cache
def fetch(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    fib(40)
