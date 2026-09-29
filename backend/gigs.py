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


def search_gigs(keyword):
    results = []

    for gig in gigs:
        if keyword.lower() in gig["title"].lower():
            results.append(gig)

    return results
