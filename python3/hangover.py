# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
import secrets


def get_dotenv():
    """ Load environment variables from a .env file. """
    from dotenv import load_dotenv
    load_dotenv()
    return os.environ


def get_log_path(filename):
    """ Get the path for the log file. """
    return os.path.join(os.path.dirname(__file__), filename)


def sh(command):
    """ Execute a shell command and return the output. """
    return subprocess.check_output(command, shell=False)


# Load environment variables and log file path
dotenv = get_dotenv()
TWILIO_ACCOUNT_SID = dotenv['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = dotenv['TWILIO_AUTH_TOKEN']
LOG_FILE_PATH = get_log_path('hangover.txt')


def main():
    # Exit early if any session with my_username is found.
    if any(s.startswith('my_username ') for s in sh('who').decode('utf-8').split('\n')):
        return

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Phone numbers.
    my_number = '+xxx'  # Replace with your number
    number_of_boss = '+xxx'  # Replace with the boss's number

    excuses = [
        'Locked out',
        'Pipes broke',
        'Food poisoning',
        'Not feeling well',
        'Having car issues, won\'t make it in',
        'Childcare fell through, need to stay home',
        'Unexpected home emergency, can\'t come in',
        'Severe weather making it unsafe to travel',
        'Have a last-minute doctor\'s appointment',
        'Suffering from a severe migraine',
        'Family emergency came up unexpectedly',
        'Experiencing an allergic reaction, need to see a doctor',
        'Power outage at home, can\'t work remotely',
        'Internet is down, unable to work remotely',
        'Pet needs to be taken to the vet urgently',
        'Lost my keys, can\'t leave the house',
        'Experiencing severe back pain, unable to come in',
        'Have to deal with a sudden dental issue',
        'Public transportation strike, no way to commute'
    ]

    try:
        # Send a text message.
        client.messages.create(
            to=number_of_boss,
            from_=my_number,
            body='Gonna work from home. ' + secrets.SystemRandom().choice(excuses),
        )
    except TwilioRestException as e:
        # Log errors.
        with open(LOG_FILE_PATH, 'a') as f:
            f.write('Failed to send SMS: {}'.format(e))
        raise


if __name__ == '__main__':
    main()
