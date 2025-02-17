import os

"""
Elizabeth Lourcey
Will be fully implemented pending more games moved into modules_directory
"""

class HelpManager:
    def __init__(self):
        self.manager = []

    # based on casino.py's get_submodules() function
    def add_message(self):
        for file in os.listdir("modules_directory"):
            if file.endswith(".py"):
                file = file[:-3]
                i = __import__('modules_directory.' + file, fromlist=[''])
                if (hasattr(i, 'help')):
                    self.manager.append(str(i.help))


    def print_message(self):
        for message in self.manager:
            print(message)


if __name__ == "__main__": # for testing
    help_manager = HelpManager()
    help_manager.add_message()
    user = input("type help if you need help\n")
    if user == "help":
        for message in help_manager.manager:
            help_manager.print_message()

