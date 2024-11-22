row1=["😀 ", "😁 ", "😂 "]
row2=["😍 ", "🥰 ", "😘 "]
row3=["🥱 ", "😴 ", "😪 "]

map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position=input("where do you want to put the treasure ? ")
# print(type(place))
# position=place.split(",")


Outer_list=int(position[1])

inner_list=int(position[0])
horizontal=map[Outer_list-1]

horizontal[inner_list-1]="X"

print(f"{row1}\n{row2}\n{row3}")