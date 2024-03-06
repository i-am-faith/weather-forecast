import streamlit as st
import plotly.express as px
from backend import get_data

# Set page title and icon
st.set_page_config(
    page_title="Weather Prediction",
    page_icon="☁️", 
)




# Streamlit Navbar
page_options = ["Home", "About", "Contact"]
selected_page = st.sidebar.radio("Navigation", page_options)

if selected_page == "Home":
    # Add title
    st.title("Weather Forecast")
    local_image_path = "images\weather_photo.jpg"
    st.image(local_image_path, use_column_width=True)

    place = st.text_input(label="Place", placeholder="Enter A City...", key="city")
    days = st.slider(
        label="Forecast days",
        min_value=1,
        max_value=5,
        key="days-slider",
        help="Select the number of forecasted days",
    )
    option = st.selectbox(
        label="Select type of data to view",
        options=(["Temperature", "Sky"]),
        key="dataselect",
    )
    st.subheader(f"{option} for the next {days} day(s) in {place}")

    # Get the temperature/sky data
    try:
        if place:
            filter_data = get_data(place, days)

            # Create a temperature plot
            if option == "Temperature":
                temps = [dict["main"]["temp"] / 10 for dict in filter_data]
                dates = [dict["dt_txt"] for dict in filter_data]
                figure = px.line(
                    x=dates, y=temps, labels={"x": "Date", "y": "temperature (C)"}
                )
                st.plotly_chart(figure)

            if option == "Sky":
                for day_num in range(days):
                    st.subheader(f"Day {day_num + 1} Sky Conditions:")
                    day_data = filter_data[day_num * 6 : (day_num + 1) * 6]
                    sky_conditions = [dict["weather"][0]["main"] for dict in day_data]
                    images = {
                        "Clear": "images/clear.png",
                        "Clouds": "images/cloud.png",
                        "Rain": "images/rain.png",
                        "Snow": "images/snow.png",
                    }
                    image_paths = [images[condition] for condition in sky_conditions]
                
                    # Concatenate timestamps and captions for each image
                    captions = [
                        f"{timestamp}: {condition}" for timestamp, condition in zip(["12am", "4am", "8am", "12pm", "4pm", "8pm"], sky_conditions)
                    ]
                
                    # Display all images in one line
                    st.image(image_paths, caption=captions, width=115)

    except KeyError:
        # st.error("Please enter a valid city")
        st.warning("PLEASE ENTER A VALID CITY!! ")
        st.warning(
        "If you are facing issues while searching for your City, you can try these methods:\n"
        "1. ✅ Double-check your spelling.\n"
        "2. ✅ Enter the appropriate city.\n"
        "3. ✅ It's possible that your requested geocode address is invalid"
        )


# About Page
elif selected_page == "About":

    st.title("About Us")

    st.write(
        "1. Welcome to Our Weather Prediction Application!\n"
        "2. I am Sourin Mukherjee with my team, dedicated to providing you with accurate and insightful weather predictions.\n"
        "3. ⚠️THIS WEBSITE IS USED FOR TRAINING AND DEVELOPMENT PURPOSES⚠️"
        )

    # Insert an image from a local file
    team_image = "images\project members.png"
    st.image(team_image, use_column_width=True)


    st.success("Thank you for choosing our Weather App!")


# Contact Page
elif selected_page == "Contact":
    import streamlit as st

    st.title("Contact Us")

    st.write("Feel free to reach out to us with any questions, feedback, or inquiries.")

    # Create form inputs
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)

    # Add a submit button
    if st.button("Submit"):
        # You can add your logic to handle the form submission here
        # For example, sending an email, storing the form data, etc.

        # Display a success message after submission
        st.success("Your message has been submitted successfully!")
    