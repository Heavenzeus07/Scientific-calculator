import subprocess

def install_requirements():
    # Replace 'requirements.txt' with the actual path to your requirements file
    subprocess.run(['pip', 'install','customtkinter'])

def run_login_script():
    # Replace 'LOGIN.py' with the name of your Python file
    subprocess.run(['python', 'sankha.py'])

if __name__ == "__main__":
    install_requirements()
    run_login_script()
