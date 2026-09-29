from users import register_user
from gigs import create_gig


def main():
    print("Welcome to LocalGig Backend")

    user = register_user(
        "Demo User",
        "demo@example.com",
        "Worker"
    )

    gig = create_gig(
        "Graphic Design",
        "Create a simple poster",
        1000
    )

    print("User:", user)
    print("Gig:", gig)


if __name__ == "__main__":
    main()