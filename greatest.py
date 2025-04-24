from solution import find_greatest
import os

answer = find_greatest(os.getcwd()+"/docs/2025budget.pdf")
print(f"The greatest number found in the document is: {answer}")