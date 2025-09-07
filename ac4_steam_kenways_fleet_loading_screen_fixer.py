# -*- coding: utf-8 -*-
"""AC4 Steam Fixer

Simply run the script, and it will step you through what to do.
Only works on STEAM version of AC4.
"""

import os
import shutil
import urllib.request

def find_game_path():
    """
    Attempts to find the game's installation path on a standard Steam installation.
    This function assumes a default Steam installation location.
    """
    steam_path = os.getenv('PROGRAMFILES(X86)') or os.getenv('PROGRAMFILES')
    if steam_path:
        path = os.path.join(steam_path, 'Steam', 'steamapps', 'common', "Assassin's Creed IV Black Flag")
        if os.path.isdir(path):
            return path
    return None

def apply_fix():
    """
    Automates the process of backing up the original AC4BFSP.exe and
    replacing it with the community-made fix.
    """
    print("--- Assassin's Creed IV: Black Flag Kenway's Fleet Fix ---")

    game_path = find_game_path()
    if not game_path:
        print("Error: Could not find the game's installation folder.")
        print("Please ensure Assassin's Creed IV: Black Flag is installed via Steam.")
        return

    print(f"Game folder found at: {game_path}")

    # Define file paths
    original_exe = os.path.join(game_path, 'AC4BFSP.exe')
    backup_exe = os.path.join(game_path, 'AC4BFSP_original_backup.exe')

    # Path to the old executable downloaded from Steam Depot
    steam_content_path = os.path.join(os.path.dirname(os.path.dirname(game_path)), 'content', 'app_242050', 'depot_242051')
    temp_fix_file = os.path.join(steam_content_path, 'AC4BFSP.exe')

    if not os.path.exists(original_exe):
        print(f"Error: The file '{original_exe}' was not found.")
        return

    # 1. Create a backup of the original file
    if os.path.exists(backup_exe):
        print("A backup file already exists. Skipping backup.")
    else:
        print("Creating a backup of the original AC4BFSP.exe...")
        try:
            shutil.copyfile(original_exe, backup_exe)
            print("Backup created successfully.")
        except Exception as e:
            print(f"Error creating backup: {e}")
            return

    # 2. Instruct the user to download the depot using the Steam console
    print("\nIMPORTANT: This script requires a manual step.")
    print("Opening Steam console automatically...")
    os.system("start steam://open/console")

    print("\n1. A Steam console window has just opened. Go to that window.")
    print("2. Copy the following command and paste it into the console:")
    print("   download_Depot 242050 242051 7598860626606919774")
    print("3. Press Enter to start the download.")
    print(f"\nThe depot will download to: {steam_content_path}")
    input("\nPress Enter to continue once the download is complete.")

    if not os.path.exists(temp_fix_file):
        print(f"Error: The downloaded fix file '{temp_fix_file}' was not found.")
        print("Please ensure you have performed the Steam console steps correctly.")
        return

    # 3. Replace the original file with the new one
    print("\nReplacing the original AC4BFSP.exe with the new fix...")
    try:
        shutil.copyfile(temp_fix_file, original_exe)
        print("File replaced successfully. The fix has been applied.")
    except Exception as e:
        print(f"Error replacing file: {e}")
        return

    print("\nFix applied. You can now launch Assassin's Creed IV: Black Flag from Steam.")
    print("A backup of the original executable is located at:")
    print(backup_exe)

if __name__ == '__main__':
    apply_fix()
