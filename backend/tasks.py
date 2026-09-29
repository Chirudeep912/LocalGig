tasks = []


def create_task(gig_id, worker_id):
    task = {
        "gig_id": gig_id,
        "worker_id": worker_id,
        "status": "Open"
    }

    tasks.append(task)

    return task


def update_task_status(task, status):
    task["status"] = status

    return task
