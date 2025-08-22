import base64

# Encode
text = "Hello World!"
encoded = base64.b64encode(text.encode())
print(encoded)  # Output: b'SGk='


# Decode
decoded = base64.b64decode(encoded).decode()
print(decoded)  # Output: 'Hi'
