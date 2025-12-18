from sys import argv
from app.command_processor import CommandProcessor
from service.purchase import Purchase


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    purchase = Purchase()
    processor = CommandProcessor(purchase)
    with open(argv[1]) as f:
        for line in f:
            processor.process(line.strip())
        

if __name__ == "__main__":
    main()
