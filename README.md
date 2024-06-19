# Django Social OUATH Integration Backend

### Setup

- set up a virtual environment
    ```
    python3 -m virtualenv .venv
    ```
- Install requirements files
    ```
    pip install -r requirements.txt
    ```


### Oauth setup

- Head over to api/api/settings.py
- In the settings.py file locate the ```SOCIAL_AUTH_GOOGLE_OAUTH2_KEY``` and ```SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET``` variables
- Head over to [https://console.cloud.google.com](Google API) to get your secret keys
- Replace your keys with that in the variables