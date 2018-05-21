import subprocess


output = subprocess.check_output(['tail', '-n 5', 'test2.log'], universal_newlines=True)
