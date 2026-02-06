*NO LONGER FUNCTIONAL* 

 
I’ve refined the technical terms to ensure it sounds like a professional tool for the English-speaking modding community.

Nexus Mods restricts automatic collection downloads to Premium users only. For Free users, Vortex (Mod Manager) requires a manual click on a "Download Manually" button for every single mod in a collection. This opens a browser tab where you must click "Slow Download" again. For collections with hundreds of mods, this process is tedious and inefficient.

🛠 The Solution
This repository provides a hybrid automation solution designed to bypass this repetitive workflow, optimized for high-resolution displays (tested on 5120x1440 Ultrawide):

Python Script (Desktop): Uses PyAutoGUI with image recognition focused on a Region of Interest (ROI). It detects and clicks the button inside the Vortex modal while ignoring background elements.

Tampermonkey Script (Web): A JavaScript snippet that monitors tabs opened by Vortex, automates the "Slow Download" click once the DOM is ready, and closes the tab after the nxm:// protocol triggers.

🧰 Tech Stack
Python 3.12 (Stable environment for UI automation)

PyAutoGUI & OpenCV (Image processing and click precision)

Tampermonkey (Web-side script injection)

Winsound (Hardware-based audio feedback)

📋 Prerequisites
Python 3.12 installed.

Required libraries:

Bash
pip install pyautogui opencv-python Pillow
Tampermonkey extension installed in your browser.

⚙️ How to Use
Clone the repository.

Capture a screenshot of just the word manually from the Vortex button and save it as target_manually.png in the project root.

Add the nexus_auto_click.user.js script to your Tampermonkey dashboard.

Run the bot:

Bash
python downloadManuallyVortexModManager.py
Start your collection download in Vortex and let the automation handle the rest. 🍦
