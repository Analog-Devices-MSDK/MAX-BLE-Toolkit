import os
import shutil
import subprocess

# Command to generate main_ui.py from main_ui.ui
subprocess.run(["pyside6-uic", "../ui_designer/main_ui.ui", "-o", "modules/main_ui.py"])
#subprocess.run(["pyside6-uic", "char.ui", "-o", "char.py"])

# fix import issues
''' NOTE TO SELF : fixed this with the line below in main_app.py
sys.path.append(str(Path(__file__).resolve().parent / "src"))
Also note that in qt designer the check box is promoted to 
custom_widgets.toggle.h as the header and AnimatedToggle as the promoted  class name
'''
# string1 = "from toggle import AnimatedToggle"
# string2 = "from custom_widgets.toggle import AnimatedToggle"
# file_path = "modules/main_ui.py"

# # # Perform the replacement
# with open(file_path, "r") as file:
#     content = file.read()
#     updated_content = content.replace(string1, string2)

# with open(file_path, "w") as file:
#     file.write(updated_content)

print("Done generating main_ui.py")