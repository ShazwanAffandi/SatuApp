import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_travel_budget():

  sysprompt = """You are a travel budget planner. You will be given a budget(in MYR) and a number of nights to stay. You will then give many recommend country (all continents) that is affordable within the given budget and number of nights. You will also give accommodation, activities, and other relevant details(include price for fly)."""

  st.title("Travel Budget Planner")
  st.write("Enter your budget and number of nights to stay.")

  st.header("Budget")
  budget = st.number_input("Enter your budget:", min_value=0)
  stay_nights = st.number_input("Number of nights:", min_value=1)
  generate_button = st.button("Generate")

  if generate_button:
    if not budget or not stay_nights:
      st.warning("Please enter both budget and number of nights.")
    else:
      prompt = f"Budget: {budget}, Number of nights: {stay_nights}"
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
              {
                  "role": "system",
                  "content": sysprompt
              },
              {
                  "role": "user",
                  "content": prompt
              },
          ],
          max_tokens=1000,
      )
      st.write(response.choices[0].message.content)


def main():
  generate_travel_budget()


if __name__ == "__main__":
  main()
