# greatest_number

## Setup
### Installation 
Clone/fork the repo and install dependencies with Pip: 
- `pytest` for testing: run `pip install -U pytest`
- `pypdf` for pdf parsing: `pip install pypdf`
    - `numpy` dependency: `pip install -U numpy`

### Execution 
- To run some primtive tests for the solution functions made, run `pytest test.py`. 
- To get the answer for a sample document `docs/2025budget.pdf` run `python3 greatest.py`

## Files 
- `greatest.py`: Runs the solution on sample document. 
- `solution.py`: Contains basic, and more contextual solution for number detection algorithm with text inputs. Also contains pdf parsing function.
- `test.py`: Outlines basic tests (including edge cases) for `solution.py` algorithms   
- `helper.py`: Contains helper functions for `solution.py` functions. 