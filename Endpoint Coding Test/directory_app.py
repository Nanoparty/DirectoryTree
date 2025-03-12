from file_system import FileSystem

class DirectoryApp:

    def __init__(self):
        self.fs = FileSystem()
        self.running = True
        
    def execute(self):
        while (self.running):
            user_input = input("")
            tokens = user_input.split(" ")
            command = tokens[0]
            args = tokens[1:]

            if command == "CREATE":
                if len(args) != 1:
                    print("Invalid args for command CREATE.\n Expected args are [directory].")
                    continue
                
                directory = args[0]
                self.fs.add_directory(directory)

            elif command == "LIST":
                if len(args) > 0:
                    print("Invalid args for command LIST. \n No expected args.")
                    continue

                self.fs.list_directories()

            elif command == "MOVE":
                if len(args) != 2:
                    print("Invalid args for command MOVE. \n Expected args are [source_directory] [target_directory]")
                    continue

                source_directory = args[0]
                target_directory = args[1]
                self.fs.move_directory(source_directory, target_directory)

            elif command == "DELETE":
                if len(args) != 1:
                    print("Invalid args for command DELETE. \n Expected args are [directory]")
                    continue

                directory = args[0]
                self.fs.delete_directory(directory)

            elif command == "EXIT":
                print("Exiting Program...")
                self.running = False;

            else:
                print("Invalid command. Valid commands are CREATE, LIST, MOVE, DELETE, EXIT")

if __name__ == '__main__':
    da = DirectoryApp()
    da.execute()

    