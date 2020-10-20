"""
Some Python wrapping of the frioul_batch command available on the head of the INT HPC Cluster
in order to facilitate passive/ parallel computation
"""

import subprocess

def launch_cmd(cmd, core, exec_dir, stdout_file, stderr_file, cmd_file):
    """
    Basic Python wrapping of the frioul_batch command of frioul
    :param cmd: the whole command to be executed on the cluster
    :param core: the number of CPU core to use: between 1 to 16
    :param exec_dir: the directory where to launch the command
    :param stdout_file: the  asbolute path of the standart output file of the process
    :param stderr_file: the  asbolute path of the standart error file of the process
    :param cmd_file: the command passed to frioul_batch (should be cmd)
    :return: None
    """
    subprocess.run(
        ["frioul_batch", "-d", exec_dir, "-E", stderr_file, '-O', stdout_file,  '-C', cmd_file, '-c',  str(core), '"' + cmd + '"']
    )
    pass


def launch_bvproc(path_bvproc, brainvisa_python, core, exec_dir, stdout_file, stderr_file, cmd_file):
    """
    Execute brainvisa process stored into a bvproc file in a passive way on frioul
    :param path_bvproc: path of the bvproc to be executed on frioul in a passiv way
    :param brainvisa_python: instance of python belonging to brainvisa
    :param core: number of core required (1 to 16)
    :param exec_dir: directory where to launch the computation
    :param stdout_file: standart output file path
    :param stderr_file: standart error file path
    :param cmd_file: cmf file path
    :return: None
    """

    cmd = brainvisa_python + " -m   brainvisa.axon.runprocess  --enabledb " + path_bvproc
    launch_cmd(cmd, core, exec_dir, stdout_file, stderr_file, cmd_file)
    pass

