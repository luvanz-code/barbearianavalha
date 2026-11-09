import re

class BookingService:
    def __init__(self):
        self.appointments = []

    def validate_phone(self, phone: str) -> bool:
        \"\"\"Valida formato de celular brasileiro com DDD (10 ou 11 digitos).\"\"\"
        digits = re.sub(r'\D', '', phone)
        return len(digits) in (10, 11)

    def book_slot(self, client_name: str, client_phone: str, service_name: str, scheduled_at: str):
        if not client_name or not client_name.strip():
            raise ValueError("Nome do cliente e obrigatorio.")
        if not client_phone or not self.validate_phone(client_phone):
            raise ValueError("Numero de telefone invalido. Informe o DDD e o numero.")
        
        # Verificacao de double-booking (concorrencia de horario)
        for app in self.appointments:
            if app['scheduled_at'] == scheduled_at and app.get('status') != 'CANCELADO':
                raise ValueError("Horario indisponivel (double-booking).")

        new_app = {
            'client_name': client_name.strip(),
            'client_phone': client_phone.strip(),
            'service_name': service_name,
            'scheduled_at': scheduled_at,
            'status': 'AGENDADO'
        }
        self.appointments.append(new_app)
        return new_app
