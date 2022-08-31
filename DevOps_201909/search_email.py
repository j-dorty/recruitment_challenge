import base64
from utils import gmail_authenticate

from base64 import urlsafe_b64decode

def search_messages(service, query):
    """
    This function takes the Gmail APi service and the given query and:
        - Requests the service for all emails matching the query (continually if there is a next page token present)
        - compiles and returns the relevant emails in a list
    """
    result = service.users().messages().list(userId='me',q=query).execute()
    messages = [ ]
    if 'messages' in result:
        messages += result['messages']
    while 'nextPageToken' in result:
        page_token = result['nextPageToken']
        result = service.users().messages().list(userId='me',q=query, pageToken=page_token).execute()
        if 'messages' in result:
            messages +=result['messages']
    return messages

def read_message(service, message):
    """
    This function takes Gmail API `service` and the given `message_id` and:
        - Downloads the content of the email
        - Prints the email basic information (To, From, Subject, Date and Body)
    """
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    payload = msg['payload']
    headers = payload.get("headers")
    body = payload.get("body")
    parts = payload.get("parts")
    if headers:
        for header in headers:
            name = header.get("name")
            value = header.get("value")
            if name.lower() == 'from':
                print("From:", value)
            if name.lower() == "to":
                print("To:", value)
            if name.lower() == "subject":
                print("Subject:", value)
            if name.lower() == "date":
                print("Date:", value)
    
    if body and body.get("size") > 0:
        value = body.get("data")

    if parts:
        body = parts[0].get("body") # email body is always the first part of the parts of returned emails
        value = body.get("data")
    
    print("Email body:", urlsafe_b64decode(value).decode("utf-8"))


    print("-"*50)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Email Search using Gmail API")
    parser.add_argument('query', type=str, help='The search query to find desired emails')

    args = parser.parse_args()
    service = gmail_authenticate()
    messages = search_messages(service, args.query)
    
    for message in messages:
        read_message(service, message)