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


def subprocess_popen(command):
    import subprocess
    subprocess.Popen(command)


def os_popen(command):
    import os
    os.popen(command)


def convert():
    source = input("user input")
    subprocess_popen(source)
    os_popen(source)
    os_system(source)
    pickle_loads(source)
    marshal_loads(source)
    _eval(source)
    subprocess_run(source)
