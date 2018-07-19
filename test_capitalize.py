import pytest
def capital_case(x):
	if not isinstance(x, str):
		raise TypeError('Please provide a string argument')
	return x.capitalize()
def test_capitalize_case():
	assert capital_case('semphore') == 'Semphore'

def test_raises_exception_on_non_string_arguments():
	with pytest.raises(TypeError):
		capital_case(9)