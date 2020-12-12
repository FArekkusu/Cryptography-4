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

## Password cracking

### Recovering passwords

Password hashes were taken from [here](https://github.com/vladlytvynenko/crypto-labs/tree/master/lab4).

#### MD 5

Total passwords - 200,000  
Cracked with dictionary attack - 153,116 in 7.39 seconds  
Cracked with bruteforce attack - 93,216 in 30 minutes (6 hours and 18 minutes estimated to crack the rest)

#### bcrypt

Total passwords - 200,000  
Cracked with dictionary attack - 1,122 in 23 minutes (4 years estimated to crack the rest)  
Cracked with bruteforce attack - 0 in 30 minutes (bruteforce attack is infeasible)

#### Summary

MD5 is notoriously bad, and unsurprisingly it turned out to be very easy to crack - ~75% of the passwords were found with a dictionary attack in mere seconds, and it is possible to find all the preimages in only a few hours.

SHA-1 with salt - untested due to hashcat refusing to process the file. In theory, it is still easy to crack with a dictionary attack, although it will be considerably slower than cracking plain MD5 as every password-salt pair has to be checked for existence among the hashes. Bruteforce becomes very time-consuming as checking every possible combination of symbols instead of picking passwords from a known list will be even slower than that.

Bcrypt is known as a secure algorithm which takes long time to hash a password. For this reason even though a dictionary attack is possible, it'll be very slow, and a bruteforce attack is completely out of question, as checking every possible combination of letters will take years even for relatively short passwords.

From the results it is clear that the dictionary attack is very effective as it allows to recover a huge amount of password quickly even for secure algorithms like bcrypt or argon2 (not tested here). The only downside is the fact that it is not possible to crack every single password as anything that is not present in the dictionary will be skipped. Bruteforce attack has no such problem as it exhausts the list of all possible strings, but it is also a lot more time-consuming.

### Recommendations

When working on real life applications one should use secure attack-resistant hashing algorithms with high execution time and/or memory consumption such as bcrypt, or preferably argon2, as with the modern hardware any hashing function which can be executed in a fraction of a second provides practically no protection. The second issue, which is even more important, is the quality of passwords itself - the passwords should be long (12 or better 16 characters as a minimum) and unpredictable (without patterns, without padding the password with the same character to fulfill the minimum length requirement, without putting all the digits and special characters at the end of the password etc.), as a simple dictionary attack applied to a list of low-quality passwords yields results almost immediately after it is launched.
