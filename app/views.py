from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
import urllib.parse
import requests
from requests_oauthlib import OAuth1Session


class LinkedInAuthViewSet(ViewSet):

    @action(detail=False, methods=['get'], url_path='generate-url')
    def generate_linkedin_url(self, request):
        params = {
            'response_type': 'code',
            'client_id': settings.LINKEDIN_CLIENT_ID,
            'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
            'scope': 'openid profile email',
        }
        url = f"{settings.LINKEDIN_AUTH_URL}?{urllib.parse.urlencode(params)}"
        return Response({'url': url})

    @action(detail=False, methods=['get'], url_path='callback')
    def linkedin_callback(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'Missing authorization code'}, status=400)
        token_data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
            'client_id': settings.LINKEDIN_CLIENT_ID,
            'client_secret': settings.LINKEDIN_CLIENT_SECRET,
        }
        token_response = requests.post(settings.LINKEDIN_TOKEN_URL, data=token_data)

        if token_response.status_code != 200:
            return Response({'error': 'Failed to fetch access token'}, status=400)

        access_token = token_response.json().get('access_token')
        if not access_token:
            return Response({'error': 'No access token received'}, status=400)
        userinfo_headers = {'Authorization': f'Bearer {access_token}'}
        userinfo_response = requests.get(settings.LINKEDIN_USERINFO_URL, headers=userinfo_headers)

        if userinfo_response.status_code != 200:
            return Response({'error': 'Failed to fetch user info'}, status=400)
        return Response(userinfo_response.json())


class TwitterAuthViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path='generate-url')
    def generate_url(self, request, *args, **kwargs):
        try:
            oauth = OAuth1Session(
                client_key=settings.TWITTER_API_KEY,
                client_secret=settings.TWITTER_API_SECRET_KEY,
                callback_uri=settings.TWITTER_REDIRECT_URI
            )

            request_token_url = settings.TWITTER_REQUEST_TOKEN_URL
            response = oauth.fetch_request_token(request_token_url)

            oauth_token = response.get('oauth_token')
            oauth_token_secret = response.get('oauth_token_secret')
            authorize_url = f'https://api.twitter.com/oauth/authorize?oauth_token={oauth_token}'

            return Response(
                {
                    'authorization_url': authorize_url,
                    'oauth_token': oauth_token,
                    'oauth_token_secret': oauth_token_secret
                }
            )

        except Exception as e:
            return Response({'error': 'An error occurred', 'details': str(e)}, status=500)

    @action(detail=False, methods=['get'], url_path='callback')
    def twitter_callback(self, request, *args, **kwargs):
        try:
            oauth_token = request.GET.get('oauth_token')
            oauth_verifier = request.GET.get('oauth_verifier')

            if not oauth_token or not oauth_verifier:
                return Response({'error': 'Missing required parameters'}, status=400)

            oauth = OAuth1Session(
                client_key=settings.TWITTER_API_KEY,
                client_secret=settings.TWITTER_API_SECRET_KEY,
                resource_owner_key=oauth_token,
                resource_owner_secret=request.GET.get('oauth_token_secret')
            )

            access_token_url = settings.TWITTER_ACCESS_TOKEN_URL
            response = oauth.fetch_access_token(access_token_url, verifier=oauth_verifier)

            access_token = response.get('oauth_token')
            access_token_secret = response.get('oauth_token_secret')
            if not access_token or not access_token_secret:
                return Response({'error': 'Failed to retrieve access token'}, status=400)
            oauth = OAuth1Session(
                client_key=settings.TWITTER_API_KEY,
                client_secret=settings.TWITTER_API_SECRET_KEY,
                resource_owner_key=access_token,
                resource_owner_secret=access_token_secret
            )
            user_info_url = settings.TWITTER_USERINFO_URL
            user_info_response = oauth.get(user_info_url)
            if user_info_response.status_code != 200:
                return Response({'error': 'Failed to fetch user info'}, status=400)
            user_info = user_info_response.json()
            return Response(user_info)
        except Exception as e:
            return Response({'error': 'An error occurred', 'details': str(e)}, status=500)