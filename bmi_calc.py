import streamlit as st
from openai import OpenAI

# Connect to NVIDIA (paste your key below)
client = OpenAI(
api_key=NVIDIA_API_KEY,
base_url="https://integrate.api.nvidia.com/v1"
)

st.title("BMI Expert AI App")
st.write("The app gives you detailed analysis of your BMI along with a food choices.")

st.header("Enter your details below")

name = st.text_input("Enter your name")
wt = st.number_input("Enter your weight")
ht = st.number_input("Enter your height")

if st.button("Calculate BMI"):
    bmi = round(wt / (ht/100)**2,2)
    st.write(f"{name}, with your weight {wt} and height {ht}, your BMI is:{bmi}")

    st.write(".... AI Nutritionist Expert is analyzing your bmi and providing you with a diet plan and exercise suggestions....")

    prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as {bmi}. The user data is mainly of Indians. Give the analysis in a friendly tone and provide suggestions for a healthy lifestyle. Also, provide a diet plan for the user based on the BMI value in a table format. The diet plan should be for 7 days and should include breakfast, lunch, dinner, and snacks. Also, provide a list of exercises that the user can do to maintain a healthy lifestyle.The output shouldn't be more than 100 words."


    with st.status("Analyzing..."):
    # Ask the AI something
        response = client.chat.completions.create(
                    model="z-ai/glm-5.3-flash",
                    messages=[
                    {"role": "user", "content": prompt}
                    ]
                    )

    # print(response.text)
    st.write(response.choices[0].message.content)
    st.markdown(response.choices[0].message.content)
    
    # if st.button("Get AI Analysis"):
    #     prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, and BMI as {bmi}. The user data is mainly of Indians. Give the analysis in a friendly tone and provide suggestions for a healthy lifestyle. Also, provide a diet plan for the user based on the BMI value in a table format. The diet plan should be for 7 days and should include breakfast, lunch, dinner, and snacks. Also, provide a list of exercises that the user can do to maintain a healthy lifestyle.The output shouldn't be more than 100 words."
    #     # Ask the AI something
    #     response = client.chat.completions.create(
    #             model="z-ai/glm-5.3-flash",
    #             messages=[
    #             {"role": "user", "content": prompt}
    #             ]
    #             )
    #             # print(response.text)
    #     st.write(response.choices[0].message.content)
    #     st.markdown(response.choices[0].message.content)


