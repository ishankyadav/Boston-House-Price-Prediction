import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Boston House Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    model = joblib.load("boston_house_price_model.pkl")

    return model


model = load_model()


# =========================================================
# HEADER
# =========================================================

st.title("🏠 Boston House Price Prediction")

st.markdown(
    """
    ### Machine Learning Based House Price Predictor

    Enter the property details below and the trained machine
    learning model will estimate the house price.
    """
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("About the Project")

st.sidebar.info(
    """
    This application predicts Boston house prices
    using a regression-based machine learning model.

    The model was trained using the Boston Housing
    dataset with 13 input features.
    """
)

st.sidebar.markdown("### Model Features")

st.sidebar.write("• Crime Rate")
st.sidebar.write("• Residential Land")
st.sidebar.write("• Industrial Land")
st.sidebar.write("• Charles River")
st.sidebar.write("• Nitric Oxide")
st.sidebar.write("• Number of Rooms")
st.sidebar.write("• Building Age")
st.sidebar.write("• Distance")
st.sidebar.write("• Highway Accessibility")
st.sidebar.write("• Property Tax")
st.sidebar.write("• Pupil-Teacher Ratio")
st.sidebar.write("• Black Population Index")
st.sidebar.write("• Lower Status Population")


# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("🏡 Enter Property Details")

col1, col2, col3 = st.columns(3)


# ---------------------------------------------------------
# Column 1
# ---------------------------------------------------------

with col1:

    crim = st.number_input(
        "CRIM - Crime Rate",
        min_value=0.0,
        value=0.03,
        step=0.01,
        format="%.4f",
        help="Per capita crime rate by town."
    )

    zn = st.number_input(
        "ZN - Residential Land (%)",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Proportion of residential land zoned for lots over 25,000 sq.ft."
    )

    indus = st.number_input(
        "INDUS - Industrial Land (%)",
        min_value=0.0,
        value=7.0,
        step=0.1,
        help="Proportion of non-retail business acres per town."
    )

    chas = st.selectbox(
        "CHAS - Charles River",
        options=[0, 1],
        format_func=lambda x: "Yes (1)" if x == 1 else "No (0)",
        help="1 if tract bounds Charles River, otherwise 0."
    )

    nox = st.number_input(
        "NOX - Nitric Oxide",
        min_value=0.0,
        value=0.46,
        step=0.01,
        format="%.2f",
        help="Nitric oxide concentration."
    )


# ---------------------------------------------------------
# Column 2
# ---------------------------------------------------------

with col2:

    rm = st.number_input(
        "RM - Average Number of Rooms",
        min_value=1.0,
        value=6.5,
        step=0.1,
        format="%.2f",
        help="Average number of rooms per dwelling."
    )

    age = st.number_input(
        "AGE - Building Age (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0,
        help="Proportion of owner-occupied units built before 1940."
    )

    dis = st.number_input(
        "DIS - Distance to Employment Centers",
        min_value=0.0,
        value=4.5,
        step=0.1,
        format="%.2f",
        help="Weighted distance to five Boston employment centers."
    )

    rad = st.number_input(
        "RAD - Highway Accessibility",
        min_value=1,
        value=4,
        step=1,
        help="Index of accessibility to radial highways."
    )


# ---------------------------------------------------------
# Column 3
# ---------------------------------------------------------

with col3:

    tax = st.number_input(
        "TAX - Property Tax Rate",
        min_value=0.0,
        value=250.0,
        step=1.0,
        help="Full-value property-tax rate per $10,000."
    )

    ptratio = st.number_input(
        "PTRATIO - Pupil Teacher Ratio",
        min_value=0.0,
        value=18.0,
        step=0.1,
        format="%.2f",
        help="Pupil-teacher ratio by town."
    )

    b = st.number_input(
        "B - Population Index",
        min_value=0.0,
        value=390.0,
        step=1.0,
        help="Transformed population-related feature from the dataset."
    )

    lstat = st.number_input(
        "LSTAT - Lower Status Population (%)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.1,
        format="%.2f",
        help="Percentage of lower status population."
    )


# =========================================================
# PREDICTION
# =========================================================

st.divider()

predict_button = st.button(
    "🔮 Predict House Price",
    use_container_width=True
)


if predict_button:

    # Create input DataFrame
    input_data = pd.DataFrame({

        "CRIM": [crim],
        "ZN": [zn],
        "INDUS": [indus],
        "CHAS": [chas],
        "NOX": [nox],
        "RM": [rm],
        "AGE": [age],
        "DIS": [dis],
        "RAD": [rad],
        "TAX": [tax],
        "PTRATIO": [ptratio],
        "B": [b],
        "LSTAT": [lstat]

    })


    # Make prediction
    prediction = model.predict(input_data)[0]


    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.success("Prediction completed successfully!")

    st.subheader("🏠 Predicted House Price")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:

        st.metric(
            label="Estimated Price",
            value=f"${prediction:.2f}K"
        )

    with result_col2:

        st.metric(
            label="Estimated Price",
            value=f"${prediction * 1000:,.0f}"
        )

    with result_col3:

        st.metric(
            label="Rooms",
            value=f"{rm:.1f}"
        )


    st.info(
        """
        The predicted value is based on the trained machine
        learning model and the property characteristics entered above.

        The original MEDV target is expressed in thousands of dollars,
        so a prediction of 25.50 corresponds approximately to $25,500.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center">

    **Boston House Price Prediction System**

    Built using Python • Scikit-learn • Pandas • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)