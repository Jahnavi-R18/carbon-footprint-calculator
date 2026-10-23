import matplotlib.pyplot as plt

# GLOBAL CONSTANTS: Emission factors in kg CO2e per unit
EF_ELECTRICITY = 0.85 # per kWh
EF_PETROL = 2.31 # per Litre
EF_DIESEL = 2.68 # per Litre
EF_LPG = 2.98 # per kg

def collect_inputs():
    print("\nCARBON FOOTPRINT CALCULATOR INPUTS \n")
    
    while True:
        try:
            electricity = float(input("Enter monthly Electricity usage (in kWh): "))
            petrol = float(input("Enter monthly Petrol consumed (in Litres): "))
            diesel = float(input("Enter monthly Diesel consumed (in Litres): "))
            lpg = float(input("Enter monthly LPG gas consumed (in kg): "))
            
            if electricity < 0 or petrol < 0 or diesel < 0 or lpg < 0:
                print("\nError: Inputs cannot be negative values. Try again.\n")
                continue
                
            return {
                "Electricity": electricity,
                "Petrol": petrol,
                "Diesel": diesel,
                "LPG": lpg
            }
        except ValueError:
            print("\nError: Please enter numerical digits only. Try again.\n")

def calculate_emissions(monthly_data):
    """Calculates annual emissions in Metric Tons."""
    elec_tons = (monthly_data["Electricity"] * EF_ELECTRICITY * 12) / 1000
    petrol_tons = (monthly_data["Petrol"] * EF_PETROL * 12) / 1000
    diesel_tons = (monthly_data["Diesel"] * EF_DIESEL * 12) / 1000
    lpg_tons = (monthly_data["LPG"] * EF_LPG * 12) / 1000
    
    results = {
        "Electricity": elec_tons,
        "Petrol": petrol_tons,
        "Diesel": diesel_tons,
        "LPG Cooking Gas": lpg_tons
    }
    return results

def show_charts(results_dict):
    categories = list(results_dict.keys())
    values = list(results_dict.values())
    
    #Pie Chart
    plt.figure(figsize=(6, 5))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Carbon Footprint Contribution (%)")
    print("Opening Pie Chart window...")
    plt.show()
    
    #Bar Chart
    plt.figure(figsize=(7, 5))
    plt.bar(categories, values, color='green', width=0.4)
    plt.title("Annual Carbon Footprint Magnitude")
    plt.xlabel("Emission Sources")
    plt.ylabel("Emissions (Metric Tons CO2e)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    print("Opening Bar Chart window...")
    plt.show()


if __name__ == "__main__":
    user_inputs = collect_inputs()
    
    calculated_results = calculate_emissions(user_inputs)
    
    total_annual = sum(calculated_results.values())
    trees_needed = round((total_annual * 1000) / 22)
    
    
    print("  ANNUAL CARBON AUDIT RESULTS ")
    print(f" Electricity : {calculated_results['Electricity']:.3f} Tons CO2e")
    print(f" Petrol : {calculated_results['Petrol']:.3f} Tons CO2e")
    print(f" Diesel : {calculated_results['Diesel']:.3f} Tons CO2e")
    print(f" LPG Gas : {calculated_results['LPG Cooking Gas']:.3f} Tons CO2e")
    print("--------------------------------------------------")
    print(f"TOTAL FOOTPRINT: {total_annual:.2f} Metric Tons CO2e/year")
    print(f"Offset Target : Plant approx. {trees_needed} trees to neutralize.")

    show_charts(calculated_results)
    print(" Program closed successfully.")

