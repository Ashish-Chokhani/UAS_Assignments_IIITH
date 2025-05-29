import numpy as np
import scipy.integrate as spi

# Define the cosmological parameters
H0 = 67.4  # Hubble constant in km/s/Mpc
H0_s = H0 / (3.085677581e19)  # Convert to 1/s
Omega_L = 0.685
Omega_M = 0.315
Omega_R = 0.00005
Omega_K = 1.0 - (Omega_L + Omega_M + Omega_R)  # Assuming a flat universe

# Define the function inside the integral
def integrand(x):
    return 1 / (H0_s * x * np.sqrt(Omega_L + Omega_K * x**-2 + Omega_M * x**-3 + Omega_R * x**-4))

# Perform numerical integration
t_yr, _ = spi.quad(integrand, 0, 1)  # Integral in seconds
t_yr /= (60 * 60 * 24 * 365.25)  # Convert to years

# Convert to billion years
t_Gyr = t_yr / 1e9

print(f"Age of the Universe: {t_Gyr:.2f} billion years")