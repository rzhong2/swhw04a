# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 13:44:00 2016
Updated Feb 19, 2018

The primary goal of this file is to demonstrate a simple python program to check python API

@author: rzhong2
"""
import requests
import json
def get_repos(username):
    repos_url = 'https://api.github.com/user/repos'
    # from https://github.com/user/settings/tokens
    token = '1a6d4c036977502c121237ae729ae8a1aeb7ad25'
    # create a re-usable session object with the user creds in-built
    gh_session = requests.Session()
    gh_session.auth = (username, token)

    # get the list of repos belonging to me
    repos = json.loads(gh_session.get(repos_url).text)

    # print the repo names
    for repo in repos:
        number_url = 'https://api.github.com/repos/%s/%s/commits' % (username, repo['name'])
        # create a re-usable session object with the user creds in-built
        nb_session = requests.Session()
        nb_session.auth = (username, token)

        # get the list of repos belonging to me
        number_repos = json.loads(nb_session.get(number_url).text)
        # print the repo names
        for number_repo in number_repos:
            number = number_repo['commit']['comment_count']
        repo_name = repo['name']
        return('Repo: '+repo_name+' Number of commits: '+str(number)+'\n')
