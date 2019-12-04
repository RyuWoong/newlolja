import os

def GET_KEY(name):
    path = os.path.dirname( os.path.abspath( __file__ ) )+"/"+name
    file = open(path,"r",encoding="utf-8")
    key = file.read().split()
    return key

