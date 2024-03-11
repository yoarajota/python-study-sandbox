from datasets import load_dataset
import pandas as pd
import numpy as np 
import pyautogui
import time

dataset = load_dataset("Abirate/english_quotes")

# Create datframe

df = pd.DataFrame(dataset["train"])

# If has tag love
luv = df[df['tags'].apply(lambda x: 'love' in x)]

# Shuffle dataframe
luv = luv.sample(frac=1).reset_index(drop=True)

# Implement an `abort` button that will stop this script from running.

pyautogui.moveTo(700, 955)

# Loop quotes
for i in luv['quote']:
    pyautogui.moveTo(700, 955)
    pyautogui.click()
    pyautogui.write(i)
    pyautogui.press("enter")
    time.sleep(2)