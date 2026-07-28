from memory.memory_manager import MemoryManager


def main():
    memory = MemoryManager()

    memory.save("name", "Saman")
    memory.save("project", "AREN OS")

    print("Name:", memory.load("name"))
    print("Project:", memory.load("project"))


if __name__ == "__main__":
    main()