# import class and constants
from ldap3 import Server, Connection, SUBTREE
import json

s = Server('my.ldap.server', port=636, use_ssl=True, get_info='ALL')  # define a secure LDAP server
conn = Connection(s, user='myLDAPUsername', password='myPassword')
conn.bind()
if not conn.bind():
    print('error in bind', conn.result)
conn.search(search_base='OU=... Users,DC=....,DC=...',
            search_filter='(objectClass=organizationalPerson)',
            search_scope=SUBTREE,
            attributes=['cn', 'SamAccountName']
            )
# Main ide was to get values from conn.response to JSON format
# So first i appended them to list. Then got list of object
elements = []
for entry in conn.response:
    elements.append(entry['attributes'])
# Internal part converts list of object to dictionary, and then dictionary is converted to JSON
json_string = json.dumps([ob.__dict__['_store'] for ob in elements])
print(json_string)
