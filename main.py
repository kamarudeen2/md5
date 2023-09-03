import hashlib

def generate_md5(input):
    md5 = hashlib.md5()
    md5.update(input.encode())
    return md5.hexdigest()

input = "dawodu"
md5_show = generate_md5(input)
print(f"md5 Hash: {md5_show}")