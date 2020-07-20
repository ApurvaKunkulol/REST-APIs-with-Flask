import functools

user = {"username": "Apurva", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"{user['username']} is not an admin."
    return  secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
