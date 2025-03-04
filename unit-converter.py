import streamlit as st  

st.title("🔄️ Unit Converter App")  
st.markdown("### Converts Length, Weight, and Time Instantly")  
st.write("Welcome! Now you can convert your unit using this app")  


category = st.selectbox("Choose Your Unit", ["Length", "Weight", "Time"])  

def convert_units(category, value, unit):  
    if category == "Length":  
        if unit == "Kilometers to miles":  
            return value * 0.621371  
        elif unit == "Miles to kilometers":  
            return value / 0.621371  

    elif category == "Weight":  
        if unit == "Kilograms to pounds":  
            return value * 2.20462  
        elif unit == "Pounds to kilograms":  
            return value / 2.20462  

    elif category == "Time":  
        if unit == "Seconds to minutes":  
            return value / 60  
        elif unit == "Minutes to seconds":  
            return value * 60  
        elif unit == "Minutes to hours":  
            return value / 60  
        elif unit == "Hours to minutes":  
            return value * 60  
        elif unit == "Hours to days":  
            return value / 24  
        elif unit == "Days to hours":  
            return value * 24  


if category == "Length":  
    unit = st.selectbox("⇋ Select Conversion", ["Kilometers to miles", "Miles to kilometers"])  
elif category == "Weight":  
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])  
elif category == "Time":  
    unit = st.selectbox("⌚ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])  

 
value = st.number_input("Enter Your Value to Convert")  


if st.button("Convert"):  
    result = convert_units(category, value, unit)  
    st.success(f"The Result is {result: .2f}")  
