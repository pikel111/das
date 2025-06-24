import subprocess
import sys
import colorama
from colorama import Fore, Style
import os

def instalar_dependencias():
    # Detecta el gestor de paquetes adecuado
    if os.path.exists('/usr/bin/apt-get'):
        package_manager = 'apt-get'
    elif os.path.exists('/usr/bin/yum'):
        package_manager = 'yum'
    elif os.path.exists('/usr/bin/dnf'):
        package_manager = 'dnf'
    else:
        raise EnvironmentError("No se encontró un gestor de paquetes compatible.")

    try:
        if package_manager == 'apt-get':
            # Comandos para distribuciones basadas en Debian/Ubuntu
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'unrar'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'tmux'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'rar'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'syncthing'], check=True)

                 

        elif package_manager in ['yum', 'dnf']:
            # Comandos para distribuciones basadas en Red Hat (CentOS, RHEL, Rocky)
            subprocess.run(['sudo', package_manager, 'update', '-y'], check=True)
            subprocess.run(['sudo', package_manager, 'install', '-y', 'unrar'], check=True)
            subprocess.run(['sudo', package_manager, 'install', '-y', 'tmux'], check=True)
            subprocess.run(['sudo', package_manager, 'install', '-y', 'rar'], check=True)

        # Comandos comunes (independientes del gestor de paquetes)
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'rarfile'], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'rarfile'], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'rich'], check=True)


        # Imprimir mensaje en color rojo
        print(Fore.RED + "\nDependencias instaladas, ya puedes ejecutar el server.py")
        print(Style.RESET_ALL)

    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al ejecutar el comando: {e.cmd}")
        print(f"Código de salida: {e.returncode}")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init(autoreset=True)  # Inicializa colorama
    instalar_dependencias()  # Llama a la función para instalar dependencias
