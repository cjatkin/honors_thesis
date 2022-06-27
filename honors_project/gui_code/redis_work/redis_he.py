#https://betterprogramming.pub/getting-started-with-redis-a-python-tutorial-3a18531a73a6

import redis

r = redis.Redis(host = 'localhost', port=6379, db=1)

r.set('hello', '3')
value = r.get('hello')
print(value)

r.delete('hello')
print(r.get('hello'))
