from datetime import datetime

class Appointment:
    def __init__(self, id, client_name, client_phone, service_name, scheduled_at, status='AGENDADO', payment_method=None):
        self.id = id
        self.client_name = client_name
        self.client_phone = client_phone
        self.service_name = service_name
        self.scheduled_at = scheduled_at
        self.status = status
        self.payment_method = payment_method
