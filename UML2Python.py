from graphviz import Digraph

class UMLGenerator:
    def __init__(self):
        # Initialize UMLGenerator with an empty dictionary for classes and a Digraph for UML diagrams
        self.classes = {}
        self.uml_diagram = Digraph('UMLDiagram', format='png')  # Format set to 'png' by default
        self.uml_diagram.attr(rankdir='LR')  # Set the rank direction to left-to-right

    def create_class(self, class_name):
        # Check if the class already exists
        if class_name in self.classes:
            print(f"Class '{class_name}' already exists. Please choose another name.")
        else:
            # Initialize class attributes and relationships
            self.classes[class_name] = {
                'attributes': [],
                'methods': [],
                'inheritance': None,
                'composition': [],
                'aggregation': []
            }
            # Add a node for the class in the UML diagram
            self.uml_diagram.node(class_name, shape='record', color='black', style='filled', fillcolor='lightgray')

    def add_attribute(self, class_name, attribute_name, attribute_type):
        # Add an attribute to the specified class
        if class_name in self.classes:
            self.classes[class_name]['attributes'].append((attribute_name, attribute_type))
            self.update_uml_diagram()

    def add_method(self, class_name, method_name, return_type):
        # Add a method to the specified class
        if class_name in self.classes:
            self.classes[class_name]['methods'].append((method_name, return_type))
            self.update_uml_diagram()

    def set_inheritance(self, class_name, parent_class):
        # Set inheritance relationship between the specified class and its parent class
        if class_name in self.classes:
            self.classes[class_name]['inheritance'] = parent_class
            self.update_uml_diagram()

    def add_composition(self, class_name, composed_class):
        # Add a composition relationship between the specified class and another class
        if class_name in self.classes:
            self.classes[class_name]['composition'].append(composed_class)
            self.update_uml_diagram()

    def add_aggregation(self, class_name, aggregated_class):
        # Add an aggregation relationship between the specified class and another class
        if class_name in self.classes:
            self.classes[class_name]['aggregation'].append(aggregated_class)
            self.update_uml_diagram()

    def update_uml_diagram(self):
        # Update the UML diagram based on the current class relationships and attributes
        self.uml_diagram.clear()
        self.uml_diagram.attr(rankdir='LR')

        for class_name, attributes in self.classes.items():
            # Build the label for the class node in the UML diagram
            label = f'{{ {class_name} |'
            label += ' | '.join([f'{name}: {type}' for name, type in attributes['attributes']])
            label += ' | ' + ' | '.join([f'{name}()' for name, _ in attributes['methods']])
            label += ' }}'

            # Add the class node with the constructed label
            self.uml_diagram.node(class_name, label=label, shape='record', color='black', style='filled',
                                  fillcolor='lightgray')

            # Add edges for inheritance, composition, and aggregation relationships
            if attributes['inheritance']:
                self.uml_diagram.edge(attributes['inheritance'], class_name, arrowhead='empty', dir='back')

            for composed_class in attributes['composition']:
                self.uml_diagram.edge(class_name, composed_class, label='', arrowhead='odot')

            for aggregated_class in attributes['aggregation']:
                self.uml_diagram.edge(class_name, aggregated_class, label='', arrowhead='diamond')

        # Render the UML diagram to a file named 'UMLDiagram.png'
        self.uml_diagram.render(filename='UMLDiagram', view=False, cleanup=True)

    def show_uml_diagram(self):
        # View the UML diagram using the default viewer
        self.uml_diagram.view(filename='UMLDiagram')

    def generate_python_code(self):
        # Generate Python code based on the defined classes, attributes, and relationships
        code = ''
        for class_name, attributes in self.classes.items():
            code += f'class {class_name}'

            if attributes['inheritance']:
                code += f'({attributes["inheritance"]})'

            code += ':\n'

            # Attributes
            for attr_name, attr_type in attributes['attributes']:
                code += f'    {attr_name}: {attr_type}\n'

            # Constructor
            code += f'    def __init__(self):  # Initialize attributes in the constructor\n'
            for attr_name, _ in attributes['attributes']:
                code += f'        self.{attr_name} = None\n'

            # Methods
            for method_name, return_type in attributes['methods']:
                code += f'    def {method_name}(self) -> {return_type}:\n'
                code += f'        # Add method implementation here\n'

            # Composition
            for composed_class in attributes['composition']:
                code += f'    {composed_class.lower()} = {composed_class}()\n'

            # Aggregation
            for aggregated_class in attributes['aggregation']:
                code += f'    {aggregated_class.lower()} = None  # Initialize in constructor\n'

            code += '\n'

        return code

    def save_to_file(self, filename):
        # Save the generated Python code to a file with the specified filename
        with open(filename, 'w') as file:
            file.write(self.generate_python_code())

def main():
    # Main function to interactively use the UMLGenerator
    uml_generator = UMLGenerator()

    while True:
        print("\nChoose an option:")
        print("1. Create class")
        print("2. Add attribute")
        print("3. Add method")
        print("4. Set inheritance")
        print("5. Add composition")
        print("6. Add aggregation")
        print("7. Show UML diagram")
        print("8. Finish and generate code")

        option = input("Enter option (1-8): ")

        if option == '1':
            class_name = input("Enter class name: ")
            uml_generator.create_class(class_name)
        elif option in ['2', '3', '4', '5', '6']:
            existing_classes = list(uml_generator.classes.keys())
            if not existing_classes:
                print("Error: No classes created. Please create a class first.")
                continue

            print("Existing classes:")
            for i, class_name in enumerate(existing_classes, start=1):
                print(f"{i}. {class_name}")

            class_index = input("Choose the class to modify (enter the number): ")

            try:
                class_index = int(class_index)
                if 1 <= class_index <= len(existing_classes):
                    class_name = existing_classes[class_index - 1]

                    if option == '2':
                        attr_name = input("Enter attribute name: ")
                        attr_type = input("Enter attribute type: ")
                        uml_generator.add_attribute(class_name, attr_name, attr_type)
                    elif option == '3':
                        method_name = input("Enter method name: ")
                        return_type = input("Enter return type: ")
                        uml_generator.add_method(class_name, method_name, return_type)
                    elif option == '4':
                        parent_class = input("Enter parent class name: ")
                        uml_generator.set_inheritance(class_name, parent_class)
                    elif option == '5':
                        composed_class = input("Enter composed class name: ")
                        uml_generator.add_composition(class_name, composed_class)
                    elif option == '6':
                        aggregated_class = input("Enter aggregated class name: ")
                        uml_generator.add_aggregation(class_name, aggregated_class)
                else:
                    print("Invalid class index. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == '7':
            uml_generator.show_uml_diagram()
        elif option == '8':
            output_file = input("Enter output Python file name (e.g., output.py): ")
            uml_generator.save_to_file(output_file)
            print(f'Python code generated and saved to {output_file}')
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
