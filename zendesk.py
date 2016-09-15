# Zenpy accepts an API token

from zenpy import Zenpy

creds = {
    'email' : 'user@example.com',
    'token' : 'addyourtokenhere',
    'subdomain': 'yourzendesksubdomain'
}


# Default
zenpy = Zenpy(**creds)

# Alternatively you can provide your own requests.Session object
# zenpy = Zenpy(**creds, session=some_session)

tickets = []
gravitron = {}
for ticket in zenpy.tickets():
    tickets.append(ticket.to_dict())
    domain = (str(ticket.requester.email.split('@')[-1]))
    tickets[-1]["domain"] = domain
    if domain not in gravitron.keys():
      gravitron[domain] = ticket.tags
    else:
      gravitron[domain] = list(set(gravitron[domain]+ticket.tags))
print gravitron

for k in gravitron.keys():
  if "feature_request_deal_blocking" in gravitron[k]:
      print k, 'feature failure' 
