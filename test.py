import pytest
from solution import basic_greatest, smart_greatest

#tests for basic float vs integer comparison
def test_basic():
    text = """
    The revenue last year was reported as 32000. We expect a 10 percent increase this year, projected to be 35200.56. 
    """
    assert basic_greatest(text) == 35200.56

#tests detection of numbers with units, vs comma separated numbers and plain integers
def test_smart():
    text = """
    The revenue made last year was reported as 32 million. 
    
    \nWe expect a 10 percent increase this year, projected to rise to 35.2, in millions.

    \nOur competitors, in comparison made only 25,000,000 last year. They are expected to make 30000000 this year.
    """
    assert smart_greatest(text) == 35.2 * 1_000_000

#tests correct conversion and comparison of numbers with units, millions vs billions
def test_smart2():
    text = """
    The monopoloy in the industry made 35.2 billion last year. 
    
    \nIn comparison, we brought home a revenue of 32 million.
    \nOur competitors, meanwhile, made only 25,000,000 last year. They are expected to make 30000000 this year.
    """
    assert smart_greatest(text) == 35.2 * 1_000_000_000

#tests detection of comma separated numbers vs units 
def test_smart3():
    text = """
    The revenue we made last year was reported as 25 million. 
    \nOur competitors, in comparison made 35,200,000 last year.
    """
    assert smart_greatest(text) == 35.2 * 1_000_000

# tests comma separated numbers vs integer
def test_smart4():
    text = """
    The revenue we made last year was reported as 25,000,000. 
    \nOur competitors, in comparison made 35200000 last year.
    """
    assert smart_greatest(text) == 35.2 * 1_000_000

# tests detection of -+ sign in front of numbers
def test_smart4():
    text = """
    The profit we made last year was reported as -35,200,000. 
    \nOur competitors, in comparison made net profit of +25000000 last year.
    """
    assert smart_greatest(text) == 25 * 1_000_000