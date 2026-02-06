import pyautogui
import time
import winsound
import sys

# --- QA & STABILITY CONFIGURATIONS ---
# Failsafe: Drag the mouse to the upper-left corner of the screen to abort the script
pyautogui.FAILSAFE = True
# Default delay between PyAutoGUI commands to ensure UI stability
pyautogui.PAUSE = 0.5 

def get_search_region():
    """
    Defines a centralized Region of Interest (ROI) to avoid false positives 
    from background elements or sidebars.
    """
    width, height = pyautogui.size()
    # Focus on the center of the screen (40% width, 50% height) 
    # where Vortex modals typically appear.
    r_width = int(width * 0.4)
    r_height = int(height * 0.5)
    r_x = (width - r_width) // 2
    r_y = (height - r_height) // 2
    return (r_x, r_y, r_width, r_height)

def run_automation():
    # Use a small, specific image of the word 'manually' for better precision
    target_img = 'target_manually.png'
    search_area = get_search_region()
    
    print(f"--- Nexus Automation Started (Python 3.12) ---")
    print(f"Monitor: {pyautogui.size()} | ROI: {search_area}")
    print("Press Ctrl+C in terminal or move mouse to top-left corner to stop.")

    while True:
        try:
            # Grayscale=True and lowered confidence to handle 1440p Antialiasing
            button = pyautogui.locateOnScreen(
                target_img, 
                confidence=0.48, 
                grayscale=True, 
                region=search_area
            )

            if button:
                # Calculate center coordinates and perform the click
                center = pyautogui.center(button)
                pyautogui.click(center)
                
                # Immediate audio feedback via system beep
                winsound.Beep(1000, 250)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Successfully clicked 'manually' button.")
                
                # Generous sleep to allow Vortex to open the browser tab 
                # and prevent accidental double-clicks.
                time.sleep(10) 
            
        except pyautogui.ImageNotFoundException:
            # Silent loop while waiting for the modal to appear
            pass
        except KeyboardInterrupt:
            # Clean exit on manual stop
            print("\n--- Automation stopped by user ---")
            sys.exit()
        except Exception as e:
            # Error handling for unexpected UI or system issues
            print(f"⚠️ Unexpected error: {e}")
            time.sleep(5)

        # Scan interval to prevent high CPU usage
        time.sleep(1)

if __name__ == "__main__":
    run_automation()