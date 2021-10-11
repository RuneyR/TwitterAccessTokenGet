import sys
import time
import ReadandWrite

import tweepy

# Auth tokens. The First Index in file is for key, 2nd is for secret.
ReadandWrite.check_ck_file()
consumer_stuff = ReadandWrite.get_consumer_keys()
consumer_key = consumer_stuff[1]
consumer_secret = consumer_stuff[2]
if not consumer_key.find('Replace') & consumer_secret.find('Replace'):
    sys.exit("Please read " + ReadandWrite.cKeys + " and follow instructions.")
    time.sleep(5)
# Start session by logging into handler Dev account.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Request access to account via Twitter OAUTH. User must sign in and give shown verification code to continue.
try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepyException:
    sys.exit('Error! Failed to get request token. Ensure the file is written to!')
    time.sleep(5)

print("Follow the link and sign in. Once signed in, copy and paste the code given below.\n")
try:
    verifier = input('Input Digit Code given by Twitter below\n')
    auth.get_access_token(verifier)
except tweepy.TweepyException:
    sys.exit('Verification error. Please try again and ensure Twitter code is correct. Exiting...')
    time.sleep(5)

print("\nTake a screenshot now. If you miss it, run the program again, there is no harm in it.\n")
ReadandWrite.write_token(auth.access_token, auth.access_token_secret)
print(auth.access_token)
print(auth.access_token_secret)
time.sleep(10)
