from .controller import Controller
from .model import Model


def main():
    model = Model()
    controller = Controller(model)
    controller.run()


if __name__ == "__main__":
    main()

