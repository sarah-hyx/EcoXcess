import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Configure the API key
genai.configure(api_key = "APIKEY")

# Load the generative model
model = genai.GenerativeModel(model_name="gemini-1.0-pro")

class PromptMotive:
    def __init__(self):
        self.motive = input("What do you want to do?: ")
        self.location = input("Your country or state?: ")
        self.prompt = f"Give me 5 sustainable ideas or places to {self.motive} in {self.location} in point form with a dash infront of each new point with no asterisks."

    def response(self):
        chat_session = model.start_chat()
        response = chat_session.send_message(self.prompt)
        print(f"\n\nHere are some eco-friendly suggestions to {self.motive}:\n\n{response.text}")


class CarbonFootprintCalculator:
    def __init__(self):
        self.cfp_perlitre = 2.352  
        self.cfp_perkwh = 0.433  
    
    def calculate_carbon_footprint(self, car_km, litres_per_100km, electricity_usage):
        now = self.get_month()
        car_emissions = (car_km / 100) * litres_per_100km * self.cfp_perlitre
        electricity_emissions = electricity_usage * self.cfp_perkwh
        total_emissions = car_emissions + electricity_emissions
        print(f"Total carbon footprint for {now} is {total_emissions} kilograms.")

        if total_emissions > 300:
            print("Try to reduce your carbon footprint next month!")
        else:
            print("Good job! your carbon footprint this month is below average. ")
            
        return now, total_emissions

    def get_month(self):
        month = input("Enter this month and year seperated by comma eg.(March 2024): ")
        return month
        
    def write_to_csv(self, month, emissions):
        with open("user_data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([month, emissions])

    def get_user_data(self):
        litres_per_100km = 0
        print("Please enter your data for the month to calculate your carbon footprint:")
        
        public_transport = input("Do you take public transport / cycle most of the time? (Y/N): ").lower()

        if public_transport == "y":
            car_km = 0
        elif public_transport == "n":
            car_km = float(input("Enter your car kilometres for this month (in km): "))
            litres_per_100km = float(input("Enter your car's fuel consumption (litres per 100 kilometers): "))
        else:
            print("Invalid input. Assuming you do not take public transport.")
            car_km = float(input("Enter your car kilometres for this month (in km): "))

            litres_per_100km = float(input("Enter your car's fuel consumption (litres per 100 kilometers): "))
        electricity_usage = float(input("Enter your electricity usage for this month (in kWh): "))

        return car_km, litres_per_100km, electricity_usage
