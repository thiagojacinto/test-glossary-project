import pytest
from fastapi.testclient import TestClient
from fastapi import Response

from testglossary.main import app, active_API_version

client = TestClient(app)
active_target_url = '/api/{}/terms'.format(active_API_version)

def test_should_return_an_array():
    response = client.get(active_target_url)
    assert response.status_code == 200
    assert isinstance(response.json().get('result'), list) == True


def test_should_return_status_code_200():
    response = client.get(active_target_url)
    assert response.status_code == 200


def test_should_return_404_on_not_found_resource():
    response = client.get('{}/2'.format(active_target_url))
    assert response.status_code == 404


def test_page_path_parameter_should_not_be_required():
    response_with_page = client.get('{}?page=0'.format(active_target_url))
    response_without_page = client.get('{}'.format(active_target_url))
    assert response_with_page.status_code == response_without_page.status_code
    assert response_with_page.json().get('result') == response_without_page.json().get('result')


def test_page_path_should_be_positive():
    response_with_page_negative = client.get('{}?page=-1'.format(active_target_url))
    assert response_with_page_negative.status_code == 422


def test_tests_terms_per_page_path_parameter_should_be_greater_than_one():
    response_with_invalid_terms_per_page_parameter = client.get(
        '{}?terms_per_page=0'.format(active_target_url))
    assert response_with_invalid_terms_per_page_parameter.status_code == 422


def test_terms_list_path_parameters_should_have_default_values():
    response_with_default_values = client.get(active_target_url)
    assert response_with_default_values.status_code == 200
    assert response_with_default_values.json().get('page') == 0
    assert response_with_default_values.json().get('offset') == 10


def test_terms_per_page_path_parameter_should_not_be_required():
    response_with_terms_per_page = client.get(
        '{}?terms_per_page=10'.format(active_target_url))
    response_without_terms_per_page = client.get('{}'.format(active_target_url))
    assert response_with_terms_per_page.status_code == response_without_terms_per_page.status_code
    assert response_with_terms_per_page.json().get('result') == response_without_terms_per_page.json().get('result')

def test_terms_list_response_should_have_paginated_result_structure():
    response = client.get(active_target_url)
    response_attributes = response.json()
    expected_attributes = ['result', 'page', 'offset']

    assert response.status_code == 200
    assert expected_attributes == [attribute for attribute in expected_attributes if attribute in response_attributes]


@pytest.fixture()
def search_term_by():
    def _search_term_by_name(search_term='test') -> Response:
        return client.get('{}/search/{}'.format(active_target_url, search_term))
    
    return _search_term_by_name
    
    
def test_search_term_by_name(search_term_by):
    assert search_term_by('test').status_code == 200


def test_search_term_attempt_with_more_than_30_characters(search_term_by):
    longer_sentence = 'this-is-a-longer-sentence-more-than-30-caracters'
    
    assert search_term_by(longer_sentence).status_code == 422


def test_search_term_attempt_with_less_than_3_characters(search_term_by):
    small_sentence = 'no'
    
    assert search_term_by(small_sentence).status_code == 422


def test_search_term_with_page_path_parameter_should_be_positive(search_term_by):
    page_parameter = 'aplha?page=-1'
    
    assert search_term_by(page_parameter).status_code == 422


def test_search_term_with_test_term_by_page_path_parameter_should_be_greater_than_one(search_term_by):
    page_parameter = 'aplha?terms_per_page=0'

    assert search_term_by(page_parameter).status_code == 422

def test_search_term_non_existent(search_term_by):
    term_that_not_exists = 'not-a-test-term'
    response = search_term_by(term_that_not_exists)
    
    assert response.status_code == 404
    assert 'not' in response.json().get('detail').lower()