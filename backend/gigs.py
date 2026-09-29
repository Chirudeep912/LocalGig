gigs = []


def create_gig(title, description, budget):
    gig = {
        "title": title,
        "description": description,
        "budget": budget,
        "status": "Open"
    }

    gigs.append(gig)

    return gig


def get_gigs():
    return gigs
