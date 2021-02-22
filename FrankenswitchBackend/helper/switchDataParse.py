# Taken from Google's quickstart https://developers.google.com/sheets/api/quickstart/python
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pprint

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.scripts', 'https://www.googleapis.com/auth/script.external_request']
# Switch database
# https://docs.google.com/spreadsheets/d/1TJAIiWmwYkhnI_w5xcOl_RRXZvgYcJoAfOxHFholcFE/edit#gid=1735254964
switch_database = '1TJAIiWmwYkhnI_w5xcOl_RRXZvgYcJoAfOxHFholcFE'
frankenswitch_sheet = '1pBggUHTHfCo-mQ4604Jeh0BoPqovvDLwEamYH-keqQ8'

# authentication
def get_sheet():
    creds = None
    token = os.path.split(os.path.dirname(__file__))[0]
    if os.path.exists(token + '/helper/token.pickle'):
        with open(token + '/helper/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()


def get_switch_info():
    sheet = get_sheet()
    # Get manufacturer and switch name
    ranges = ["Standard Switches!A6:A", "Standard Switches!C6:C", "Standard Switches!D6:D"]
    result = sheet.values().batchGet(spreadsheetId=switch_database, ranges=ranges).execute()
    values = result.get("valueRanges", [])
    if values:
        # TODO: don't index randomly like this, need to check if values[0, 1, 2] are defined
        # pprint.pprint(values)
        return values[0]["values"], values[1]["values"], values[2]["values"]


def insert_frankenswitch(top, stem, bottom):
    sheet = get_sheet()
    values = [
        [top, stem, bottom]
    ]
    body = {
        "values": values
    }
    result = sheet.values().append(
        spreadsheetId=frankenswitch_sheet, range="Sheet1!B3:D",
        valueInputOption="RAW", body=body).execute()
    print(result)
