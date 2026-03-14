import ipaddress
import re

def validate_public_ipv4(ip_string):
    try:
        ip_obj = ipaddress.IPv4Address(ip_string)
        
        if ip_obj.is_private:
            return False, f"Error: '{ip_string}' is a valid IPv4 format, but it is a PRIVATE address, not public."
        elif ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_multicast:
            return False, f"Error: '{ip_string}' is a reserved/loopback address, not a public IP."
            
        return True, f"Success: '{ip_string}' is a valid public IPv4 address."
        
    except ipaddress.AddressValueError:
        return False, f"Error: '{ip_string}' does not follow the correct IPv4 format."

def validate_gmail(email_string):
    if not email_string.endswith("@gmail.com"):
        return False, f"Error: '{email_string}' is invalid. It must end with '@gmail.com'."
    
    username = email_string.replace("@gmail.com", "")
    
    if len(username) < 1:
        return False, "Error: The username part before '@gmail.com' cannot be empty."
    
    if not re.match(r"^[a-z0-9.]+$", username):
        if re.search(r"[A-Z]", username):
            return False, f"Error: '{email_string}' is invalid. The username must contain only lowercase letters, no uppercase."
        else:
            return False, f"Error: '{email_string}' is invalid. The username can only contain lowercase letters, numbers, and dots (.)."
            
    return True, f"Success: '{email_string}' is a perfectly valid Gmail address."

user_ip = input("Enter an IPv4 address to validate: ")
is_valid_ip, ip_msg = validate_public_ipv4(user_ip)
print(ip_msg)
    
user_email = input("\nEnter a Gmail address to validate: ")
is_valid_email, email_msg = validate_gmail(user_email)
print(email_msg)