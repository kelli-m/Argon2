# Argon2
Argon2 is a password-hashing algorithm designed to make password guessing more computationally expensive. It is memory-hard, meaning it requires a configurable amount of memory as well as processing time. This makes brute-force attacks more expensive.

This project demonstrates how to use Argon2 in Python to hash and verify passwords. I chose this tutorial because our CS 461 team is developing an open-source password manager, and protecting the user's master password is an important part of the project's security.

Argon2 is a password-hashing algorithm designed to make password guessing more computationally expensive. It is memory-hard, meaning it requires a configurable amount of memory as well as processing time. This makes brute-force attacks more expensive.

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install the library

```bash
python -m pip install argon2-cffi
```

## Basic Usage

Import `PasswordHasher` from the `argon2` package:

```python
from argon2 import PasswordHasher

ph = PasswordHasher()

password = "example-password"
hashed_password = ph.hash(password)

print(hashed_password)
```

Run the Python file to generate a password hash.

### How Argon2 Works

Argon2 produces an encoded string containing the algorithm parameters, salt, and password hash. This allows the library to verify a password later using the stored hash without storing the original password.

Argon2 generates a random salt automatically when hashing a password. As a result, hashing the same password multiple times can produce different encoded strings.

To verify a password:

```python
ph.verify(hashed_password, password)
```

The library returns `True` if the password matches the hash. If it does not match, verification raises an exception that should be handled by the application.


## References

- [MojoAuth: Argon2 in Python](https://mojoauth.com/security-guides/argon2-in-python)
- [Argon2 Python Tutorial — YouTube search result](https://www.bing.com/videos/riverview/relatedvideo?q=argon2+python+tutorial)
