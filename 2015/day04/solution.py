import hashlib

def part1_naive(priv_key_prefix: str) -> int:
    suffix = 1
    while True:
        # Encode to bytes before use with hashlib
        h = hashlib.md5()
        encoded_text_to_hash = (priv_key_prefix + str(suffix)).encode()
        h.update(encoded_text_to_hash)
        digest = h.hexdigest()
        if digest.startswith("00000"):
            return suffix
        suffix += 1
    

if __name__=="__main__":
    priv_key_prefix = 'yzbqklnj'
    print(part1_naive(priv_key_prefix))