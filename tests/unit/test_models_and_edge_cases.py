import pytest
from app.models.entities import Appointment
from app.services.booking_service import BookingService

def test_appointment_model_instantiation():
    """Valida a criacao da entidade Appointment com valores predefinidos."""
    app = Appointment(1, "Carlos", "41999998888", "Barba", "2026-11-10 10:00")
    assert app.id == 1
    assert app.client_name == "Carlos"
    assert app.status == "AGENDADO"
    assert app.payment_method is None

def test_booking_empty_name():
    """Valida o bloqueio de agendamento quando o nome do cliente esta vazio."""
    service = BookingService()
    with pytest.raises(ValueError, match="Nome do cliente e obrigatorio"):
        service.book_slot("", "41999998888", "Corte", "2026-11-10 14:15")
