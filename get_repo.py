# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:44:00 2016
Updated Feb 26, 2018

The primary goal of this file is to demonstrate a simple python program to check python API

@author: rzhong2
"""
import requests
import json
def get_repos(username):
    repos_url = 'https://api.github.com/user/repos'
    # from https://github.com/user/settings/tokens
    # create a re-usable session object with the user creds in-built
    gh_session = requests.Session()
    gh_session.auth = (username, token)

    # get the list of repos belonging to me
    repos = json.loads(gh_session.get(repos_url).text)
    return('TRUE')
