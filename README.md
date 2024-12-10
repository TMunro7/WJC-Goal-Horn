# Goal Horn Program

This program monitors your screen for a specific image (representing a "goal") and, when detected, triggers a connected LIFX smart bulb to change color and play a goal horn sound.

## What the Code Does

1. **LIFX Integration:**  
   The code uses the [lifxlan](https://github.com/mclarkk/lifxlan) library to communicate with a LIFX smart bulb. It discovers the bulb (based on MAC address and IP), turns it on, and changes its color.

2. **Screen Detection:**  
   Using `pyautogui`, the script continuously scans a specific region of the screen for a reference image (`goal.jpg`). When it detects the goal image, it proceeds to the "goal event" sequence.

3. **Goal Event Sequence:**
   - **Light Color Change:** The bulb’s color changes to red (or another specified color).
   - **Play Horn Sound:** With `pygame`, it plays an MP3 horn sound (`dontStopTheParty.mp3`).
   - **Revert Color:** After a 20-second delay, the bulb’s color reverts to its original state.

---

## Requirements

- **Python 3.7+** (Recommended)
- **Virtual Environment (Optional)** to isolate dependencies.

### Installing Dependencies

A `requirements.txt` file is included. It lists all the required Python packages:

- `lifxlan`
- `python-dotenv`
- `pyautogui`
- `pygame`

---

### Steps to Set Up:

1. **Check Python and pip:**
   ```bash
   python --version
   pip --version

2. **Create and Activate a Virtual Environment (Recommended):**

    ```bash
    `python -m venv venv`
    # On Linux/MacOS
    `source venv/bin/activate`
    # On Windows
    `venv\Scripts\activate`

3. **Install all required packages:**
    `pip install -r requirements.txt`

### Setting Up Environment Variables

The code uses environment variables for the LIFX bulb’s MAC address and IP. The .env file should parameters shown in the .env.example file
- Create a .env file in the project root if it doesn’t exist.
- Copy the contents of the .env.example file and replace the required values.

### What Happens:

    1. The script attempts to connect to the LIFX bulb and turn it on.
    2. It starts scanning the specified region of the screen for `goal.jpg`.
    3. When the goal image is detected:
    - It prints "Goal found!"
    - Changes the light color to red
    - Plays the horn sound
    - Waits 20 seconds
    - Reverts the light to its original color
