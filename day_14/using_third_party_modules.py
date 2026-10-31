import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(f"Status code is:", r.status_code)

r = requests.get('https://httpbin.org/get')
print(f"Status code is:", r.status_code)
print(r.text)
