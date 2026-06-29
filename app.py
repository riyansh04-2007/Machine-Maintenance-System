import streamlit as st
import pandas as pd
import joblib

model=joblib.load('maintenance.pkl')

st.title('Machine Maintenance System')
st.markdown("Tell the condition of your machine: ")



air_temperature=st.number_input(
    "Air Temperature[k]",
    min_value=295.3,
    max_value=304.5,
    value=300.0,
    help="Enter the surrounding air temperature in Kelvin (K)."
)

process_temperature=st.number_input(
    "Process Temperature[k]",
    min_value=305.7,
    max_value=313.8,
    value=310.0,
    help="Enter the machine's process temperature in Kelvin (K)."
)

rpm=st.number_input(
    "Rotational Speed(rpm)",
    min_value=1168,
    max_value=2886,
    value=1540,
    help="Enter the rotational speed in revolutions per minute (RPM)."
)

torque=st.number_input(
    "Torque(Nm)",
    min_value=3.8,
    max_value=76.6,
    help="Enter the torque applied by the machine in Newton-meters (Nm)."
)

tool_wear=st.number_input(
    "Tool Wear",
    min_value=0,
    max_value=253,
    value=110,
    help="Enter the accumulated tool wear in minutes since the tool was last replaced."
)

machine_type=st.selectbox(
    "Machine Type",
    ['LOW','MEDIUM','HIGH'],
    index=None,
    help="Select the machine type: L (Low), M (Medium), or H (High)."
)

type_L=0
type_M=0
type_H=0

if machine_type=="Low":
    type_L=1
elif machine_type=="Medium":
    type_M=1
else:
    type_H=1


input_data=pd.DataFrame({
    'Air temperature [K]':[air_temperature],
    'Process temperature [K]':[process_temperature],
    'Rotational speed [rpm]':[rpm],
    'Torque [Nm]':[torque],
    'Tool wear [min]':[tool_wear],
    'Type_H':[type_H],
    'Type_L':[type_L],
    'Type_M':[type_M]
})

predict=st.button('Predict Machine Failure')
if predict:
    prediction=model.predict(input_data)

    if prediction[0]==0:
        st.success('Your Machine is healthy')
    else:
        st.error("Machine Failure")