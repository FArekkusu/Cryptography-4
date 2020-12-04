# Cryptography-4

This script generates random passwords, computes their hashes, and writes those to separate `.csv` files.

## Password generation

For password generation the following 4 functions are used:

* `top_100_picker` - picks a random password from the list of [100 most common passwords](https://github.com/FArekkusu/Cryptography-4/blob/main/words/top_100.txt) (default chance - 10%)
* `top_100k_picker` - picks a random password from the list of [100,000 most common passwords](https://github.com/FArekkusu/Cryptography-4/blob/main/words/top_100k.txt) (default chance - 65%)
* `random_generator` - generates a random password consisting of 10-20 lowercase and uppercase letters of the English alphabet, and digits (default chance - 5%)
* `humanlike_generator` - generates a "human-like password" (default chance - 20%)

### Human-like passwords

"Human-like passwords" generator creates strings of text resembling passwords which humans tend to come up with. The generation algorithm works as follows:
1. A "minimum desired length" is picked in range `[8; 12]`
2. Several words are selected randomly from a list of [3,000 most common words](https://github.com/FArekkusu/Cryptography-4/blob/main/words/common_words.txt) until their total length becomes greater or equal to the minimum desired length
3. All of the selected words are turned to lowercase, uppercase, or capitalcase (each option has an equal chance to be picked), and then concatenated
4. A number is appended to the password with a certain chance:
    * 25% chance of appending a number in range `[0; 999]`
    * 25% chance of appending a number in range `[1970; 2000]`

## Password hashing

For password hashing the following 3 algorithms are used:

* [MD5](https://en.wikipedia.org/wiki/MD5) (using the [haslib](https://docs.python.org/3/library/hashlib.html) library)
* [SHA-1](https://en.wikipedia.org/wiki/SHA-1) (using the [haslib](https://docs.python.org/3/library/hashlib.html) library; salt is additionaly generated using the [secrets](https://docs.python.org/3/library/secrets.html) library and appended to the password before hashing)
* [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) (using the [bcrypt](https://github.com/pyca/bcrypt/) library)

The generated password hashes can be found [here](https://github.com/FArekkusu/Cryptography-4/tree/main/generated_hashes).
