# Python Google API Challenge

## Setup:

- Create new Gmail account
- Enable Gmail API for the Gmail account you just created

![enter image description here](https://github.com/j-dorty/recruitment_challenge/blob/master/DevOps_201909/assets/enable-gmail-api.png)

- Create new project

![enter image description here](https://github.com/j-dorty/recruitment_challenge/blob/master/DevOps_201909/assets/create_project.PNG)

- Create Credentials

![enter image description here](https://github.com/j-dorty/recruitment_challenge/blob/master/DevOps_201909/assets/create_credentials.PNG)

- Create O Auth 2.0 client_id

![enter image description here](https://github.com/j-dorty/recruitment_challenge/blob/master/DevOps_201909/assets/create_credentials.PNG)

## Execution:

### Send Mail:

     python .\send_email.py <Destination Email> <Email Subject> <Email Body> (Optional -F <Path to File attachtments>)

Required Args:

- Destination Email - The email address to send an email to {str}
- Email Subject - The subject of the email {str}
- Email body - The body of the email {str}

Optional Args:

- Email attachments - Include -F / --files flag - Follow with path to attachment files - multiple attachments supported

Output:
None

### Search Mail:

    python .\search_email.py <Query>

Required Args:

- Query - query to use as search operator - Follows advanced search syntax documented [here](https://support.google.com/mail/answer/7190)

Output:
Emails matching the query parameter are printed to console.
Information outputted follows:

    To: <Destination Email>
    From: <Origin Email>
    Subject: <Email Subject>
    Date: <Day>, <Date (dd, mm, yyyy)> <Time (hh:mm:ss)>
    Email body: <Email Body>
    --------------------------------------------------

Example output

    PS C:\Users\edohjac\Documents\recruitment_challenge\DevOps_201909> python .\search_email.py "test"
    To: haenselamsrecruitmentchallenge@gmail.com
    From: haenselamsrecruitmentchallenge@gmail.com
    Subject: jack
    Date: Tue, 23 Aug 2022 15:37:49 -0500
    Email body: test
    --------------------------------------------------
    To: haenselamsrecruitmentchallenge@gmail.com
    From: haenselamsrecruitmentchallenge@gmail.com
    Subject: hello
    Date: Tue, 23 Aug 2022 14:44:19 -0500
    Email body: This is a test email
    --------------------------------------------------

- a brief documentation of your steps in terms what is needed to setup this API connection, PLEASE in your words not just copy & paste from google
