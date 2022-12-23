csgo-sticker-buyer
## Automation for buying CS:GO Major stickers

This script aims to automate repetitive buying of csgo sticker capsules from current major (RIO 2022). For now it is dumb script clicking on a hard coded sets of coordinates in order to speed up the process, as the used library is slow at finding exact images on the screen, it is only used for the authorize button in overlay, because that item's position may vary.

GUI examples:

![Screenshot_20221223_173050](https://user-images.githubusercontent.com/73882365/209372299-118efaa1-6094-4d98-aaac-ae1f6d99cc29.png)
![Screenshot_20221223_174456](https://user-images.githubusercontent.com/73882365/209372348-49291a33-75e6-4c08-a272-50b98bb834c9.png)

Prerequisites:
- python 3.11.1 
  - pillow library https://pillow.readthedocs.io/en/stable/ or https://pypi.org/project/Pillow/
  - pyautogui library https://pyautogui.readthedocs.io/en/latest/
  - tkinter library https://docs.python.org/3/library/tkinter.html
- *csgo installed and running in 1920x1080 resolution, before starting the script sticker menu should be open, like this:*

![Screenshot_20221215_103157](https://user-images.githubusercontent.com/73882365/207824089-2090760e-94a3-4c9f-9ecc-89ffba6291ac.png)

***BEWARE of the number of items you input (sum of capsules you want to buy) because your inventory may overflow and this app will stop. Also if you have no sufficent balance/funds in your steam wallet this app will stop. Don't move your mouse while the app is running.***

GUI error examples:

![image](https://user-images.githubusercontent.com/73882365/209372493-cbf8d4ec-39c3-490e-8886-2813ed0c600e.png)
![Screenshot_20221223_173422](https://user-images.githubusercontent.com/73882365/209372334-fe61a28e-a74d-41d8-a05b-4036e57f148d.png)

Link to YouTube video of the app running:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/w9QcKshCkaQ/0.jpg)](https://youtu.be/w9QcKshCkaQ)


***IF YOU DON'T KNOW WHAT YOU ARE DOING HERE, DON'T RUN THIS CODE***

