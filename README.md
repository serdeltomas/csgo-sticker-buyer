csgo-sticker-buyer
## Automation for buying CS:GO Major stickers

This script aims to automate repetitive buying of csgo sticker capsules from current major (RIO 2022). For now it is dumb script clicking on a hard coded sets of coordinates in order to speed up the process, as the used library is slow at finding exact images on the screen, it is only used for the authorize button in overlay, because that item's position may vary.

GUI example:

![image](https://user-images.githubusercontent.com/73882365/209368198-6c7766aa-3d01-4e84-8710-a2f0618c8e78.png)


***BEWARE of the number of items you input (sum of capsules you want to buy) because your inventory may overflow and this app will stop. Also if you have no sufficent balance/funds in your steam wallet this app will stop. Don't move your mouse while the app is running.***

Prerequisites:
- python 3.11.1 
  - pillow library https://pillow.readthedocs.io/en/stable/ or https://pypi.org/project/Pillow/
  - pyautogui library https://pyautogui.readthedocs.io/en/latest/
  - tkinter library https://docs.python.org/3/library/tkinter.html
- *csgo installed and running in 1920x1080 resolution, before starting the script sticker menu should be open, like this:*

![Screenshot_20221215_103157](https://user-images.githubusercontent.com/73882365/207824089-2090760e-94a3-4c9f-9ecc-89ffba6291ac.png)

***IF YOU DON'T KNOW WHAT YOU ARE DOING HERE, DON'T RUN THIS CODE***

