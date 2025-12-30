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
        # FIXED: Ensure factor stays within realistic bounds and saturates at high humidity
        # Temperature factor: 1 - temperature/100, clamped to non-negative
        temp_factor = max(0.0, 1.0 - temperature / 100.0)
        humidity_factor = humidity / 100.0
        factor = humidity_factor * temp_factor
        
        # Saturation for high humidity: cap at 0.95 when humidity > 80%
        if humidity > 80:
            factor = min(factor, 0.95)
        
        # Final clamp to [0, 1]
        return max(0.0, min(1.0, factor))
    
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