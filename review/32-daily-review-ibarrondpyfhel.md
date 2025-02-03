# 🚀 ibarrond/Pyfhel

![20250203193926](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20250203193926.png)

## Review
- [x] Get to know the terms used in Homomorphic Encryption
- [ ] Run the example code in the repository

## First, Get to Know the Term

Consider that I'm a beginner in the field of cryptography. Thus, the first task in getting to know the term is to understand the basic concept of Homomorphic Encryption.

1. MultDepth and Relinearization
1. WAHC
1. Hamming Distance

### MultDepth and Relinearization
- **MultDepth**（多層乘法深度）- The **number** of multiplications that can be performed on the ciphertext before it becomes too complex to decrypt
- **Relinearization**（重線性化）- A technique used to reduce the complexity of the ciphertext

The use of these techniques is to avoid the ciphertext getting too complex to decrypt.

### WAHC
- Workshop on Applied Homomorphic Cryptography
- [WAHC 2025 – 13th Workshop on Encrypted Computing & Applied Homomorphic Cryptography](https://homomorphicencryption.org/wahc-2025/)
- [Homomorphic Encryption Standard](https://homomorphicencryption.org/standard/)

### Hamming Distance
- This is a measurement of the difference between two binary strings. It can be used for password matching (if the distance is 0, the password is correct. Therefore, you don’t need to store the password in the database; you only need to store its hash)
- BFV is more suitable for Hamming Distance than CKKS

| BFV | CKKS |
| --- | ---  |
| Integer | Floating Point |

