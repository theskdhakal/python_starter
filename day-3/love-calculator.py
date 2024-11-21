print("Welcome to Love test program. Let's Begin !")

your_name=input(("Whats your name ? \n").lower())
lover_name=input(("Whats your loveer's name ? \n").lower())

combined_name=str(your_name)+ str(lover_name)
print(combined_name)


count_of_t=combined_name.count("t")
count_of_r=combined_name.count("r")
count_of_u=combined_name.count("u")
count_of_e=combined_name.count("e")

total_first_number=count_of_t + count_of_r + count_of_u + count_of_e

count_of_l=combined_name.count("l")
count_of_o=combined_name.count("o")
count_of_v=combined_name.count("v")
count_of_e=combined_name.count("e")

total_second_number=count_of_l + count_of_o + count_of_v + count_of_e


total_percentage=int(str(total_first_number) + str(total_second_number))

print(total_percentage)


if total_percentage <= 10 or total_percentage >= 90:
    print(f"Your love_score is {total_percentage},you guys mingle like coke and mentos")
elif 40<= total_percentage <= 50:
    print("Your love_score is {toal_percentage},You guys go alright")
else:
    print(f"your love score is {total_percentage}")

