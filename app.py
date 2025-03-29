import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
from joblib import dump, load


# Main function to handle the Streamlit app
def main():
    # Sidebar menu options
    activities = ["About", "Monitoring System", "Developers"]
    option = st.sidebar.selectbox("Menu Bar:", activities)

    # About section
    if option == "About":
        # Display project information
        html_temp = """
        <div style="background-color: yellow; padding: 10px;">
            <center><h1>ABOUT OUR PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.title("What is Money Laundering?")
        image = Image.open("images/1.png")  # Ensure the image path is correct
        st.image(image, use_container_width=True)  # Updated parameter
        st.subheader(
            "Money laundering is the illegal process of concealing the origins of money obtained illegally by passing it through a complex sequence of banking transfers or commercial transactions."
        )

    # Monitoring System section
    elif option == "Monitoring System":
        st.title("TRANSACTION MONITORING SYSTEM")
        image = Image.open(
            "images/Magnify_Monitoring.jpg"
        )  # Ensure the image path is correct
        st.image(image, use_container_width=True)  # Updated parameter
        st.subheader("Please Upload Your Dataset")

        # File uploader for dataset
        data = st.file_uploader("Upload your dataset", type=["csv"])
        if data is not None:
            # Load and display the dataset
            df = pd.read_csv(data)
            st.dataframe(df.head(10))
            st.success("Data Successfully loaded")

            # Load the pre-trained model
            try:
                model = load("final_model.joblib")
            except FileNotFoundError:
                st.error(
                    "Model file 'final_model.joblib' not found. Please ensure it is in the correct directory."
                )
                return

            # Preprocessing function for the dataset
            def preprocessData(dataFrame):
                # Drop unnecessary columns
                try:
                    dataFrame = dataFrame.drop(["step", "nameOrig", "nameDest"], axis=1)
                except KeyError as e:
                    st.error(f"Missing columns in the dataset: {e}")
                    return None
                # Convert categorical variables to dummy/indicator variables
                x_new = pd.get_dummies(dataFrame)
                return x_new

            # Predict button
            if st.button("Predict"):
                st.balloons()  # Display balloons animation
                x_new = preprocessData(df)
                if x_new is not None:
                    # Make predictions and save results
                    df["y_prednew"] = model.predict(x_new)
                    df.to_csv(
                        "final_result.csv", index=False
                    )  # Save results to a CSV file
                    dump(model, "final_model.joblib")  # Save model using joblib
                    st.title("Your Output is")
                    st.dataframe(df)  # Display the results
                else:
                    st.error("Data preprocessing failed. Please check your dataset.")

    # Developers section
    elif option == "Developers":
        st.title("Developers")
        st.subheader("This project was developed by a team of passionate developers.")
        st.text("Contact: msdianuc07@gmail.com")


# Entry point for the Streamlit app
if __name__ == "__main__":
    main()
