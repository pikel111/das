import os
import subprocess

# Obtener la ruta del script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Verificar si el script está en el directorio correcto
if not os.path.exists(os.path.join(script_dir, "iniciador.py")):
    print("❌ Tu programa no está actualizado.")
    exit(1)  # Salir con un código de error

os.chdir(script_dir)  # Cambia al directorio del script

def leer_version_tmodloader(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.startswith("tmodloaderversion:"):
                    return linea.split(":")[1].strip()
    except FileNotFoundError:
        print("❌ El archivo de configuración no se encontró.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
    return None

def ejecutar_script(version):
    # Ruta relativa de los scripts
    script_144 = os.path.join("server", "start-tModLoaderServer.sh")
    script_143 = os.path.join("1.4.3", "start-tModLoaderServer.sh")
    script_1353 = os.path.join("1.3.5.3", "tModLoaderServer")

    try:
        # Ejecutar tailscaled en segundo plano
        subprocess.Popen(["sudo", "tailscaled"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ tailscaled iniciado en segundo plano.")

        subprocess.Popen(["syncthing"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ syncthing iniciado en segundo plano.")

        if version == "1.4.4":
            subprocess.run(["bash", script_144, "-nosteam"], check=True)
            print("✅ Ejecutando start-tModLoaderServer.sh para la versión 1.4.4.")
        elif version == "1.4.3":
            subprocess.run(["bash", script_143], check=True)
            print("✅ Ejecutando start-tModLoaderServer.sh para la versión 1.4.3.")
        elif version == "1.3.5.3":
            subprocess.run([script_1353, "-config", "serverconfig.txt"], check=True)
            print("✅ Ejecutando tModLoaderServer para la versión 1.3.5.3.")
        else:
            print(f"⚠️ No hay un script definido para la versión {version}.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar el script para la versión {version}: {e}")

if __name__ == "__main__":
    archivo_config = "archivo.txt"  # Nombre del archivo de configuración
    version = leer_version_tmodloader(archivo_config)
    if version:
        ejecutar_script(version)
    else:
        print("⚠️ No se pudo determinar la versión de tModLoader.")
