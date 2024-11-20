temperatures = {
    "Monday": [67, 71, 74, 77],
    "Tuesday": [52, 56, 66, 50],
    "Wednesday": [77, 80, 87, 95],
    "Thursday": [67, 77, 81, 77],
    "Friday": [54, 60, 67, 60],
}
for k, v in temperatures.items():
    print(f"{k}: {sum(v)/len(v):.0f}")
