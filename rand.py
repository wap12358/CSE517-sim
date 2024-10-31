import random
import math

class RandomNumberGenerator:
    """
    A random number generator class for generating numbers based on various distributions.
    By default, generates numbers based on an exponential distribution.
    """
    def __init__(self):
        self.last_error = 0.0  # Error term to compensate for rounding bias in integer conversion
    
    def round_off(self, float_value):
        """
        Rounds a floating-point value to the nearest integer with error compensation.
        """
        # Apply error compensation
        compensated_value = float_value + self.last_error
        integer_value = int(compensated_value)  # Convert to integer
        self.last_error = compensated_value - integer_value  # Update error for next time
        return integer_value

    def exponential(self, rate):
        """
        Generates an integer based on an exponential distribution with the given rate parameter.
        Applies error compensation to ensure the rounding process does not skew the mean.
        """
        # Generate a uniform random number between 0 and 1
        u = random.uniform(0, 1)
        
        # Convert uniform random number to an exponential distribution
        exact_value = -math.log(1 - u) / rate

        return self.round_off(exact_value)

    def reset_error(self):
        """
        Resets the error term, useful if starting a new sequence or distribution.
        """
        self.last_error = 0.0