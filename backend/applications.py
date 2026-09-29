applications = []


def apply_for_gig(worker_id, gig_id, proposal):
    application = {
        "worker_id": worker_id,
        "gig_id": gig_id,
        "proposal": proposal,
        "status": "Pending"
    }

    applications.append(application)

    return application


def get_applications():
    return applications
