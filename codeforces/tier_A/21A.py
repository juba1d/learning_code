import re

def is_valid_jabber_id(jabber_id):
    # Regular expression to match valid username and resource
    username_regex = r'^[\w]{1,16}$'
    
    # Splitting based on '/'
    parts = jabber_id.split('/')
    
    # If there's only one part, then there's no resource part
    if len(parts) == 1:
        username_and_hostname = parts[0]
        resource = None
    else:
        username_and_hostname = parts[0]
        resource = parts[1]
    
    # Splitting based on '@'
    username_and_hostname_parts = username_and_hostname.split('@')
    
    # If there's no '@' or more than one '@', it's invalid
    if len(username_and_hostname_parts) != 2:
        return "NO"
    
    username = username_and_hostname_parts[0]
    hostname = username_and_hostname_parts[1]
    
    # Validate username
    if not re.match(username_regex, username):
        return "NO"
    
    # Validate resource if present
    if resource is not None:
        if not re.match(username_regex, resource):
            return "NO"
    
    # Validate hostname
    if len(hostname) == 0:
        return "NO"
    
    hostname_parts = hostname.split('.')
    for part in hostname_parts:
        if not re.match(username_regex, part):
            return "NO"
    
    # Check overall length constraints
    if len(username) < 1 or len(username) > 16:
        return "NO"
    if len(hostname) < 1 or len(hostname) > 32:
        return "NO"
    if resource is not None and (len(resource) < 1 or len(resource) > 16):
        return "NO"
    
    return "YES"

# Reading input
jabber_id = input().strip()

# Checking if the Jabber ID is valid
print(is_valid_jabber_id(jabber_id))
