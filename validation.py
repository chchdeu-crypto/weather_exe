def check_not_empty_input(txt):
    return txt !="" 

def check_len_input(txt):
    return len(txt)==2

def raise_on_empty():
    raise ValueError("input ust not be empty")

def raise_on_len():
    raise ValueError("input most contine 2 letters")

def check_if_us(txt):
    return txt == "US"