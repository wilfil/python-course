#!/usr/bin/env python3.9

from argparse import ArgumentParser
import shlex, subprocess
import os,sys

parser = ArgumentParser(description="Kills all the process on a certain port number")
parser.add_argument("port", type=int, help="port number in which the process are running")

args = parser.parse_args()

complete_command = f"lsof -n -i4TCP:{args.port} | grep -i listen"

command_line_1 = shlex.split(f"lsof -n -i4TCP:{args.port}")
command_line_2 = shlex.split("grep -i listen")

#args= shlex.split(command_line_1)
##print(args)

try:
    ps = subprocess.run(complete_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # ps2 = subprocess.run(["ls -latr"], shell=True, stdout=subprocess.PIPE)

#except subprocess.CalledProcessError as err:
except:
    print(f"No process running on port {args.port}")
    sys.exit(1)

else:
    lines = ps.stdout.splitlines()

    for line in lines:
        pid = int(line.split()[1])
        print("PID is %s" % pid)
        os.kill(pid, 9)


