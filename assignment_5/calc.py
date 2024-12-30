import math

def calculate_c_i(s_i, tau_bit):
  """
  Calculates C_i based on the given formula.

  Args:
    s_i: The value of S_i.
    tau_bit: The bit time.

  Returns:
    The calculated value of C_i.
  """
  return (47 + 8 * s_i + math.floor((34 + 8 * s_i - 1) / 4)) * tau_bit

# Example usage
s_i = 8
tau_bit = 1000/450_000
c_i = calculate_c_i(s_i, tau_bit)
print(f"C_i = {c_i}")

