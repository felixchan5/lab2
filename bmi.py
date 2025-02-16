def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    
    # Display BMI
    print("BMI = " + str(bmi))
    
    # Classify the BMI and return the corresponding value
    if bmi < 18.5:
        print("Weight Classification = Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification = Normal Weight")
        return 0
    else:
        print("Weight Classification = Over Weight")
        return 1

# Example usage
result = calculate_bmi(weight=57, height=1.73)
print("Return Value =", result)
