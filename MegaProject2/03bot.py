import pyautogui
import time
import subprocess
from openai import OpenAI
import pyperclip
client = OpenAI(
    api_key="OPENAI_API_KEY",)
def is_last_message_from_sender(chat_log, sender_name="Mummy Ji"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
# Give some time to switch to the correct window
time.sleep(3)

# Click on the icon at (901, 804)
pyautogui.click(125, 795)
time.sleep(1)  # Wait for UI response
while True:
    # Drag from (484, 98) to (1036, 654)
    pyautogui.moveTo(600, 170)
    pyautogui.dragTo(1229, 700, duration=2, button='left')
    time.sleep(1)

    # Copy the selected text using Command + C (for macOS)
    pyautogui.hotkey('command', 'c')
    time.sleep(1)
    pyautogui.click(595,170)
    # Retrieve copied text using macOS pbpaste
    chat_history = subprocess.run("pbpaste", capture_output=True, text=True).stdout.strip()

    # Print or use the copied text
    print("Copied Text:", chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Rishu Rajput who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only) please don't give output woth date and name"},
                    {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Mummy Ji: "},
                    {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content

        pyautogui.click(765, 740)
        time.sleep(1)
        pyperclip.copy(response)
        pyautogui.hotkey('command', 'v')
        time.sleep(1)
        pyautogui.press('enter')
    