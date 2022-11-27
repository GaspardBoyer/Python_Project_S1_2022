# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:45:39 2022

@author: gaspb
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
# streamlit run "C:\Users\gaspb\Downloads\Master 2 QE\Python coding\Project_Python\Coding\Project_Main_Script.py"
# Renaming our variable to make it clearer : 
df = pd.read_csv('C://Users//gaspb//Downloads//Master 2 QE//Python coding//Project_Python//Data//heart_failure.txt', sep=',')
df = df.rename(columns = {'age':'Age',
                          'anaemia':'Anaemia',
                          'creatinine_phosphokinase':'CPK',
                          'diabetes':'Diabetes',
                          'ejection_fraction':'Ejection fraction',
                          'high_blood_pressure':'High blood pressure',
                          'platelets':'Level of platelets',
                          'serum_creatinine':'Level of creatinine',
                          'serum_sodium':'Level of sodium',
                          'sex':'Sex',
                          'smoking':'Smoking',
                          'time':'Number of day pst the diagnostic',
                          'DEATH_EVENT':'Dead'})

st.title('Heart Failure Problem')

st.header('Introduction and descriptive statistic')
st.subheader('What is a heart faillure ?')
st.write('Heart failure is the inability of the heart muscle to normally propel blood through the body. It is a frequent and potentially severe disease, with a strong impact on the quality of life if it is not detected in time and treated. It can occur, for example, in the course of a myocardial infarction or angina pectoris.') 

st.write('Heart failure occurs when the heart loses some of its muscular strength and normal contraction capacity; it no longer pumps enough blood to allow the organs to receive enough oxygen and nutrients, which are essential for their proper functioning.')

st.write('Initially, the heart tries to adapt to the loss of its contraction force by accelerating its beats (increase in heart rate), then it increases in volume (thickening of the walls or dilation of the cardiac chambers). This extra workload for the heart eventually leads to heart failure.')

st.subheader('What are the indicator ?')
st.write('Thus, it is essential to detect it as soon as possible.' 
'To do this, doctors and other health specialists base their work on a number of physiological measurements. Among these we count : ')

physiological_measurements = st.selectbox(
    'Wish physiological measurements would you like to investigate ? ',
    ('CPK','Ejection fraction','Level of platelets', 'Level of creatinine', 'Level of sodium')
    )

distribution_physiological_measurements = px.histogram(df,physiological_measurements, color='Sex')
st.plotly_chart(distribution_physiological_measurements)

with st.expander('A little explanation ?'):
    if (physiological_measurements=='CPK'):
        st.write(' CPK or Creatine PhosphoKinase is an important protein in energy metabolism.'
                 'Its role is to replenish ATP (adenosine triphosphate) reserves, which can be used by the cell for its respiration and energy. Its determination is of interest in the diagnosis of myocardial infarction (increase in the MB fraction), muscle damage (increase in the MM fraction) and meningeal damage.')
        st.write('Its normal rate is for men: 0 - 195 IU/l and women: 0 - 170 IU/l, the main origins of an elevation of CPK are an attack of the cardiac muscle, skeletal muscles, meninges...etc')
    elif (physiological_measurements=='Ejection fraction'):
        st.write('The ejection fraction (EF) is the percentage of blood ejection from a heart chamber during a beat. '
                 'When the ejection fraction is decreased, the body can maintain cardiac output in two ways: by increasing the heart rate, or by maintaining a constant systolic ejection volume by increasing the end-diastolic volume of the ventricle. ')
        st.write('Increasing the end-diastolic volume results in dilation of the ventricle and thus the heart. This stretching of the cardiac muscle fibers, due to the elastic properties of the muscle fibers, allows a transient improvement of its contraction and is therefore an adaptation mechanism, often deleterious in the long term (Frank-Starling law).')
        st.write('When these compensation mechanisms are exceeded, cardiac output decreases and becomes insufficient for the body needs. A picture of cardiac insufficiency sets in.')
        st.write('It is of the order of 50 to 70% in the normal individual (typical normal value: 60%), and may be decreased in case of abnormal contractility, and may go down to 10-15% in case of major dysfunction, often responsible for heart failure. In case of heart failure, its value allows to distinguish between systolic (low ejection fraction) and diastolic heart failure (called "preserved systolic function").')        
    elif (physiological_measurements=='Level of platelets'):
        st.write('Work in Progress')
    elif (physiological_measurements=='Level of creatinine'):
        st.write('Creatinine is a chemical compound left over from the energy production processes in your muscles. Healthy kidneys filter creatinine from the blood. Creatinine leaves your body as a waste product in the urine.')
        st.write('Creatinine usually enters your bloodstream and is filtered out of the bloodstream at a generally constant rate. The amount of creatinine in your blood should be relatively stable. An increase in creatinine levels may be a sign of poor kidney function.')
        st.write('Serum creatinine is expressed in milligrams of creatinine per deciliter of blood (mg/dL) or micromoles of creatinine per liter of blood (micromoles/L). The typical range for serum creatinine is: For adult men, 0.74 to 1.35 mg/dL (65.4 to 119.3 micromoles/L). For adult women, 0.59 to 1.04 mg/dL (52.2 to 91.9 micromoles/L)')
    else :
        st.write('This test determines the amount of sodium in your blood. Sodium is particularly important for nerve and muscle function. Your body maintains sodium balance through various mechanisms. Sodium enters your bloodstream through food and drink. It leaves the bloodstream through urine, stool and sweat. Having the right amount of sodium is important for your health. Too much sodium can increase your blood pressure.')
        st.write('Normal results for this test are 135 to 145 mEq/L (milliequivalents per liter), according to the Mayo Clinic. But different labs use different values for "normal." A blood sodium level below 135 mEq/L is called hyponatremia. Hypernatremia means high levels of sodium in the blood. It is defined as levels that exceed 145 mEq/L. ')


