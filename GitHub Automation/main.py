"""
Project: Simple Automation Script
File: main.py
Author: Carina Pilar
Date Created: 2025-01-16
Last Updated: 2025-01-16
Version: 1.0

Description:
This is a very simple script that automates the process of unsubscribing from GitHub issues on the page below:
https://github.com/notifications
It clicks on Select all, then on Unsubscribe.

Objectives:
- Simplify unsubscribing from GitHub issues by automating it.
- Saves time and improves efficiency - you can read a book while waiting.

Usage:
1. Open your browser, go to: https://github.com/notifications
2. Download the file main.py.
3. Run the script using the command:
   `python main.py`
4. Go back to Chrome and let the automation begin.

Contact:
Email address on my GitHub profile page.
"""

# Importing libraries
import pyautogui
import time

# Getting cursor position on the Select All checkbox - done just once
# time.sleep(5)
# print(pyautogui.position())

# Giving you time to open Chrome before automation starts
time.sleep(5)

# Checks the Select All option and hits the Unsubscribe button multiple times
# It's manually set to number of pages based on the number of subscriptions, it's how many times the automation needs to run
for x in range(0, 189):
    pyautogui.click(x=376, y=280) # Checks the Select All
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("space") # Clicks on Unsubscribe
    
    # Giving time for the list to refresh
    time.sleep(5)
