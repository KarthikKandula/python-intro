# Imports
import subprocess

def runAddScript():
    script_path = './add.sh'

    output = runShellScript(script_path,'0','7')

    print(f"Output from ADD script \n\n{output}")

def runGitScript():
    script_path = './git.sh'

    output = runShellScript(script_path,'notes','main')

    print(f"Output from GIT script \n\n{output}")

def runShellScript(script_path,arg1,arg2):
    print("Running shell script...")

    process = subprocess.Popen([script_path, arg1, arg2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = process.communicate()

    if process.returncode == 0:
        print("Shell script executed successfully")
        # print(f"Output from shell script \n{error.decode() + output.decode()}")
    else:
        print("Shell script failed with error code", process.returncode)

    return error.decode() + output.decode()

# Main - all program execution starts from here
def main():
    print("main")
    
    runAddScript()
    runGitScript()

if __name__ == '__main__':
    main()
