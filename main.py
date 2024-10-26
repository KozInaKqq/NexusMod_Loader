def InitModsList():
    mod_list=[]
    return mod_list

def GetRequirement(mod_name):
    req_mod_list = []
    return req_mod_list

def Download():
    pass

if __name__== "__main__":
    mod_list = InitModsList()
    for mod in mod_list:
        for req in GetRequirement(mod):
            if req not in mod_list:
                mod_list+=req
    for i in mod_list:
        Download(i)
    print("Hello")


