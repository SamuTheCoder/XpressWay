from .constants import *
from datetime import datetime

def validate_id(id: str) -> str:
    """ Validate payment ID accordying to rules """
    if not id:
        raise ValueError("Missing ID field")
    if not isinstance(id, str):
        raise ValueError(f"Invalid ID type {type(id)}. Expected string")
    
    return id

def validate_credit_card_num(credit_num: int) -> int:
    """ Validate credit car number accordying to rules """
    if not credit_num:
        raise ValueError("Missing Credit Card Number field")
    if not isinstance(credit_num, int):
        raise ValueError(f"Invalid Credit Card Number type {type(credit_num)}. Expected int")
    if len(credit_num < MIN_CREDIT_CARD_NUM_LEN):
        raise ValueError(f"Credit Card Number should have at least {MIN_CREDIT_CARD_NUM_LEN} digits")
    if len(credit_num > MAX_CREDIT_CARD_NUM_LEN):
        raise ValueError(f"Credit Card Number exceedes {MAX_CREDIT_CARD_NUM_LEN} digits")
    
    return credit_num    

def validate_cvv(cvv: int) -> int:
    """ Validate CVV accordying to rules """
    if not cvv:
        raise ValueError("Missing CVV field")
    if not isinstance(cvv, int):
        raise ValueError(f"Invalid CVV type {type(cvv)}. Expected int")
    if len(cvv != CVV_LEN):
        raise ValueError(f"CVV lenght should be of {CVV_LEN} digits")
    return cvv

def validate_expiration_date(expiration_date: str) -> str:
    """Validate the credit card expiration date according to rules."""
    
    if not expiration_date:
        raise ValueError("Missing Expiration Date field")
    
    if not isinstance(expiration_date, str):
        raise ValueError(f"Invalid Expiration Date type {type(expiration_date)}. Expected string")
    
    # Check if the format is MM/YY
    if len(expiration_date) != EXP_DATE_LEN or expiration_date[2] != '/':
        raise ValueError(f"Invalid Expiration Date format. Expected {EXP_DATE_LEN} (MM/YY)")
    
    try:
        month, year = expiration_date.split('/')
        month = int(month)
        year = int(year)
        
        # Ensure month is valid (1-12)
        if month < 1 or month > 12:
            raise ValueError("Invalid month in Expiration Date. Month must be between 01 and 12")
        
        # Convert YY to YYYY (e.g., 25 -> 2025)
        current_year = datetime.now().year
        full_year = 2000 + year
        
        # Check if the date has passed
        current_month = datetime.now().month
        if full_year < current_year or (full_year == current_year and month < current_month):
            raise ValueError("Credit card has expired")
    
    except ValueError as e:
        raise ValueError(f"Invalid Expiration Date: {e}")
    
    return expiration_date
    
