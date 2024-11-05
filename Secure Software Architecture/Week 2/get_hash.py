# import Python's hash algorithm module
import hashlib

file_path = "./Sample_file.txt"  # Replace with your file path


def create_checksum(file_path):
    # call the 256 bit Secure Hashing Algorithm
    sha256_hash = hashlib.sha256()

    # open the file in read mode as a binary file
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # return the checksum as a string of hexadecimal digits
    return sha256_hash.hexdigest()


# call the create_checksum routine passing it the file path
checksum = create_checksum(file_path)

print(f"Checksum for {file_path}: {checksum}")
