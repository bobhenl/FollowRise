from werkzeug.security import generate_password_hash, check_password_hash


hashed = generate_password_hash("heslo123", "MD5")
print(hashed)

print(check_password_hash(hashed, "heslo123"))