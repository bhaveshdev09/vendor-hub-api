import uuid


def get_random_code():
    """
    The function `random_code` generates a random code with 12 chars using the UUID library in Python.
    :return: The code is returning the last part of a randomly generated UUID.
    """
    return str(uuid.uuid4()).split("-")[-1]
