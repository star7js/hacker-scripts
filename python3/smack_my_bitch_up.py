
#!/usr/bin/env python

import os
import random
from twilio.rest import Client  # Updated import for newer Twilio versions
import subprocess
import sys
from time import strftime

# Exit if no sessions with my username are found
output = subprocess.check_output('who')
if 'my_username' not in output.decode('utf-8'):  # Decoding the output for string comparison
    sys.exit()

# Returns 'None' if the key doesn't exist
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Phone numbers
my_number = '+xxx'  # Replace with your number
her_number = '+xxx'  # Replace with the recipient's number

reasons = [
  'Working hard',
  'Gotta ship this feature',
  'Someone messed up the system again'  # Changed wording for professionalism
]

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Sending the SMS
client.messages.create(
    to=her_number,
    from_=my_number,
    body="Late at work. " + random.choice(reasons)
)

# Print confirmation message
print("Message sent at " + strftime("%a, %d %b %Y %H:%M:%S"))
