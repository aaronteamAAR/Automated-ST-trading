from tda import auth, client
import json



token_path = '/path/to/token.json'
api_key = 'PJNXBXPGWJM9RV4JCQVHLKZBKZO0FBWV@AMER.OAUTHAP'
redirect_uri = 'https://127.0.0.1:8080'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)
