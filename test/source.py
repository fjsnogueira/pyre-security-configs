def os_system(command):
    import os
    os.system(command)

def pickle_loads(command):
    import pickle
    pickle.loads(command)

def marshal_loads(command):
    import marshal
    marshal.loads(command)

def _eval(command):
    eval(command)

def subprocess_run(command):
    import subprocess
    subprocess.run(command)

def popen(command):
    import subprocess
    subprocess.Popen(command)

def convert():
    source = input("user input")
    os_system(source)
    pickle_loads(source)
    marshal_loads(source)
    _eval(source)
    subprocess_run(source)

