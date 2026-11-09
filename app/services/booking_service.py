class BookingService:
    def __init__(self):
        self.appointments = []

    def book_slot(self, client_name, client_phone, service_name, scheduled_at):
        if not client_name or not client_phone:
            raise ValueError("Nome e telefone sao obrigatorios.")
        for app in self.appointments:
            if app.scheduled_at == scheduled_at and app.status != 'CANCELADO':
                raise ValueError("Horario indisponivel (double-booking).")
        # Simula criacao
        new_app = {'client_name': client_name, 'client_phone': client_phone, 'service_name': service_name, 'scheduled_at': scheduled_at, 'status': 'AGENDADO'}
        self.appointments.append(new_app)
        return new_app
