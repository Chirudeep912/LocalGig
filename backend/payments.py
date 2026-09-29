payments = []


def make_payment(client_id, worker_id, amount):
    payment = {
        "client_id": client_id,
        "worker_id": worker_id,
        "amount": amount,
        "status": "Completed"
    }

    payments.append(payment)

    return payment


def get_payment_history():
    return payments
