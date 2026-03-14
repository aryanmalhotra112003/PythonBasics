import random
import string
import re

def generate_password_no_regex():
    uppers = list(string.ascii_uppercase)
    lowers = list(string.ascii_lowercase)
    digits = list(string.digits)
    specials = list("!@#$%&*")
    
    req_upper = random.sample(uppers, 1)
    req_lower = random.sample(lowers, 1)
    req_digits = random.sample(digits, 2)
    req_special = random.sample(specials, 1)
    
    mandatory = req_upper + req_lower + req_digits + req_special
    pool = list(string.ascii_letters + string.digits + "!@#$%&*")
    
    for char in mandatory:
        pool.remove(char)
        
    remaining = random.sample(pool, 11)
    password = mandatory + remaining
    random.shuffle(password)
    
    return "".join(password)

def generate_password_with_regex():
    pool = list(string.ascii_letters + string.digits + "!@#$%&*")
    
    while True:
        candidate_list = random.sample(pool, 16)
        candidate = "".join(candidate_list)
        
        if (re.search(r"[A-Z]", candidate) and 
            re.search(r"[a-z]", candidate) and 
            len(re.findall(r"\d", candidate)) >= 2 and 
            re.search(r"[!@#$%&*]", candidate)):
            return candidate


print("Password (Without Regex):", generate_password_no_regex())
print("Password (With Regex):   ", generate_password_with_regex())