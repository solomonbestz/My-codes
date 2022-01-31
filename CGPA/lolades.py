
grade_point = [3, 2, 3, 4, 2, 3, 5, 2, 5] 
units = [3, 2, 5, 4, 3, 3, 4, 2, 2]
total_quality_point = []

for n in range(len(units)):
    quality_point = grade_point[n] * units[n]
    total_quality_point.append(quality_point)
    
cgpa = sum(total_quality_point) / sum(units)

print("EMIABATA WASILAT")
print("19/5498")
print(f"Your cgpa is {round(cgpa, 2)}")