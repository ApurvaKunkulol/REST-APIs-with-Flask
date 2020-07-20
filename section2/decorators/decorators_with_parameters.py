import functools

user = {"username": "Apurva", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"{access_level} level access is not available to {user['username']}."
        return  secure_function
    return decorator



@make_secure("admin")
def get_admin_password_2():
    return "admin : 1234"


@make_secure("user")
def get_dashboard_password():
    return "user : user_password"


print(get_admin_password())
print(get_secure_password("billing"))


"""
    The primary reason to include "*args and **kwargs" in the decorator is
    that the decorator is then not tightly coupled with the function that it is
    used for.
    It will enhance the function regardless of whether it uses parameters.
"""
