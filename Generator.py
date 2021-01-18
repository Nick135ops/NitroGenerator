import random
import string
def NitroCode():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'
print(NitroCode())
