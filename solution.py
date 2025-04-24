import re
from helper import get_multiplier
from pypdf import PdfReader

def get_pdf_text(path):
    # creating a pdf reader object
    print("Reading PDF file...")
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        # extracting text from page
        text += "\n" + page.extract_text()
    
    return text
    #smart_greatest(text)

# parses document input and returns the greatest numerical value found 
def find_greatest(doc):
    text = get_pdf_text(doc)
    print("Finding greatest number...")
    return smart_greatest(text)

#only finds plain numbers, integers and floats alike 
def basic_greatest(text):
    # find all numbers in the text using regex / (re.findall returns a list of ALL matches)
    # \d = decimal digit, ?:\.\d+ matches pattern of decimal point followed by one or more digits, \b matches word boundary 
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
    # convert to integers
    numbers = [float(num) for num in numbers]
    # return the greatest number
    return max(numbers) if numbers else None

#  EXPLANATION OF REGEX
#  lookbehind (?<!\w) ensures that the match is not preceded by a word character
    #  it won't match numbers that are part of a word, prevents duplicate matches as well
#  [+\-−]? matches an optional sign, also permissive of unicode minus sign
#  (?:\d{1,3}(?:,\d{3})+|\d+) matches numbers with and without commas
    # (?:pattern) is a non-capturing group, so it will not be included in the final match, more accurate than pattern alone 
    # \d{1,3} matches one to three digits, (?:,\d{3})+ matches a comma followed by three digits at least one or more times
        # allows 7,000 or 70,000,000 but not 70,00
    # \d+ matches one or more digits
        # extends support to numbers without commas, ie 7000
#  (?:\.\d+)? matches an optional decimal point followed by one or more digits, extends support to floats 
NUMBER_REGEX = r'(?<!\w)[+\-−]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?'

#does contextual conversion of numbers with units, wrt to section / paragraph, equally tolerant of 75,000,000.00 and 75000000.00
def smart_greatest(text):
     # Split the text into paragraphs or logical blocks
    sections = re.split(r'\n\s*\n', text.strip())  # double newline = new paragraph

    max_number = None

    for section in sections:
        multiplier = get_multiplier(section)

        # Find all numbers in the section
        number_strings = re.findall(NUMBER_REGEX, section) 
        
        # Convert to float, apply multiplier, and track max
        for num_str in number_strings:
            # Our regex matches numbers with commas (ie 75,000,000), so we need to remove them before conversion, also remove unicode minus sign
            num = float(num_str.replace(',', '').replace("−", "-") ) * multiplier

            if (max_number is None) or (num > max_number):
                max_number = num

    return max_number 