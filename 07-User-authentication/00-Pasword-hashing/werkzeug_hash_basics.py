from werkzeug.security import generate_password_hash, check_password_hash

password = 'supersecretpassword'

hashed = generate_password_hash(password=password)

print(hashed)

check = check_password_hash(hashed, 'wrongpassword')

print(check)

check = check_password_hash(hashed, 'supersecretpassword')

print(check)
