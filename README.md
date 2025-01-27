# LinkedinxTwitterOauth


OAuth Integration with Twitter and LinkedIn

Prerequisites
Twitter Developer Account:

Sign up for a Twitter Developer Account.
Create a new Twitter application and get the following credentials:

API Key
API Secret Key
Access Token
Access Token Secret


LinkedIn Developer Account:

Sign up for a LinkedIn Developer Account.
Create a new LinkedIn application and get the following credentials:
Client ID
Client Secret




Prerequisites
Reddit Developer Account:

Sign up for a Twitter Developer Account.
Create a new Twitter application and get the following credentials:

API Key
API Secret Key


Ensure you have Python 3.x and pip installed.

Setting Up the Project

Step 1: Install Dependencies
Install all the necessary Python packages listed in the requirements.txt file:

pip install -r requirements.txt



Step 2: Configure API Keys
Open your settings.py file and add your Twitter and LinkedIn credentials:

Twitter Configuration:
TWITTER_API_KEY = 'your_consumer_api_key'
TWITTER_API_SECRET_KEY = 'your_consumer_api_secret_key'
TWITTER_REDIRECT_URI = 'https://yourapp.com/twitter/callback'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_USERINFO_URL = 'https://api.twitter.com/1.1/account/verify_credentials.json'



LinkedIn Configuration:
LINKEDIN_CLIENT_ID = 'your_linkedin_client_id'
LINKEDIN_CLIENT_SECRET = 'your_linkedin_client_secret'
LINKEDIN_REDIRECT_URI = 'https://yourapp.com/linkedin/callback'
LINKEDIN_ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_USERINFO_URL = 'https://api.linkedin.com/v2/me'


REDDIT Configuration:
REDDIT_CLIENT_ID = 'xcjoRXPsY5_GaXe_st4Pzg'
REDDIT_CLIENT_SECRET = 'vo7bKODfebdNnieC-MF6MmI9aLWkzg'
REDDIT_REDIRECT_URI = 'http://localhost:8000/complete/reddit/callback/'
REDDIT_AUTH_URL = 'https://www.reddit.com/api/v1/authorize'
REDDIT_TOKEN_URL = 'https://www.reddit.com/api/v1/access_token'
REDDIT_USERINFO_URL = 'https://oauth.reddit.com/api/v1/me'


Step 4: Run Migrations
Apply the database migrations:

python manage.py migrate




Testing the APIs
1. Twitter OAuth
Step 1: Generate Twitter Authorization URL

Endpoint: GET /{BASE_URL}/complete/twitter/generate-url/

Action: This API returns the Twitter authorization URL that you should redirect your users to for authentication.

Example Response:

{
    "authorization_url": "https://api.twitter.com/oauth/authorize?oauth_token=xxx",
    "oauth_token": "xxx",
    "oauth_token_secret": "xxx"
}

Step 2: Handle Twitter Callback

Just call the 

authorization_url: "https://api.twitter.com/oauth/authorize?oauth_token=xxx",

Twitter will perform this authorization and hit the call back api


2. LinkedIn OAuth
Step 1: Generate LinkedIn Authorization URL

Endpoint: GET /{BASE_URL}/complete/linkedin/generate-url/

Action: This API returns the LinkedIn authorization URL that you should redirect your users to for authentication.

Example Response:
{
    "authorization_url": "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=xxx&redirect_uri=xxx&scope=r_liteprofile"
}


Step 2: Handle LinkedIn Callback

Just call the 

authorization_url: "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=xxx&redirect_uri=xxx&scope=r_liteprofile"

Linkedin will perform this authorization and hit the call back api


2. Reddit OAuth
Step 1: Generate Reddit Authorization URL

Endpoint: GET /{BASE_URL}/complete/reddit/generate-url/

Action: This API returns the Reddit authorization URL that you should redirect your users to for authentication.

Example Response:
{
    "url": "https://www.reddit.com/api/v1/authorize?response_type=code&client_id=xcjoRXPsY5_GaXe_st4Pzg&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fcomplete%2Freddit%2Fcallback%2F&scope=identity&state=random_string_for_csrf_protection&duration=temporary"
}


Step 2: Handle Reddit Callback

Just call the 

url: "https://www.reddit.com/api/v1/authorize?response_type=code&client_id=xcjoRXPsY5_GaXe_st4Pzg&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fcomplete%2Freddit%2Fcallback%2F&scope=identity&state=random_string_for_csrf_protection&duration=temporary"

Reddit will perform this authorization and hit the call back api


How to Test the APIs


Start your Django development server:
python manage.py runserver


Test Twitter API:

Hit the endpoint /api/twitter-oauth/generate-url/ to get the authorization URL.
Redirect the user to the returned authorization_url.
Once authenticated, Twitter will redirect to /api/twitter-oauth/callback/, which will fetch the user's info.


Test LinkedIn API:

Hit the endpoint /api/linkedin-oauth/generate-url/ to get the authorization URL.
Redirect the user to the returned authorization_url.
Once authenticated, LinkedIn will redirect to /api/linkedin-oauth/callback/, which will fetch the user's info.


Test Reddit API:

Hit the endpoint /api/reddit-oauth/generate-url/ to get the authorization URL.
Redirect the user to the returned authorization_url.
Once authenticated, Reddit will redirect to /api/reddit-oauth/callback/, which will fetch the user's info.