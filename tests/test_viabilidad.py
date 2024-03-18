import pytest
from unittest.mock import patch, Mock, mock_open, MagicMock
from src.cost_and_benefit.viabilidad_reparto import *

def test_download_get_pdf():
    expected = 200
    actual = download_get_pdf()
    assert expected == actual.status_code

@patch('builtins.open', new_callable=mock_open)
def test_save_pdf(mock_open_instance):
    mock_open_instance.return_value.name = "electricity.pdf"
    mock_response = MagicMock()
    mock_response.content = b"content"
    assert save_pdf(mock_response) == "electricity.pdf"

@patch('tabula.read_pdf')
def test_get_tariff_price(mock_read_pdf):
    mock_read_pdf.return_value = [None, pd.DataFrame({"Unnamed: 1": {43: "price"}})]
    assert get_tariff_price("file") == "price"

def test_format_tariff_price():
    assert format_tariff_price('(1 0 0,1)') == 100.1

def test_format_tariff_price():
    expected = 100.1
    actual = format_tariff_price('(1 0 0,1)')
    assert expected == actual

@patch('builtins.open', new_callable=mock_open)
def test_save_prices(mock_open_instance):
    save_prices(100.1)
    mock_open_instance.assert_called_once_with('electricity_prices.csv', 'a', newline='')

@patch('builtins.open', new_callable=mock_open, read_data="month,100.1\n")
def test_get_today_price(mock_open):
    assert get_today_price() == "100.1\n"

def test_get_load_cost():
    # Define the inputs
    datos = "2000"
    load_time = 5.5
    load_capacity = (7650*36)/1000000

    result = get_load_cost(datos)
    expected_result = (float(datos) / 1000) * load_capacity * load_time
    assert result == expected_result

@patch('builtins.open', new_callable=mock_open)
def test_save_cost_of_load(mock_open):
    save_cost_of_load(0.00033165)
    mock_open.assert_called_once_with('benefit.csv', 'w+', encoding='UTF8')

def test_profit():
    assert profit(0.00033165, 100) == 99.99966835