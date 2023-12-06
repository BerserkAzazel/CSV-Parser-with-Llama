import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from llamas import Llama

def main():
    st.title("Data Analysis App with Llama-2")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Load data into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)

        st.subheader("Data Overview")
        st.write(df.head())

        # Handle conversion of numeric values in string form
        df = convert_numeric_strings(df)

        st.subheader("Descriptive Statistics")

        # Select columns for analysis
        selected_columns = st.multiselect("Select columns for analysis", df.columns)

        if selected_columns:
            statistics_df = df[selected_columns].describe()
            st.write(statistics_df)

            st.subheader("Correlation Coefficient")
            correlation_matrix = df[selected_columns].corr()
            st.write(correlation_matrix)

            st.subheader("Plots")

            # Plot histograms
            st.subheader("Histograms")
            for column in selected_columns:
                plt.figure(figsize=(8, 6))
                sns.histplot(df[column], kde=True)
                plt.title(f"Histogram of {column}")
                st.pyplot()

            # Plot scatter plots
            st.subheader("Scatter Plots")
            for col1 in selected_columns:
                for col2 in selected_columns:
                    if col1 != col2:
                        plt.figure(figsize=(8, 6))
                        sns.scatterplot(data=df, x=col1, y=col2)
                        plt.title(f"Scatter Plot between {col1} and {col2}")
                        st.pyplot()

            # Plot pie charts
            st.subheader("Pie Charts")
            for column in selected_columns:
                if df[column].dtype == 'object':
                    plt.figure(figsize=(8, 8))
                    df[column].value_counts().plot.pie(autopct='%1.1f%%')
                    plt.title(f"Pie Chart for {column}")
                    st.pyplot()

            # Llama-2 integration for descriptive answers
            st.subheader("Descriptive Answers with Llama-2")
            llama = Llama()
            for column in selected_columns:
                answer = llama.ask_descriptive(df[column])
                st.write(f"Descriptive answer for {column}: {answer}")

    else:
        st.info("Please upload a CSV file.")

def convert_numeric_strings(df):
    # Convert numeric values in string form to float
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass
    return df

if __name__ == "__main__":
    main()
