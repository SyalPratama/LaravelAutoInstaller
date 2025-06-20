import os
import sys
import subprocess
import shutil  

def run_command(command):
    print(f"\nMenjalankan: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print("Gagal menjalankan perintah.")
        sys.exit(1)

def install_laravel(project_name, version):
    command = f"composer create-project laravel/laravel {project_name} \"{version}\""
    run_command(command)

def install_package(project_dir, package):
    os.chdir(project_dir)
    if package == "breeze":
        run_command("composer require laravel/breeze --dev")
        run_command("php artisan breeze:install")
    elif package == "jetstream":
        run_command("composer require laravel/jetstream")
        run_command("php artisan jetstream:install livewire")
    elif package == "sanctum":
        run_command("composer require laravel/sanctum")
        run_command("php artisan vendor:publish --provider=\"Laravel\\Sanctum\\SanctumServiceProvider\"")
    elif package == "livewire":
        run_command("composer require livewire/livewire")
    elif package == "inertia":
        run_command("composer require inertiajs/inertia-laravel")
    else:
        print(f"Package {package} tidak dikenal.")

def update_env_database(project_dir, db_driver):
    env_path = os.path.join(project_dir, '.env')
    env_example_path = os.path.join(project_dir, '.env.example')

    # Jika .env tidak ada, salin dari .env.example
    if not os.path.exists(env_path):
        if os.path.exists(env_example_path):
            shutil.copy(env_example_path, env_path)
            print("File .env berhasil disalin dari .env.example")
        else:
            print("File .env dan .env.example tidak ditemukan.")
            return

    # Ubah DB_CONNECTION di .env
    with open(env_path, 'r') as file:
        lines = file.readlines()
    with open(env_path, 'w') as file:
        for line in lines:
            if line.startswith("DB_CONNECTION="):
                file.write(f"DB_CONNECTION={db_driver}\n")
            else:
                file.write(line)

def main():
    print("Laravel Installer Otomatis (Python CLI)\n")

    project_name = input("Nama proyek Laravel: ").strip()

    # Laravel Version Selection
    versions = [
        "11.9.0 (Latest - Jun 2025)",
        "^11.0 (LTS - 2024)",
        "^10.0 (LTS - 2023)",
        "^9.0  (LTS - 2022)",
        "^8.0  (2020)",
        "dev-master (latest dev version)"
    ]
    print("\nPilih versi Laravel:")
    for i, v in enumerate(versions, start=1):
        print(f"{i}. {v}")
    try:
        version_index = int(input("Pilih nomor versi [default 1]: ").strip() or "1") - 1
        version = versions[version_index].split()[0]
    except (ValueError, IndexError):
        print("Input tidak valid. Menggunakan default: 11.9.0")
        version = "11.9.0"

    # Package selection
    print("\nPilih package tambahan (pisahkan dengan koma, kosongkan jika tidak perlu):")
    print("   - breeze\n   - jetstream\n   - sanctum\n   - livewire\n   - inertia")
    packages_input = input("Masukkan nama package: ").strip()
    packages = [p.strip() for p in packages_input.split(",") if p.strip()]

    # DB Driver
    print("\nPilih database driver:")
    print("1. mysql\n2. pgsql")
    db_choice = input("Pilihan (1/2): ").strip()
    db_driver = "mysql" if db_choice == "1" else "pgsql"

    # Install Laravel
    install_laravel(project_name, version)

    # Install package tambahan
    for pkg in packages:
        install_package(project_name, pkg)

    # Update .env
    update_env_database(project_name, db_driver)

    print("\nInstalasi Laravel selesai!")
    print(f"Direktori: {project_name}")
    print("Jalankan perintah berikut untuk memulai:\n")
    print(f"cd {project_name}")
    print("php artisan serve")

if __name__ == "__main__":
    main()
