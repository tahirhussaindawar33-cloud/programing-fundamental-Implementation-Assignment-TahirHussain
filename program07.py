# Program 07 — Marks total & average

roll = input("Enter Roll No: ")
m1 = int(input("PF marks: "))
m2 = int(input("IC marks: "))
m3 = int(input("CG marks: "))
total = m1 + m2 + m3
avg = total / 3
print("Total =", total)
print("Average =", avg)
