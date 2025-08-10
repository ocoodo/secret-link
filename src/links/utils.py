from hashids import Hashids

hashids = Hashids(salt="salt_is_good", min_length=8)

def generate_link_id(id: int) -> str:
    return hashids.encode(id)
