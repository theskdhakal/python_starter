currentAgeYEar= input ("What is your current age in year? ")
reminderMonth=input("how many months after last birthday? ")

ageInMonth=int(currentAgeYEar)*12 + int(reminderMonth)

print(f"your age in month is {ageInMonth}")

remainingAge= (90*12) -int(ageInMonth)


ageinweeks=remainingAge*4
ageinDays=ageinweeks*7

print(f"you have {ageinDays} days, {ageinweeks} weeks, and {remainingAge} months left")