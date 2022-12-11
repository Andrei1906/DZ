# -*- coding: utf-8 -*-

import requests
import json
def get_github():
    repo = 'https://api.github.com/repos/Microsoft/vscode'
    repo = requests.get(repo).json()
    new_repo = {}
    for k in ['company', 'created_at', 'email', 'id', 'name', 'url']:
        if repo.get(k) is not None:
            new_repo[k] = repo.get(k)
    with open('repo.json', 'w') as file:
        json.dump(new_repo, file)

from tkinter import *
def tkinter():
    tk = Tk()
    Button(tk, text='Get github repo', command=get_github).pack()
    tk.mainloop()

tkinter()
