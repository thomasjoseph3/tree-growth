from SimulationBase import SimulationBase

class TreeSimulation(SimulationBase):
    def __init__(self, tree, soil_quality,water_availability,temperature_adaptation,competition_index):
        super().__init__(tree)
        self.soil_quality = soil_quality
        self.water_availability=water_availability
        self.temperature_adaptation=temperature_adaptation
        self.competition_index=competition_index

    def run_soil_quality_simulation(self):
        """Run the soil quality calculation as part of the simulation."""
        soil_quality_score = self.soil_quality.calculate_soil_quality(self.tree)
        print(f"Soil Quality Score for {self.tree.name}: {soil_quality_score}")
        return soil_quality_score

    def run_water_availability_simulation(self):
        """Run the water availability calculation as part of the simulation."""
        water_availability_score = self.water_availability.calculate()
        print(f"Water Availability Score for {self.tree.name}: {water_availability_score}")
        return water_availability_score
    
    def run_temperature_adaptation_simulation(self):
        temperature_adaptation_score = self.temperature_adaptation.calculate()
        print(f"Temperature Adaptation Score for {self.tree.name}: {temperature_adaptation_score}")
        return temperature_adaptation_score  
    
    def run_competition_index_simulation(self):
        competition_index_score = self.competition_index.calculate()
        print(f"competition Index Score for {self.tree.name}: {competition_index_score}")
        return competition_index_score      
    
    def run(self):
        """Run all parts of the simulation."""
        self.run_soil_quality_simulation()
        self.run_water_availability_simulation()
        self.run_temperature_adaptation_simulation()
        self.run_competition_index_simulation()
