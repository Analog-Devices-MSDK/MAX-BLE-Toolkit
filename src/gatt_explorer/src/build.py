import os
import shutil
import subprocess
from xml.etree import ElementTree as ET

''''
When making ui changes in QT designer load the main_ui.ui file and save it.
Then run this script. This script will strip the stylesheet properties from the main_ui.ui file
and make a  new ui file called main_ui_stripped.ui then it will generate the main_ui.py file it.
The reason for this is because any stylesheets set in QT designer will override the stylesheets
in the QSS themefiles.

'''

def strip_stylesheet_properties(ui_file_path, output_file_path):
    # Parse the XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

    # Recursively remove 'styleSheet' properties
    def remove_style_sheets(element):
        # List for storing child elements to be removed
        to_remove = []
        
        for child in element:
            if child.tag == 'property' and child.get('name') == 'styleSheet':
                to_remove.append(child)
            else:
                remove_style_sheets(child)
        
        # Removing the identified child elements
        for child in to_remove:
            element.remove(child)

    remove_style_sheets(root)

    # Write the modified XML back to a new file
    tree.write(output_file_path, encoding="utf-8", xml_declaration=True)


# Call the function with the file paths
strip_stylesheet_properties("../ui/main_ui.ui", "../ui/main_ui_stripped.ui")   
# Command to generate main_ui.py from main_ui.ui
subprocess.run(["pyside6-uic", "../ui/main_ui_stripped.ui", "-o", "modules/main_ui.py"])
#subprocess.run(["pyside6-uic", "char.ui", "-o", "char.py"])

# fix import issues
''' NOTE TO SELF : fixed this with the line below in main_app.py
sys.path.append(str(Path(__file__).resolve().parent / "src"))
Also note that in qt designer the check box is promoted to 
custom_widgets.toggle.h as the header and AnimatedToggle as the promoted  class name
'''
string1 = "from toggle import AnimatedToggle"
string2 = "from custom_widgets.toggle import AnimatedToggle"
file_path = "modules/main_ui.py"

# # Perform the replacement
with open(file_path, "r") as file:
    content = file.read()
    updated_content = content.replace(string1, string2)

with open(file_path, "w") as file:
    file.write(updated_content)

print("Done generating main_ui.py")