import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
# Data Loading
df  = pd.read_csv('india-districts-census-2011.csv')
lat_long_df = pd.read_csv('district wise centroids.csv')
df = df.merge(lat_long_df,left_on='District name',right_on='District',how='inner')
df.drop(columns=['District','State name','District code'],inplace=True)
df["Sex Ratio"] = ((df["Male"]/df["Female"])*1000).round(0).astype(int)

# Data Preprocessing
# Demographic DataFrame
demographic_df = df[['State','Latitude','Longitude','District name','Population','Male','Female','Sex Ratio']]
# Social DataFrame (Caste Analysis)

social_df = df[['State','Latitude','Longitude','District name','Population','Male','Female','SC','Male_SC','Female_SC','ST','Male_ST','Female_ST']]

# Literacy DataFrame
literacy_df = df[['State','Latitude','Longitude','District name','Population','Literate','Male_Literate','Female_Literate','Male','Female']]

# Religion Dataframe
religion_df = df[['State','Latitude','Longitude','District name','Population','Hindus','Muslims','Christians','Sikhs','Buddhists','Jains','Others_Religions','Religion_Not_Stated']]

# Education DataFrame
education_df = df[['State', 'Latitude','Longitude','District name','Population',
				   'Below_Primary_Education',
				   'Primary_Education',
				   'Middle_Education',
				   'Secondary_Education',
				   'Higher_Education',
				   'Graduate_Education',
				   'Other_Education',
				   'Literate_Education',
				   'Illiterate_Education',
				   'Total_Education']]

# Workforce DataFrame
workforce_df = df[['State','Latitude','Longitude','District name','Population',
				   'Male_Workers',
				   'Female_Workers',
				   'Main_Workers',
				   'Marginal_Workers',
				   'Non_Workers',
				   'Cultivator_Workers',
				   'Agricultural_Workers',
				   'Household_Workers',
				   'Other_Workers']]

# Age Dataframe
age_df = df[['State','Latitude','Longitude','District name','Population',
			 'Age_Group_0_29',
			 'Age_Group_30_49',
			 'Age_Group_50',
			 'Age not stated']]

# Power Parity DataFrame
parity_df = df[['State','Latitude','Longitude','District name','Population',
				'Power_Parity_Less_than_Rs_45000',
				'Power_Parity_Rs_45000_90000',
				'Power_Parity_Rs_90000_150000',
				'Power_Parity_Rs_45000_150000',
				'Power_Parity_Rs_150000_240000',
				'Power_Parity_Rs_240000_330000',
				'Power_Parity_Rs_150000_330000',
				'Power_Parity_Rs_330000_425000',
				'Power_Parity_Rs_425000_545000',
				'Power_Parity_Rs_330000_545000',
				'Power_Parity_Above_Rs_545000',
				'Total_Power_Parity']]

# Married Couples DataFrame
married_df = df[['State','Latitude','Longitude','District name','Population',
				 'Married_couples_1_Households',
				 'Married_couples_2_Households',
				 'Married_couples_3_Households',
				 'Married_couples_3_or_more_Households',
				 'Married_couples_4_Households',
				 'Married_couples_5__Households',
				 'Married_couples_None_Households']]

# Ownership DataFrame
ownership_df = df[['State','Latitude','Longitude','District name',
				   'Ownership_Owned_Households',
				   'Ownership_Rented_Households']]

# Houshold Population
household_df = df[['State','Latitude','Longitude','District name',
				   'Household_size_1_person_Households',
				   'Household_size_2_persons_Households',
				   'Household_size_1_to_2_persons',
				   'Household_size_3_persons_Households',
				   'Household_size_3_to_5_persons_Households',
				   'Household_size_4_persons_Households',
				   'Household_size_5_persons_Households',
				   'Household_size_6_8_persons_Households',
				   'Household_size_9_persons_and_above_Households']]

# Household Amenities
amenities_df = df[['State','Latitude','Longitude','District name',
				   'Households_with_Bicycle',
				   'Households_with_Car_Jeep_Van',
				   'Households_with_Radio_Transistor',
				   'Households_with_Scooter_Motorcycle_Moped',
				   'Households_with_Telephone_Mobile_Phone_Landline_only',
				   'Households_with_Telephone_Mobile_Phone_Mobile_only',
				   'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car',
				   'Households_with_Television',
				   'Households_with_Telephone_Mobile_Phone',
				   'Households_with_Telephone_Mobile_Phone_Both']]

# Household Basic Amenities
Basic_Amenities_df = df[['State','Latitude','Longitude','District name',
						 'LPG_or_PNG_Households',
						 'Housholds_with_Electric_Lighting',
						 'Households_with_Internet',
						 'Households_with_Computer',
						 'Rural_Households',
						 'Urban_Households',
						 'Households']]

# social_df
social_df["Total_SC"] = social_df["Male_SC"] + social_df["Female_SC"]
social_df["Total_ST"] = social_df["Male_ST"] + social_df["Female_ST"]
social_df["General Popuation"] = social_df["Population"] - social_df["Total_SC"] - social_df["Total_ST"]
st.title("India Census Data Analysis")
st.sidebar.title("India Census Data Analysis")
st.sidebar.subheader("Select the level of analysis")

# Create selection options
districts = df['District name'].unique().tolist()
states = df['State'].unique().tolist()

# Separate district and state selection
level = st.sidebar.radio("Select level:", ["District", "State", "India"])

if level == "District":
            option = st.selectbox('Select District', districts)
            fig_map = px.scatter_mapbox(
            demographic_df[demographic_df["District name"]==option], 
            lat='Latitude', 
            lon='Longitude', 
            size='Population',
            color='Sex Ratio',
            title='Male Female Population Data',
            mapbox_style='carto-positron',
            zoom=4)
            
            social_data = social_df[social_df["District name"] == option]
            values = [social_data["Total_SC"].values[0], social_data["Total_ST"].values[0], social_data["General Popuation"].values[0]]
            labels = ["Total_SC", "Total_ST", "General Population"]
            fig_pie = px.pie(
                values=values,
                names=labels,
                title='Population Distribution',
                template='plotly_dark')

            fig_pie.update_layout(
                title_font_size=24, 
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            fig_pie.update_traces(
                hovertemplate='<b>%{label}</b><br>Population: %{value}<extra></extra>'
            )
            literacy_df["Not_Literate"] = literacy_df["Population"] - literacy_df["Literate"]
            literacy_df["Female_Not_Literate"] = literacy_df["Female"] - literacy_df["Female_Literate"]
            literacy_df["Male_Not_Literate"] = literacy_df["Male"] - literacy_df["Male_Literate"]
            literacy_temp_df = literacy_df[literacy_df["District name"] == option]
            # Categories (Male, Female, Overall) and subcategories (Literate, Not Literate)
            categories = ["Male", "Female", "Overall"]
            subcategories = ["Not Literate", "Literate"]

            # Values for each subcategory
            not_literate_values = [
                literacy_temp_df["Male_Not_Literate"].values[0],
                literacy_temp_df["Female_Not_Literate"].values[0],
                literacy_temp_df["Not_Literate"].values[0]
            ]
            literate_values = [
                literacy_temp_df["Male_Literate"].values[0],
                literacy_temp_df["Female_Literate"].values[0],
                literacy_temp_df["Literate"].values[0]
            ]

            # Create the bar chart
            fig_b = go.Figure()

            # Add bars for "Not Literate"
            fig_b.add_trace(go.Bar(
                x=categories,
                y=not_literate_values,  # Values for Not Literate
                name="Not Literate",
                marker_color='purple'
            ))

            # Add bars for "Literate"
            fig_b.add_trace(go.Bar(
                x=categories,
                y=literate_values,  # Values for Literate
                name="Literate",
                marker_color='green'
            ))

            # Customize layout
            fig_b.update_layout(
                title="Literacy Data by Gender and Overall",
                xaxis_title="Category",
                yaxis_title="Values",
                barmode='group',  # Group bars side by side
                template='plotly_dark',
                legend_title="Literacy Status"
            )
            religion_temp_df = religion_df[religion_df["District name"] == option][[ 'Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains', 'Others_Religions', 'Religion_Not_Stated']]
            religion_temp_df["Others"] = religion_temp_df["Others_Religions"] + religion_temp_df["Religion_Not_Stated"]
            religion_temp_df.drop(columns=['Others_Religions','Religion_Not_Stated'],inplace=True)
            fig_p =px.pie(
                values=religion_temp_df.values[0],
                names=religion_temp_df.columns,
                title='Religion Distribution',
                template='plotly_dark'
            )
            education_temp_df =education_df[education_df["District name"] == option][[ 'Below_Primary_Education', 'Primary_Education', 'Middle_Education', 'Secondary_Education', 'Higher_Education', 'Graduate_Education', 'Other_Education']]
            education_temp_df.rename(columns={'Below_Primary_Education':'Below Primary', 'Primary_Education':'Primary', 'Middle_Education':'Middle', 'Secondary_Education':'Secondary', 'Higher_Education':'Higher', 'Graduate_Education':'Graduate', 'Other_Education':'Other'},inplace=True)
            fig_bar = px.bar(
                x=education_temp_df.columns,
                y=education_temp_df.values[0],
                title='Education Distribution',
                labels={'x':'Category','y':'Population'},
                template='plotly_dark',
                text_auto=True
            )
            fig_bar.update_traces(textposition='outside')
            workforce_temp_df = workforce_df[workforce_df["District name"] == option][[ 'Main_Workers', 'Marginal_Workers', 'Non_Workers', 'Cultivator_Workers', 'Agricultural_Workers', 'Household_Workers', 'Other_Workers']]
            figg = px.bar(
                x=['Main Workers', 'Marginal Workers', 'Non Workers'],
                y=[workforce_temp_df['Main_Workers'].values[0], workforce_temp_df['Marginal_Workers'].values[0], workforce_temp_df['Non_Workers'].values[0]],
                labels={'x': 'Worker Categories', 'y': 'Number of Workers'},
                title='Workforce Distribution',
                template='plotly_dark',   
            )
            figg.update_traces(textposition='outside')
            age_temp_df = age_df[age_df["District name"] == option][[ 'Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']].rename(columns={'Age_Group_0_29':'0-29', 'Age_Group_30_49':'30-49', 'Age_Group_50':'50+'})
            fig_h = px.histogram(
                x=age_temp_df.columns,
                y=age_temp_df.values[0],
                title='Age Distribution',
                labels={'x':'Age Group','y':'Population'},
                template='plotly_dark'
            )
            parity_temp_df = parity_df[parity_df["District name"] == option][[ 'Power_Parity_Less_than_Rs_45000', 'Power_Parity_Rs_45000_90000', 'Power_Parity_Rs_90000_150000', 'Power_Parity_Rs_45000_150000', 'Power_Parity_Rs_150000_240000', 'Power_Parity_Rs_240000_330000', 'Power_Parity_Rs_150000_330000', 'Power_Parity_Rs_330000_425000', 'Power_Parity_Rs_425000_545000', 'Power_Parity_Rs_330000_545000', 'Power_Parity_Above_Rs_545000']].rename(columns={'Power_Parity_Less_than_Rs_45000':'Less than 45k', 'Power_Parity_Rs_45000_90000':'45k-90k', 'Power_Parity_Rs_90000_150000':'90k-150k', 'Power_Parity_Rs_45000_150000':'45k-150k', 'Power_Parity_Rs_150000_240000':'150k-240k', 'Power_Parity_Rs_240000_330000':'240k-330k', 'Power_Parity_Rs_150000_330000':'150k-330k', 'Power_Parity_Rs_330000_425000':'330k-425k', 'Power_Parity_Rs_425000_545000':'425k-545k', 'Power_Parity_Rs_330000_545000':'330k-545k', 'Power_Parity_Above_Rs_545000':'Above 545k'})

            fig_parity = px.histogram(
                x=parity_temp_df.columns,
                y=parity_temp_df.values[0],
                title='Power Parity Distribution',
                labels={'x':'Power Parity','y':'Population'},
                template='plotly_dark'
            )
            married_df["Married_couples_3_or_more_Households"] = married_df["Married_couples_3_Households"] + married_df["Married_couples_3_or_more_Households"] + married_df["Married_couples_4_Households"] + married_df["Married_couples_5__Households"]

            married_temp_df = married_df[married_df["District name"] == option][[ 'Married_couples_1_Households', 'Married_couples_2_Households', 'Married_couples_3_or_more_Households']].rename(columns={'Married_couples_1_Households':'1', 'Married_couples_2_Households':'2', 'Married_couples_3_or_more_Households':'3+','Married_couples_None_Households':'None'})

            fig_married = px.histogram(
                x=married_temp_df.columns,
                y=married_temp_df.values[0],
                title='Married Couples Distribution (Household wise)',
                labels={'x':'Number of Couples','y':'Households'},
                template='plotly_dark',
                log_y=True,
                text_auto=True
            )
            ownership_temp_df = ownership_df[ownership_df["District name"] == option][[ 'Ownership_Owned_Households', 'Ownership_Rented_Households']]
            ownership_temp_df.rename(columns={'Ownership_Owned_Households':'Owned','Ownership_Rented_Households':'Rented'},inplace=True)
            fig_own= px.bar(
                x=ownership_temp_df.columns,
                y=ownership_temp_df.values[0],
                title='Owned vs Rented Households',
                labels={'x':'Ownership','y':'Households'},
                template='plotly_dark',
                text_auto=True
            )
            household_temp_df = household_df[household_df["District name"] == option][[ 'Household_size_1_person_Households', 'Household_size_2_persons_Households', 'Household_size_3_persons_Households', 'Household_size_4_persons_Households', 'Household_size_5_persons_Households', 'Household_size_6_8_persons_Households', 'Household_size_9_persons_and_above_Households']]
            household_temp_df.rename(columns={'Household_size_1_person_Households':'1 Person Households', 'Household_size_2_persons_Households':'2 Persons Households', 'Household_size_3_persons_Households':'3 Persons Households', 'Household_size_4_persons_Households':'4 Persons Households', 'Household_size_5_persons_Households':'5 Persons Households', 'Household_size_6_8_persons_Households':'6-8 Persons Households', 'Household_size_9_persons_and_above_Households':'9+ Persons Households'},inplace=True)
            household_temp_df["6+ Persons Households"] = household_temp_df['6-8 Persons Households'] + household_temp_df['9+ Persons Households']
            household_temp_df.drop(columns=['6-8 Persons Households','9+ Persons Households'],inplace=True)
            fig_house = px.bar(
                x=household_temp_df.columns,
                y=household_temp_df.values[0],
                title='Household Size Distribution',
                labels={'x':'Size','y':'Total Population'},
                template='plotly_dark',
                text_auto=True
            )
            Basic_Amenities_temp_df1 = Basic_Amenities_df[Basic_Amenities_df["District name"] == option][['LPG_or_PNG_Households', 'Housholds_with_Electric_Lighting', 'Households_with_Internet', 'Households_with_Computer']].rename(columns={'LPG_or_PNG_Households':'LPG/PNG', 'Housholds_with_Electric_Lighting':'Electric Lighting', 'Households_with_Internet':'Internet', 'Households_with_Computer':'Computer'})
            Basic_Amenities_temp_df2 = Basic_Amenities_df[Basic_Amenities_df["District name"] == option][['Rural_Households', 'Urban_Households']].rename(columns={'Rural_Households':'Rural', 'Urban_Households':'Urban'})
            fig_basic = px.bar(
                x=Basic_Amenities_temp_df1.columns,
                y=Basic_Amenities_temp_df1.values[0],
                title='Basic Amenities Distribution',
                labels={'x':'Amenity','y':'Households'},
                template='plotly_dark',
                text_auto=True,log_y=True
            )
            fig_basic2 = px.bar(
                x=Basic_Amenities_temp_df2.columns,
                y=Basic_Amenities_temp_df2.values[0],
                title='Rural vs Urban Households',
                labels={'x':'Household Type','y':'Households'},
                template='plotly_dark',
                text_auto=True
            )
            amenities_temp_df1 = amenities_df[amenities_df["District name"] == option][[ 'Households_with_Bicycle', 'Households_with_Scooter_Motorcycle_Moped','Households_with_Car_Jeep_Van']].rename(columns={'Households_with_Bicycle':'Bicycle', 'Households_with_Scooter_Motorcycle_Moped':'Scooter/Motorcycle/Moped', 'Households_with_Car_Jeep_Van':'Car/Jeep/Van'})
            amenities_temp_df2 = amenities_df[amenities_df["District name"] == option][[ 'Households_with_Radio_Transistor','Households_with_Television','Households_with_Telephone_Mobile_Phone_Landline_only','Households_with_Telephone_Mobile_Phone_Mobile_only','Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']].rename(columns={'Households_with_Radio_Transistor':'Radio','Households_with_Television':'Television','Households_with_Telephone_Mobile_Phone_Landline_only':'Landline','Households_with_Telephone_Mobile_Phone_Mobile_only':'Mobile','Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car':'All Electronic Amenities'})
            amenities_temp_df3 = amenities_df[amenities_df["District name"] == option][['Households_with_Telephone_Mobile_Phone_Landline_only',
                'Households_with_Telephone_Mobile_Phone_Mobile_only',
                'Households_with_Telephone_Mobile_Phone_Both']].rename(columns={'Households_with_Telephone_Mobile_Phone_Landline_only':'Landline', 'Households_with_Telephone_Mobile_Phone_Mobile_only':'Mobile', 'Households_with_Telephone_Mobile_Phone_Both':'Both'})
            fig_amenities = px.bar(
                x=amenities_temp_df1.columns,
                y=amenities_temp_df1.values[0],
                title='2 Wheelers and 4 Wheelers Distribution',
                labels={'x':'Vehicle Type','y':'Households'},
                template='plotly_dark',
                text_auto=True
            )

            fig_amenities1 = px.bar(
                x=amenities_temp_df2.columns,
                y=amenities_temp_df2.values[0],
                title='Electronic Amenities Distribution',
                labels={'x':'Amenity','y':'Households'},
                template='plotly_dark',
                text_auto=True
            )

            fig_amenities2 = px.bar(
                x=amenities_temp_df3.columns,
                y=amenities_temp_df3.values[0],
                title='Telephone Distribution',
                labels={'x':'Type','y':'Households'},
                template='plotly_dark',
                text_auto=True
            )
            
            st.plotly_chart(fig_map, use_container_width=True)
            st.plotly_chart(fig_pie, use_container_width=True)
            st.plotly_chart(fig_b, use_container_width=True)
            st.plotly_chart(fig_p, use_container_width=True)
            st.plotly_chart(fig_bar, use_container_width=True)
            st.plotly_chart(figg, use_container_width=True)
            st.plotly_chart(fig_h, use_container_width=True)
            st.plotly_chart(fig_parity, use_container_width=True)
            st.plotly_chart(fig_married, use_container_width=True)
            st.plotly_chart(fig_house, use_container_width=True)
            st.plotly_chart(fig_own, use_container_width=True)
            st.plotly_chart(fig_basic, use_container_width=True)
            st.plotly_chart(fig_basic2, use_container_width=True)
            st.plotly_chart(fig_amenities, use_container_width=True)
            st.plotly_chart(fig_amenities1, use_container_width=True)
            st.plotly_chart(fig_amenities2, use_container_width=True) 
            
elif level == "State":
    option = st.selectbox('Select State', states)
    temp_state_df = df[df["State"]==option][["District name","Population","Sex Ratio","Literate","Latitude","Longitude"]]
    fig_map = px.scatter_mapbox(
        temp_state_df, 
        lat='Latitude', 
        lon='Longitude', 
        size="Literate",
        color='Sex Ratio',
        title='Population Data',
        mapbox_style='carto-positron',
        hover_data=["District name","Population","Sex Ratio"],
        zoom=5,
        template='plotly_dark'
    )
    social_data = social_df[social_df["State"] == option]
    values = [social_data["Total_SC"].sum(), social_data["Total_ST"].sum(), social_data["General Popuation"].sum()]
    labels = ["Total_SC", "Total_ST", "General Population"]

    fig_pie = px.pie(
        values=values,
        names=labels,
        title='Population Distribution',
        template='plotly_dark'  
    )

    fig_pie.update_layout(
        title_font_size=24, 
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    fig_pie.update_traces(
        hovertemplate='<b>%{label}</b><br>Population: %{value}<extra></extra>'
    )

    education_temp_df =education_df[education_df["State"] == option][[ 'Below_Primary_Education', 'Primary_Education', 'Middle_Education', 'Secondary_Education', 'Higher_Education', 'Graduate_Education', 'Other_Education']]
    education_temp_df.rename(columns={'Below_Primary_Education':'Below Primary', 'Primary_Education':'Primary', 'Middle_Education':'Middle', 'Secondary_Education':'Secondary', 'Higher_Education':'Higher', 'Graduate_Education':'Graduate', 'Other_Education':'Other'},inplace=True)
    fig_edu = px.bar(
        x=education_temp_df.columns,
        y=education_temp_df.sum().values,
        title='Education Distribution',
        labels={'x':'Category','y':'Population'},
        template='plotly_dark',
        text_auto=True
    )
    age_temp_df = age_df[age_df["State"] == option][[ 'Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']].rename(columns={'Age_Group_0_29':'0-29', 'Age_Group_30_49':'30-49', 'Age_Group_50':'50+'})
    fig_rem1 = px.histogram(
        x=age_temp_df.columns,
        y=age_temp_df.sum().values,
        title='Age Distribution',
        labels={'x':'Age Group','y':'Population'},
        template='plotly_dark'
    )

    married_df["Married_couples_3_or_more_Households"] = married_df["Married_couples_3_Households"] + married_df["Married_couples_3_or_more_Households"] + married_df["Married_couples_4_Households"] + married_df["Married_couples_5__Households"]

    married_temp_df = married_df[married_df["State"] == option][[ 'Married_couples_1_Households', 'Married_couples_2_Households', 'Married_couples_3_or_more_Households']].rename(columns={'Married_couples_1_Households':'1', 'Married_couples_2_Households':'2', 'Married_couples_3_or_more_Households':'3+','Married_couples_None_Households':'None'})

    fig_rem2 = px.histogram(
        x=married_temp_df.columns,
        y=married_temp_df.sum().values,
        title='Married Couples Distribution (Household wise)',
        labels={'x':'Number of Couples','y':'Households'},
        template='plotly_dark',
        log_y=True,
        text_auto=True
    )
    ownership_temp_df = ownership_df[ownership_df["State"] == option][[ 'Ownership_Owned_Households', 'Ownership_Rented_Households']]
    ownership_temp_df.rename(columns={'Ownership_Owned_Households':'Owned','Ownership_Rented_Households':'Rented'},inplace=True)
    fig_rem3 = px.bar(
        x=ownership_temp_df.columns,
        y=ownership_temp_df.sum().values, 
        title='Owned vs Rented Households',
        labels={'x':'Ownership','y':'Households'},
        template='plotly_dark',
        text_auto=True
    )
    household_temp_df = household_df[household_df["State"] == option][[ 'Household_size_1_person_Households', 'Household_size_2_persons_Households', 'Household_size_3_persons_Households', 'Household_size_4_persons_Households', 'Household_size_5_persons_Households', 'Household_size_6_8_persons_Households', 'Household_size_9_persons_and_above_Households']]
    household_temp_df.rename(columns={'Household_size_1_person_Households':'1 Person Households', 'Household_size_2_persons_Households':'2 Persons Households', 'Household_size_3_persons_Households':'3 Persons Households', 'Household_size_4_persons_Households':'4 Persons Households', 'Household_size_5_persons_Households':'5 Persons Households', 'Household_size_6_8_persons_Households':'6-8 Persons Households', 'Household_size_9_persons_and_above_Households':'9+ Persons Households'},inplace=True)
    household_temp_df["6+ Persons Households"] = household_temp_df['6-8 Persons Households'] + household_temp_df['9+ Persons Households']
    household_temp_df.drop(columns=['6-8 Persons Households','9+ Persons Households'],inplace=True)
    fig_rem4 = px.bar(
        x=household_temp_df.columns,
        y=household_temp_df.sum().values,
        title='Household Size Distribution',
        labels={'x':'Size','y':'Total Population'},
        template='plotly_dark',
        text_auto=True
    )
    
    Basic_Amenities_temp_df1 = Basic_Amenities_df[Basic_Amenities_df["State"] == option][['LPG_or_PNG_Households', 'Housholds_with_Electric_Lighting', 'Households_with_Internet', 'Households_with_Computer']].rename(columns={'LPG_or_PNG_Households':'LPG/PNG', 'Housholds_with_Electric_Lighting':'Electric Lighting', 'Households_with_Internet':'Internet', 'Households_with_Computer':'Computer'})
    Basic_Amenities_temp_df2 = Basic_Amenities_df[Basic_Amenities_df["State"] == option][['Rural_Households', 'Urban_Households']].rename(columns={'Rural_Households':'Rural', 'Urban_Households':'Urban'})
    fig_rem5 = px.bar(
        x=Basic_Amenities_temp_df1.columns,
        y=Basic_Amenities_temp_df1.sum().values,
        title='Basic Amenities Distribution',
        labels={'x':'Amenity','y':'Households'},
        template='plotly_dark',
        text_auto=True,log_y=True
    )
    fig_rem6 = px.bar(
        x=Basic_Amenities_temp_df2.columns,
        y=Basic_Amenities_temp_df2.sum().values,
        title='Rural vs Urban Households',
        labels={'x':'Household Type','y':'Households'},
        template='plotly_dark',
        text_auto=True
    )

    amenities_temp_df1 = amenities_df[amenities_df["State"] == option][['Households_with_Bicycle', 'Households_with_Scooter_Motorcycle_Moped','Households_with_Car_Jeep_Van']].rename(columns={'Households_with_Bicycle':'Bicycle', 'Households_with_Scooter_Motorcycle_Moped':'Scooter/Motorcycle/Moped', 'Households_with_Car_Jeep_Van':'Car/Jeep/Van'})
    amenities_temp_df2 = amenities_df[amenities_df["State"] == option][['Households_with_Radio_Transistor','Households_with_Television','Households_with_Telephone_Mobile_Phone_Landline_only','Households_with_Telephone_Mobile_Phone_Mobile_only','Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']].rename(columns={'Households_with_Radio_Transistor':'Radio','Households_with_Television':'Television','Households_with_Telephone_Mobile_Phone_Landline_only':'Landline','Households_with_Telephone_Mobile_Phone_Mobile_only':'Mobile','Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car':'All Electronic Amenities'})
    amenities_temp_df3 = amenities_df[amenities_df["State"] == option][['Households_with_Telephone_Mobile_Phone_Landline_only',
        'Households_with_Telephone_Mobile_Phone_Mobile_only',
        'Households_with_Telephone_Mobile_Phone_Both']].rename(columns={'Households_with_Telephone_Mobile_Phone_Landline_only':'Landline', 'Households_with_Telephone_Mobile_Phone_Mobile_only':'Mobile', 'Households_with_Telephone_Mobile_Phone_Both':'Both'})
    fig_rem7 = px.bar(
        x=amenities_temp_df1.columns,
        y=amenities_temp_df1.sum().values,
        title='2 Wheelers and 4 Wheelers Distribution',
        labels={'x':'Vehicle Type','y':'Households'},
        template='plotly_dark',
        text_auto=True
    )

    fig_rem8 = px.bar(
        x=amenities_temp_df2.columns,
        y=amenities_temp_df2.sum().values, 
        title='Electronic Amenities Distribution',
        labels={'x':'Amenity','y':'Households'},
        template='plotly_dark',
        text_auto=True
    )
    fig_rem9 = px.bar(
        x=amenities_temp_df3.columns,
        y=amenities_temp_df3.sum().values, 
        title='Telephone Distribution',
        labels={'x':'Type','y':'Households'},
        template='plotly_dark',
        text_auto=True
    )
    fig_edu.update_traces(textposition='outside')
    st.plotly_chart(fig_map, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.plotly_chart(fig_edu, use_container_width=True)
    st.plotly_chart(fig_rem1, use_container_width=True)
    st.plotly_chart(fig_rem2, use_container_width=True)
    st.plotly_chart(fig_rem3, use_container_width=True)
    st.plotly_chart(fig_rem4, use_container_width=True)
    st.plotly_chart(fig_rem5, use_container_width=True)
    st.plotly_chart(fig_rem6, use_container_width=True)
    st.plotly_chart(fig_rem7, use_container_width=True)
    st.plotly_chart(fig_rem8, use_container_width=True)
    st.plotly_chart(fig_rem9, use_container_width=True)
else: 
        # Age Group Distribution
        age_temp_df = age_df[['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']].rename(
            columns={
                'Age_Group_0_29': '0-29', 
                'Age_Group_30_49': '30-49', 
                'Age_Group_50': '50+'
            }
        )
        fig = px.histogram(
            x=age_temp_df.columns,
            y=age_temp_df.sum().values,
            title='Age Distribution',
            labels={'x': 'Age Group', 'y': 'Population'},
            template='plotly_dark',
            text_auto=True
        )
        
        # Married Couples Distribution
        married_df["Married_couples_3_or_more_Households"] = (
            married_df["Married_couples_3_Households"] +
            married_df["Married_couples_3_or_more_Households"] +
            married_df["Married_couples_4_Households"] +
            married_df["Married_couples_5__Households"]
        )
        married_temp_df = married_df[['Married_couples_1_Households', 'Married_couples_2_Households', 'Married_couples_3_or_more_Households']].rename(
            columns={
                'Married_couples_1_Households': '1',
                'Married_couples_2_Households': '2',
                'Married_couples_3_or_more_Households': '3+'
            }
        )
        fig_1 = px.histogram(
            x=married_temp_df.columns,
            y=married_temp_df.sum().values,
            title='Married Couples Distribution (Household-wise)',
            labels={'x': 'Number of Couples', 'y': 'Households'},
            template='plotly_dark',
            log_y=True,
            text_auto=True
        )

        # Ownership Distribution
        ownership_temp_df = ownership_df[ownership_df["State"] == "Tamil Nadu"][['Ownership_Owned_Households', 'Ownership_Rented_Households']].rename(
            columns={
                'Ownership_Owned_Households': 'Owned',
                'Ownership_Rented_Households': 'Rented'
            }
        )
        fig_2 = px.bar(
            x=ownership_temp_df.columns,
            y=ownership_temp_df.sum().values, 
            title='Owned vs Rented Households',
            labels={'x': 'Ownership', 'y': 'Households'},
            template='plotly_dark',
            text_auto=True
        )

        # Household Size Distribution
        household_temp_df = household_df[['Household_size_1_person_Households', 'Household_size_2_persons_Households', 'Household_size_3_persons_Households', 'Household_size_4_persons_Households', 'Household_size_5_persons_Households', 'Household_size_6_8_persons_Households', 'Household_size_9_persons_and_above_Households']].rename(
            columns={
                'Household_size_1_person_Households': '1 Person Households',
                'Household_size_2_persons_Households': '2 Persons Households',
                'Household_size_3_persons_Households': '3 Persons Households',
                'Household_size_4_persons_Households': '4 Persons Households',
                'Household_size_5_persons_Households': '5 Persons Households',
                'Household_size_6_8_persons_Households': '6-8 Persons Households',
                'Household_size_9_persons_and_above_Households': '9+ Persons Households'
            }
        )
        household_temp_df["6+ Persons Households"] = (
            household_temp_df['6-8 Persons Households'] + 
            household_temp_df['9+ Persons Households']
        )
        household_temp_df.drop(columns=['6-8 Persons Households', '9+ Persons Households'], inplace=True)
        fig_3 = px.bar(
            x=household_temp_df.columns,
            y=household_temp_df.sum().values,
            title='Household Size Distribution',
            labels={'x': 'Size', 'y': 'Total Population'},
            template='plotly_dark',
            text_auto=True
        )

        # Amenities Distribution
        amenities_temp_df1 = amenities_df[['Households_with_Bicycle', 'Households_with_Scooter_Motorcycle_Moped', 'Households_with_Car_Jeep_Van']].rename(
            columns={
                'Households_with_Bicycle': 'Bicycle',
                'Households_with_Scooter_Motorcycle_Moped': 'Scooter/Motorcycle/Moped',
                'Households_with_Car_Jeep_Van': 'Car/Jeep/Van'
            }
        )
        fig4 = px.bar(
            x=amenities_temp_df1.columns,
            y=amenities_temp_df1.sum().values,
            title='2-Wheelers and 4-Wheelers Distribution',
            labels={'x': 'Vehicle Type', 'y': 'Households'},
            template='plotly_dark',
            text_auto=True
        )

        amenities_temp_df2 = amenities_df[['Households_with_Radio_Transistor', 'Households_with_Television', 'Households_with_Telephone_Mobile_Phone_Landline_only', 'Households_with_Telephone_Mobile_Phone_Mobile_only', 'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']].rename(
            columns={
                'Households_with_Radio_Transistor': 'Radio',
                'Households_with_Television': 'Television',
                'Households_with_Telephone_Mobile_Phone_Landline_only': 'Landline',
                'Households_with_Telephone_Mobile_Phone_Mobile_only': 'Mobile',
                'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car': 'All Electronic Amenities'
            }
        )
        fig5 = px.bar(
            x=amenities_temp_df2.columns,
            y=amenities_temp_df2.sum().values, 
            title='Electronic Amenities Distribution',
            labels={'x': 'Amenity', 'y': 'Households'},
            template='plotly_dark',
            text_auto=True
        )

        amenities_temp_df3 = amenities_df[['Households_with_Telephone_Mobile_Phone_Landline_only', 'Households_with_Telephone_Mobile_Phone_Mobile_only', 'Households_with_Telephone_Mobile_Phone_Both']].rename(
            columns={
                'Households_with_Telephone_Mobile_Phone_Landline_only': 'Landline',
                'Households_with_Telephone_Mobile_Phone_Mobile_only': 'Mobile',
                'Households_with_Telephone_Mobile_Phone_Both': 'Both'
            }
        )
        fig6 = px.bar(
            x=amenities_temp_df3.columns,
            y=amenities_temp_df3.sum().values, 
            title='Telephone Distribution',
            labels={'x': 'Type', 'y': 'Households'},
            template='plotly_dark',
            text_auto=True
        )

        # Sidebar Selection
        st.header("Parameter Selection")
        parameter_options = ['Population', 'Male', 'Female', 'Literate', 'Male_Literate', 'Female_Literate', 
            'SC', 'Male_SC', 'Female_SC', 'ST', 'Male_ST', 'Female_ST', 'Workers', 'Male_Workers', 'Female_Workers',
            'Main_Workers', 'Marginal_Workers', 'Non_Workers', 'Cultivator_Workers', 'Agricultural_Workers', 
            'Household_Workers', 'Other_Workers', 'Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains',
            'Others_Religions', 'LPG_or_PNG_Households', 'Households_with_Electric_Lighting', 'Households_with_Internet',
            'Households_with_Computer', 'Rural_Households', 'Urban_Households', 'Households', 'Below_Primary_Education',
            'Primary_Education', 'Middle_Education', 'Secondary_Education', 'Higher_Education', 'Graduate_Education',
            'Other_Education', 'Literate_Education', 'Illiterate_Education', 'Total_Education', 'Households_with_Bicycle',
            'Households_with_Car_Jeep_Van', 'Households_with_Radio_Transistor', 'Households_with_Scooter_Motorcycle_Moped',
            'Households_with_Telephone_Mobile_Phone_Landline_only', 'Households_with_Telephone_Mobile_Phone_Mobile_only',
            'Households_with_Television', 'Households_with_Telephone_Mobile_Phone', 'Ownership_Owned_Households',
            'Ownership_Rented_Households', 'Total_Power_Parity', 'State', 'Sex Ratio'
        ]
        parameter1 = st.selectbox("Select Parameter 1 (X-Axis):", parameter_options)
        parameter2 = st.selectbox("Select Parameter 2 (Y-Axis):", parameter_options)
        
        st.button("Click to Generate Scatter Plot")
        st.title("Geographical Scatter Plot")
        if st.button:
            if parameter1 and parameter2:
                fig_ure = px.scatter_geo(
                    df,
                    lat='Latitude',
                    lon='Longitude',
                    color=parameter1,
                    size=parameter2,
                    hover_name='District name',
                    hover_data=[parameter1, parameter2],
                    projection='natural earth',
                    title=f"Scatter Plot of {parameter1} vs {parameter2}"
                )

# Update the layout for increased size and zoom functionality
                fig_ure.update_layout(
                    width=1000,  # Adjust the width
                    height=800,  # Adjust the height
                    title_font_size=20,  # Increase title font size for better visibility
                    dragmode='zoom',  # Enable zooming
                    uirevision='constant',  # Keep zoom level when interacting
                    geo=dict(
                        showcountries=True,  # Show country borders
                        showland=True,       # Highlight land
                        landcolor="LightGreen",
                        subunitcolor="gray",
                        countrycolor="gray",
                        coastlinecolor="black",
                        projection_scale=7  # Control zoom level
                    )
                )
                st.plotly_chart(fig_ure, use_container_width=True)
            else:
                st.write("Please select both parameters to plot the scatter plot.")

        # Displaying Plots
        st.plotly_chart(fig_1, use_container_width=True)
        st.write("The data is aggregated at the district level. Please select a district or state to view the data.")
        st.plotly_chart(fig_2, use_container_width=True)
        st.plotly_chart(fig_3, use_container_width=True)
        st.plotly_chart(fig4, use_container_width=True)
        st.plotly_chart(fig5, use_container_width=True)
        st.plotly_chart(fig6, use_container_width=True)