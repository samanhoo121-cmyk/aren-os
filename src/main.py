from agents.content_agent import ContentAgent


def main():
    agent = ContentAgent()

    result = agent.execute("Create an Instagram post about AI")

    print(result)


if __name__ == "__main__":
    main()