"""
File: password_hashing.py
Author: Kelli Muldoon
Date: October 22, 2026
Project: CS 461 - Password Manager
Activity: Argon2 Password Hashing Tutorial

Description:
This script demonstrates password hashing and verification using Argon2id.

Argon2 is designed to make brute-force attacks more expensive by
requiring memory and processing time. The encoded hash string contains
the algorithm parameters, salt, and hash.

This script ONLY demonstrates password hashing and verification.
It does not implement a user interface, database integration, or
vault encryption. Hashing is one-way and does not encrypt or decrypt data.

AI Usage Statement:
ChatGPT was used to review the code and create ciations.
The code was reviewed and adapted for this tutorial activity.

Reference:
[Argon2 Python Tutorial — YouTube search result](https://www.bing.com/videos/riverview/relatedvideo?q=argon2+python+tutorial)
"""

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, InvalidHashError

ph = PasswordHasher()

password = "jjj"
password_hash = ph.hash(password)

print(f"Password: {password}")
print(f"Hashed Password: {password_hash}")


def login(user, password: str) -> bool:
    try:
        ph.verify(user.password_hash, password)
    except (VerificationError, InvalidHashError):
        return False

    # Check whether the hash needs to be upgraded.
    if ph.check_needs_rehash(user.password_hash):
        user.password_hash = ph.hash(password)
        # A real application must save the updated hash to its database.

    return True


# Simple test user to demonstrate login verification.
class User:
    def __init__(self, password_hash: str):
        self.password_hash = password_hash


user = User(password_hash)

print("\nLogin Tests")
print(f"Correct password accepted: {login(user, 'jjj')}")
print(f"Incorrect password accepted: {login(user, 'wrong-password')}")
