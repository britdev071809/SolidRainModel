"""Hydrogel simulation for Solid Rain polymer water absorption."""

class SolidRainModel:
    """Simulates water absorption and release cycles of Solid Rain polymer."""
    
    def __init__(self, initial_moisture=0.0):
        """Initialize the model with initial moisture level."""
        self.moisture = initial_moisture
    
    def calculate_retention_factor(self, humidity, temperature):
        """
        Calculate water retention factor based on environmental humidity and temperature.
        
        Args:
            humidity: Relative humidity (0-100%)
            temperature: Temperature in Celsius
        
        Returns:
            Retention factor (0-1)
        """
        # BUG: Incorrect handling of high humidity - factor can exceed 1.0
        # When humidity > 80%, retention should saturate, but current formula
        # incorrectly increases linearly.
        factor = (humidity / 100.0) * (1.0 - temperature / 100.0)
        return factor
    
    def calculate_absorption_rate(self, soil_moisture, polymer_amount):
        """
        Calculate absorption rate based on soil moisture and polymer amount.
        
        Args:
            soil_moisture: Moisture content of soil (0-1)
            polymer_amount: Amount of polymer applied (grams per hectare)
        
        Returns:
            Absorption rate (liters per hour)
        """
        # Simple linear model
        base_rate = 0.5  # liters per hour per gram
        rate = base_rate * soil_moisture * polymer_amount
        return rate
    
    def simulate_hour(self, humidity, temperature, soil_moisture, polymer_amount):
        """Simulate one hour of water retention and absorption."""
        retention = self.calculate_retention_factor(humidity, temperature)
        absorption = self.calculate_absorption_rate(soil_moisture, polymer_amount)
        # Simplified moisture change
        self.moisture = self.moisture * retention + absorption
        return self.moisture