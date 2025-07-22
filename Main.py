
"""

Disease = Tuberculosis

S = susceptible
I = infected
R = recovered
D = dead

delta S =  -B * S * I / N + sigma * R
delta I = delta S - G * I - M * I
delta R = G * I - sigma * R
delta D = M * I
N = S + I + R 

N = 1000
S0 = 995
Io= 5
Ro = 0
Do = 0
sigma = 0.002 #immunity loss rate
B = 0.05 if rain B = 0.08  # Infection rate
G = 0.02  # Recovery rate
M = 0.005 # Mortality rate

20 % chance of rain
40 % chance of rain in monsoon season

10% chance of outbreak discoveration
if discovered 4 times
    B = 0.03
    G = 0.05
"""

from random import randint
import math

Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Fixed_Population = 347377000
Population = Fixed_Population
Infected = 9615
Susceptible = Fixed_Population-Infected
Recovered = 0
Dead = 0   
infection_rate = 0.05
Rainy_Infection_Rate = 0.08
recovery_rate = 0.02
mortality_rate = 0.005
Rain_Percentage = 20
Immunity_Loss_Rate = 0.002
Disovery_Counter = 0
day = 0
mon_num = 0
Discovery_Day = -100000
Month = Months[mon_num]
Year = 0

Quarantine = False

print("\033c", end="")
print(f"Year: {Year}")
print(f"Month: {Month}")
print(f"Day {0}")
print(f'Rainy day: {False}')
print(f"Quarantine: {Quarantine}")
print(f"Population: {int(Fixed_Population)}")
print(f"Susceptible: {int(Susceptible)}")
print(f"Infected: {int(Infected)}")
print(f"Recovered: {int(Recovered)}")
print(f"Dead: {int(Dead)}")
input()


for a in range(10000000000000000000000):

    # Set Month

    day +=1

    if day == 30:
        if Quarantine == True:
            Quarantine = False
            B = infection_rate
            recovery_rate = 0.02
            Disovery_Counter = 0
            Discovery_Day = -100000
    
       

        day = 0
        mon_num+=1

        if mon_num > 11:
            Year +=1
            mon_num = 0

        Month = Months[mon_num]   

    # Increase Rain in Monsoon Seasons

    if Month in ['Jun', 'Jul', 'Aug', 'Sep']:
        Rain_Percentage = 40

    # Check for rain

    if randint(1, 100) <= Rain_Percentage:
        B = Rainy_Infection_Rate

    else:

        B = infection_rate
    
    # Check Quaratine rate

    if randint(1, 100) <= 10:
        Disovery_Counter +=1
    
    if Disovery_Counter == 10:
        B = 0.03
        recovery_rate = 0.05
        Quarantine = True
        Discovery_Day = a+1

    Susceptible = Susceptible + ((-B * ((Susceptible * Infected) / Fixed_Population)) + Immunity_Loss_Rate * Recovered)
    Infected = Infected + (B * ((Susceptible * Infected)/Fixed_Population) - (recovery_rate * Infected) - (mortality_rate * Infected))
    Recovered = Recovered + ((recovery_rate * Infected) - Immunity_Loss_Rate * Recovered)
    Dead = Dead + (mortality_rate * Infected)
    Population = Susceptible + Infected + Recovered

    if (a+1) % 7 == 0 or int(Population) <= 0:

        print("\033c", end="")
        print(f"Year: {Year}")
        print(f"Month: {Month}")
        print(f"Day {a+1}")
        print(f"Rainy day: {B == Rainy_Infection_Rate}")
        print(f"Quarantine: {Quarantine}")
        print(f"Population: {math.ceil(Population)}")
        print(f"Susceptible: {math.ceil(Susceptible)}")
        print(f"Infected: {math.ceil(Infected)}")
        print(f"Recovered: {math.ceil(Recovered)}")
        print(f"Dead: {math.ceil(Dead)}")
        #input()

    if int(Infected) <= 0:
        print("No more infected individuals.")
        break




