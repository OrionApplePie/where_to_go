from pytils import translit

MAX_SLUG_LENGTH = 128


def slugify(title=""):
    return translit.slugify(title)[:MAX_SLUG_LENGTH].replace("-", "_")
