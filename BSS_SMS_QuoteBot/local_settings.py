'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACf7fb2089305888ae689264e4ea59857b" 
AUTH_TOKEN = "b781450ee1ed151a3479eb02a5464783"
BSSSPAM_APP_SID = "AP2f25075b12123a69a251ea84de73ade3"
BSS_SPAM_ID = "+16179458208"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
