# RF Test Calculator
# Calculates expected RF output power

print("=== RF Test Calculator ===")

input_power = float(input("Enter input power (dBm): "))
amplifier_gain = float(input("Enter amplifier gain (dB): "))
cable_loss = float(input("Enter cable loss (dB): "))
attenuation = float(input("Enter attenuator loss (dB): "))

output_power = input_power + amplifier_gain - cable_loss - attenuation

print("\n=== Test Results ===")
print(f"Input Power:      {input_power:.2f} dBm")
print(f"Amplifier Gain:  +{amplifier_gain:.2f} dB")
print(f"Cable Loss:      -{cable_loss:.2f} dB")
print(f"Attenuation:     -{attenuation:.2f} dB")
print("-----------------------------")
print(f"Expected Output:  {output_power:.2f} dBm")