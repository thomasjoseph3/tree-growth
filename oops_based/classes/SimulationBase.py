class SimulationBase:
    """Base class for simulations, can hold shared attributes or methods."""
    def __init__(self, tree):
        self.tree = tree  # Reference to the Tree object

    def run(self):
        """Placeholder for running the simulation. Each subclass will implement specific logic."""
        raise NotImplementedError("Subclasses should implement this method.")
