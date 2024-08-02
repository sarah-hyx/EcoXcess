from EcoXcess import PromptMotive
from EcoXcess import CarbonFootprintCalculator

def display_options():
    options = ["Suggest idea based on motive and location", "Input monthly carbon footprint", "Display monthly carbon footprint graph", "Tips and tricks", "Exit"]
    print("\n")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

def main():
    run = True
    while run:
        display_options()
        choice = input("What would you like to do?(Numbers only): ")
        
        if choice == "1":
            prompt_instance = PromptMotive()
            prompt_instance.response()
        elif choice == "2":
            cfp = CarbonFootprintCalculator()
            mileage, l_100, elec_usage = cfp.get_user_data()
            now, emissions = cfp.calculate_carbon_footprint(mileage, l_100, elec_usage)
            cfp.write_to_csv(now, emissions)
        elif choice == "3":
            months = []
            carbon_footprints = []
            with open("user_data.csv", "r") as file:
                file.readline()
                for line in file:
                    month, year, emission = line.strip().replace('"',"").split(",")
                    months.append(f"{month},{year}")
                    carbon_footprints.append(float(emission))
            months = months[-3:-1] + [months[-1]]
            carbon_footprints = carbon_footprints[-3:-1] +[carbon_footprints[-1]]
            
            data = {
                'Category': months,
                'Value': carbon_footprints
            }
            
            df = pd.DataFrame(data)
            ax = df.plot(kind='bar', x='Monthly digital footprint', y='Value', color='skyblue')
            ax.set_ylim(0, max(df['Value']) * 1.1)
            plt.show()
            
        elif choice == "4":
            motive = input("What would you like eco friendly tips and tricks on?: ")
            chat_session = model.start_chat()
            response = chat_session.send_message(f"5 Tips and tricks on how to {motive} in an eco-friendly manner in point form with a dash infront every new point without asterisks.")
            print(f"\n\nHere are some tips on how to {motive} in an eco-friendly manner:\n\n{response.text}")
        elif choice == "5":
            print("Thank you for using our programme!")
            run = False
        else:
            print("\nInvalid choice. Please select a valid option (1-4).")
main()
