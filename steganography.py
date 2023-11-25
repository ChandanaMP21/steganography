# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:22:35 2023

@author: chand
"""

from cryptography.fernet import Fernet
import cv2
import os

def encrypt(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# Read the image
img = cv2.imread("img.jpg")

# Get user input
msg = input("Enter the secret message you want to send: ")
password = input("Enter the password: ")

# Generate a key from the password
key = Fernet.generate_key()

# Encrypt the message
encrypted_message = encrypt(msg, key)

# Embed the encrypted message in the image
flat_img = img.flatten()
for i in range(len(encrypted_message)):
    flat_img[i] = encrypted_message[i]

# Reshape the image back to its original dimensions
img = flat_img.reshape(img.shape)

# Save the modified image
cv2.imwrite("Encryptedmsg.jpg", img)

# Open the encrypted image
os.system("start Encryptedmsg.jpg")

print("***************************")
#decryption
print("Starting decryption....")

# Get password for decryption
pas = input("Enter passcode for Decryption: ")

# Check if the password is valid
if password == pas:
    # Extract the encrypted message from the image
    extracted_message = flat_img[:len(encrypted_message)]

    # Decrypt the message
    decrypted_message = decrypt(bytes(extracted_message), key)
    print("Decrypted message:", decrypted_message)
else:
    print("Not a valid key")