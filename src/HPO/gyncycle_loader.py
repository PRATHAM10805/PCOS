import libsbml


def load_gyncycle_model(path):

    document = libsbml.readSBML(path)

    if document.getNumErrors() > 0:
        document.printErrors()

        raise RuntimeError(
            "Could not load GynCycle SBML model."
        )

    model = document.getModel()

    if model is None:
        raise RuntimeError(
            "SBML file does not contain a model."
        )

    return model


def inspect_model(model):

    print("=" * 70)
    print("GYNCYCLE MODEL")
    print("=" * 70)

    print(
        f"\nModel ID: {model.getId()}"
    )

    print(
        f"Model name: {model.getName()}"
    )

    print(
        f"\nSpecies: "
        f"{model.getNumSpecies()}"
    )

    print(
        f"Parameters: "
        f"{model.getNumParameters()}"
    )

    print(
        f"Reactions: "
        f"{model.getNumReactions()}"
    )

    print("\nSTATE VARIABLES")
    print("-" * 70)

    for i in range(
        model.getNumSpecies()
    ):

        species = model.getSpecies(i)

        print(
            f"{i:3d} | "
            f"{species.getId():30s} | "
            f"{species.getName()}"
        )

    print("\nPARAMETERS")
    print("-" * 70)

    for i in range(
        model.getNumParameters()
    ):

        parameter = model.getParameter(i)

        print(
            f"{parameter.getId():30s} | "
            f"{parameter.getValue()}"
        )


def main():

    path = (
        "models/BIOMD0000000494.xml"
    )

    model = load_gyncycle_model(
        path
    )

    inspect_model(model)


if __name__ == "__main__":
    main()