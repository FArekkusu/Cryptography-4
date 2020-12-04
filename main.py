import csv
import os
from random import choices
from password_generators import top_100_picker, top_100k_picker, random_generator, humanlike_generator
from password_hashers import hash_md5, hash_sha1_salt, hash_bcrypt

def create_generator_picker(generators_with_weights):
    generators = [x for x, _ in generators_with_weights]
    weights = [x for _, x in generators_with_weights]
    return lambda: choices(generators, weights, k=1)[0]

def generate_passwords(n, generator_picker):
    return [generator_picker()() for _ in range(n)]

def write_hashes_to_file(filename, hashes):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=hashes[0].keys())
        writer.writeheader()
        for x in hashes:
            writer.writerow(x)

if __name__ == "__main__":
    target_directory = "generated_hashes"
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    generators_with_weights = (
        (top_100_picker, 10),
        (top_100k_picker, 65),
        (random_generator, 5),
        (humanlike_generator, 20)
    )
    generator_picker = create_generator_picker(generators_with_weights)

    for hashing_function in (hash_md5, hash_sha1_salt, hash_bcrypt):
        passwords = generate_passwords(100_000, generator_picker)
        hashes = [hashing_function(x) for x in passwords]

        filename = os.path.join(target_directory, f"{hashing_function.__name__[5:]}.csv")
        write_hashes_to_file(filename, hashes)