from xml.etree import ElementTree as ET

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

# Example usage
input_ui_file = "/path/to/your/input.ui"  # Replace with the path to your .ui file
output_ui_file = "/path/to/your/output.ui"  # Replace with the path to your desired output file

# Call the function with the file paths
strip_stylesheet_properties("ui/main_ui_o.ui", "ui/new_ui.ui")