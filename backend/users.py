users = []


def register_user(name, email, role):
    user = {
        "name": name,
        "email": email,
        "role": role
    }

    users.append(user)

    return user


def get_users():
    return users
