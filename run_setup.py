# run_setup.py - Run this ONCE before main file
import os
os.makedirs('data', exist_ok=True)
os.makedirs('outputs', exist_ok=True)
print("Folders created! Now put creditcard.csv inside the 'data/' folder")
