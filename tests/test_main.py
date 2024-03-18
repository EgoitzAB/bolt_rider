import pytest
from unittest.mock import patch, call
from src.main import main

@patch('src.cost_and_benefit.viabilidad_reparto.download_get_pdf')
@patch('src.cost_and_benefit.viabilidad_reparto.save_pdf')
@patch('src.cost_and_benefit.viabilidad_reparto.get_tariff_price')
@patch('src.cost_and_benefit.viabilidad_reparto.format_tariff_price')
@patch('src.cost_and_benefit.viabilidad_reparto.save_prices')
@patch('src.cost_and_benefit.viabilidad_reparto.get_today_price')
@patch('src.cost_and_benefit.viabilidad_reparto.get_load_cost')
def test_main(mock_get_load_cost, mock_get_today_price, mock_save_prices, mock_format_tariff_price, mock_get_tariff_price, mock_save_pdf, mock_download_get_pdf):
    # Set up the mock methods
    mock_download_get_pdf.return_value = 'file'
    mock_save_pdf.return_value = 'pdf'
    mock_get_tariff_price.return_value = 'tariff'
    mock_format_tariff_price.return_value = 'formatted'
    mock_save_prices.return_value = 'saved'
    mock_get_today_price.return_value = 'today_price'
    mock_get_load_cost.return_value = 'load_cost'

    main()

    # Check that the methods were called in the correct order
    calls = [call('file'), call('pdf'), call('tariff'), call('formatted'), call('saved'), call('today_price')]
    mock_download_get_pdf.assert_has_calls(calls)

@patch('src.cost_and_benefit.viabilidad_reparto.get_today_price')
@patch('src.cost_and_benefit.viabilidad_reparto.get_load_cost')
def test_main(mock_get_load_cost, mock_get_today_price):
    # Set up the mock methods
    mock_get_today_price.return_value = "2000"
    mock_get_load_cost.return_value = 4.0

    # Call the main function
    result = main()

    # Check that the result is as expected
    expected_result = 4.0
    assert result == expected_result