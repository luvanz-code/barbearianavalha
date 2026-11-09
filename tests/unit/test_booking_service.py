import pytest
from app.services.booking_service import BookingService

def test_booking_success():
    service = BookingService()
    res = service.book_slot("Carlos Silva", "41999998888", "Corte + Barba", "2026-11-10 14:15")
    assert res['status'] == 'AGENDADO'

def test_double_booking_prevention():
    service = BookingService()
    service.book_slot("Carlos Silva", "41999998888", "Corte + Barba", "2026-11-10 14:15")
    with pytest.raises(ValueError, match="Horario indisponivel"):
        service.book_slot("Marcos Outro", "41988887777", "Corte", "2026-11-10 14:15")
