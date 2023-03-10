from hashlib import md5,sha1


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def make_sha1(s, encoding='utf-8'):
    return sha1(s.encode(encoding)).hexdigest()
