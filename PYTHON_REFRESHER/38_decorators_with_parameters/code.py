import functools
user = {"username": "Jose","access_level":"admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args,**kwargs):
            if user['access_level'] == access_level:
                return func(*args,**kwargs)
            else:
                print(f"No {access_level} right for the user {user['username']}!")
        return secure_function
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 12345"

@make_secure("guest")
def get_guest_password():
    return "user: password"

print(get_admin_password())
print(get_guest_password())

user = {"username": "Anne","access_level":"guest"}
print(get_admin_password())
print(get_guest_password())