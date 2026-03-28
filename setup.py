#!/usr/bin/env python3
"""
Ram Sir Platform - Quick Setup Script
Run: python setup.py
"""
import os
import sys
import subprocess

def run(cmd, check=True):
    print(f"  ▶ {cmd}")
    result = subprocess.run(cmd, shell=True, check=check)
    return result.returncode == 0

def main():
    print("=" * 60)
    print("  🎓 Ram Sir Course Platform - Auto Setup")
    print("  By Ramgopal Prajapati | Indore, M.P.")
    print("=" * 60)

    print("\n[1/5] Creating virtual environment...")
    run("python -m venv venv", check=False)

    # Detect activate script
    if os.name == 'nt':
        pip = "venv\\Scripts\\pip"
        python = "venv\\Scripts\\python"
    else:
        pip = "venv/bin/pip"
        python = "venv/bin/python"

    print("\n[2/5] Installing requirements...")
    run(f"{pip} install django pillow")

    print("\n[3/5] Running migrations...")
    run(f"{python} manage.py makemigrations courses")
    run(f"{python} manage.py migrate")

    print("\n[4/5] Populating initial courses (15+ courses)...")
    run(f"{python} manage.py populate_courses")

    print("\n[5/5] Creating superuser...")
    print("\n  👉 Please create your admin account:")
    os.system(f"{python} manage.py createsuperuser")

    print("\n" + "=" * 60)
    print("  ✅ Setup Complete!")
    print("\n  🚀 Start the server:")
    print("     python manage.py runserver")
    print("\n  🌐 Open browser:")
    print("     Main site: http://127.0.0.1:8000/")
    print("     Admin:     http://127.0.0.1:8000/admin/")
    print("=" * 60)

if __name__ == "__main__":
    main()
