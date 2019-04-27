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


def subprocess_call(command):
    import subprocess
    subprocess.call(command)


def subprocess_check_call(command):
    import subprocess
    subprocess.check_call(command)


def subprocess_check_output(command):
    import subprocess
    subprocess.check_output(command)


def subprocess_getstatusoutput(command):
    import subprocess
    subprocess.getstatusoutput(command)


def subprocess_getoutput(command):
    import subprocess
    subprocess.getoutput(command)


def os_popen(command):
    import os
    os.popen(command)


def os_execl(command):
    import os
    os.execl(command, "arg", "arg")


def os_execlp(command):
    import os
    os.execlp(command, "arg", "arg")


def os_execle(command):
    import os
    os.execle(command, "arg", "arg")


def os_execlpe(command):
    import os
    os.execlpe(command, "arg", "arg")


def os_execv(command):
    import os
    os.execv(command, "args")


def os_execve(command):
    import os
    os.execve(command, "args", "env")


def os_execvp(command):
    import os
    os.execvp(command, "args")


def os_execvpe(command):
    import os
    os.execvpe(command, "args", "env")


def os_spawnl(command):
    import os
    os.spawnl("mode", command, "arg", "args")


def os_spawnle(command):
    import os
    os.spawnle("mode", command, "arg", "args")


def os_spawnv(command):
    import os
    os.spawnv("mode", command, "args")


def os_spawnve(command):
    import os
    os.spawnve("mode", command, "args", "env")


def os_spawnlp(command):
    import os
    os.spawnlp("mode", command, "args", "env")


def os_spawnlpe(command):
    import os
    os.spawnlpe("mode", command, "arg", "env")


def os_spawnvp(command):
    import os
    os.spawnvp("mode", command, "args")


def os_spawnvpe(command):
    import os
    os.spawnvpe("mode", command, "args", "env")


def convert():
    source = input("user input")
    subprocess_popen(source)
    os_popen(source)
    os_system(source)
    pickle_loads(source)
    marshal_loads(source)
    _eval(source)

    subprocess_run(source)
    subprocess_call(source)
    subprocess_check_call(source)
    subprocess_check_output(source)
    subprocess_getstatusoutput(source)
    subprocess_getoutput(source)

    os_execl(source)
    os_execlp(source)
    os_execle(source)
    os_execlpe(source)
    os_execv(source)
    os_execve(source)
    os_execvp(source)
    os_execvpe(source)
    os_spawnl(source)
    os_spawnle(source)
    os_spawnv(source)
    os_spawnve(source)
    os_spawnlp(source)
    os_spawnlpe(source)
    os_spawnvp(source)
    os_spawnvpe(source)
