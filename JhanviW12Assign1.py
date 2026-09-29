
Jhanvi_patients = {
    "ana" : (80, 50, 150, 90, 140),
    "ben" : (130, 140, 135, 90, 140),
    "carlo" : (90, 100, 95, 90, 140)
}
for patient, reading in Jhanvi_patients.items():
    high_count = 0
    average = 0
    print("\nPatient: ", patient)
    print("Blood sugar summary - ")
    for read in reading:
        average = sum(reading)/len(reading)
        if read > 120:
            print(read, "- High")
            high_count = high_count + 1
        else:
            print(read, "- Normal")

    print("Number of high readings:", high_count)
    print("Highest blood sugar count ", max(reading), "-", patient)
    print("Lowest blood sugar count ", min(reading), "-", patient)
    print(f"Average: {average:.2f}")
    print("Difference: ", max(reading)-min(reading))
