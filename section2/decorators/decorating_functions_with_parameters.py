import functools

user = {"username": "Apurva", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"{user['username']} is not an admin."
    return  secure_function


@make_secure
def get_admin_password():
    return "1234"

@make_secure
def get_secure_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_admin_password())
print(get_secure_password("billing"))


"""
    The primary reason to include "*args and **kwargs" in the decorator is
    that the decorator is then not tightly coupled with the function that it is
    used for.
    It will enhance the function regardless of whether it uses parameters.
"""
