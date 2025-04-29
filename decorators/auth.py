def is_admin(user):
    return user.get("role") == "admin"


def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if not is_admin(user):
            print("Access denied!")
            return
        return func(user, *args, **kwargs)

    return wrapper


@admin_required
def delete_user(user, username):
    # Perform delete functionality
    print(f"User '{username}' has been deleted")


u1 = {"name": "Bibek", "role": "admin"}
u2 = {"name": "Deepak", "role": "guest"}

delete_user(u2, "deepak_034")
delete_user(u1, "bibek01")