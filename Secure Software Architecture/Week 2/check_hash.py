import hashlib

# Replace with your file path
file_path = "./Sample_file.txt"
# Replace with the actual expected checksum
expected_checksum = "dd878aad4826449856fd7a45a9ce619ef5fdc25bc6682d9c991a9b0ec516fa31"


def create_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def verify_checksum(file_path, expected_checksum):
    actual_checksum = create_checksum(file_path)
    return actual_checksum == expected_checksum


is_valid = verify_checksum(file_path, expected_checksum)
print(f"Is the checksum valid? {is_valid}")
