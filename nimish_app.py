import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_timeline import timeline
import plotly.graph_objects as go
from datetime import datetime
import time
from streamlit_lottie import st_lottie
import requests

# Navigation sidebar
st.sidebar.title("Sections")
sections = [
    "👤 Who is Nimish??",
    " 📈 Case Study: The Collections Initiatives",
    " 💼 Why I’m the Candidate for the Job: Proven Instances",
    " 🚀 Areas of Improvement and Action Plan",
    " 📑 Future Plan",
    "Closing"
]
selected_section = st.sidebar.radio("Select a section to navigate:", sections)

# Section 1: 👤 Who is Nimish??
if selected_section == "👤 Who is Nimish??":
    
    # lottie_html = """
    # <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    # <dotlottie-player src="https://lottie.host/fff8746c-d9c6-45d4-8827-6d5cff59e86e/PgPPsmZmvy.lottie" 
    #                 background="transparent" 
    #                 speed="1" 
    #                 style="width: 300px; height: 300px" 
    #                 loop 
    #                 autoplay>
    # </dotlottie-player>
    # """

    # # Streamlit App
    # st.write("### Lottie Animation Embed")
    # st.components.v1.html(lottie_html, height=400)
    
    # Setting up the title and introduction
    st.title("✨ My Story at Snowflake: Building a Case for a Permanent Role")
    st.header("Who is Nimish??")
    st.markdown("""
    - Experienced professional with over **4 years of experience** in project management and cloud implementations. 
    - Currently pursuing Master’s in Business Analytics and Project Management at the University of Connecticut (UCONN).
    - Previously worked as an OTC consultant for **HighRadius Technologies**, designed and implemented Cash Application and Credit Management solutions for enterprise customers.
    - Fast forward to now, have been driving the FY25 collections IT initiatives at Snowflake.
    - Primary KPI is to ensure the delivery of value for all the FY25 IT implementation related to Snowflake collections.
    """)
    st.markdown("### Nimish's Responsibilities at a Glance:")
    projects = {
            "Item": ["Collections Aging Dashboard", "HRC Enhancement - AWS MP", "Credit Card AdHoc Batch Run", "DMX in HRC Phase 1", "OD/InArrears Invoices in Draft", "AWS CashApp OD AdHoc Payments", "OTC/NPI Monthly Updates", "ServiceNow Demand Updates"],
            "Project Stage": ["Staggered Deployment", "Under UAT", "Under UAT", "Under Design", "Under POC", "Under Development", "Ongoing", "Ongoing"],
            "Project Status": ["Green", "Green", "Green", "Amber -> Green", "Amber", "Green", "Ongoing", "Ongoing"],
            "Reponsibility": ["Project Manager", "Project Manager", "Project Manager", "Project Manager", "Project Manager", "Project Manager", "Owner", "Owner"],
        }
    df = pd.DataFrame(projects)
    st.table(df)


    st.image(
    "/home/vscode/sf_streamlit_app/Snowflake_Internship_Image.jpeg",
    caption="My First Day at the Dublin Office",
    use_container_width=True 
    )
    st.image(
    "/home/vscode/sf_streamlit_app/IMG_3154.JPG",
    caption="My First Day at UCONN",
    use_container_width=True 
    )
    
    # # Embed LinkedIn Badge
    # st.header("My LinkedIn Profile")
    # linkedin_badge_html = """
    # <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    # <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="nimish-pastaria" data-version="v1">
    #     <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/nimish-pastaria?trk=profile-badge">Nimish P.</a>
    # </div>
    # """
    # st.components.v1.html(linkedin_badge_html, height=310)
    
    # # Define the skills data
    # info = {
    #     "skills": [
    #         "Project Management", "Stakeholder Management", "SQL", "Problem Solving Mindset", 
    #     ]
    # }

    # # Number of columns in the skills grid
    # skill_col_size = 3

    # # Skills Section
    # st.subheader("Key Skills 🛠️ ")

    # def skill_tab():
    #     # Calculate the number of rows and columns needed for the grid
    #     rows, cols = len(info["skills"]) // skill_col_size, skill_col_size
    #     skills = iter(info["skills"])
    #     if len(info["skills"]) % skill_col_size != 0:
    #         rows += 1  # Add an extra row if the skills don't fit perfectly

    #     # Create the skill grid
    #     for x in range(rows):
    #         columns = st.columns(skill_col_size)
    #         for index_ in range(skill_col_size):
    #             try:
    #                 skill = next(skills)  # Get the next skill
    #                 columns[index_].button(skill)  # Create a button for the skill
    #             except StopIteration:
    #                 break  # Exit if there are no more skills

    # # Render the skills section
    # with st.spinner(text="Loading section..."):
    #     skill_tab()

    st.markdown("#### Contact:")
    st.markdown("- Email: nimish.pastaria@gmail.com")
    st.markdown("- Phone: +1 (413) 466-0810")
    st.markdown("- LinkedIn: https://www.linkedin.com/in/nimish-pastaria")

# Section 2:  📈 Case Study: The Collections Initiatives
elif selected_section == " 📈 Case Study: The Collections Initiatives":
    st.header(" 📈 Case Study: The Collections Initiatives")
    st.markdown("---")
    st.markdown("""
    ### 🔍 Projects Summary:
    The collections initiatives holistically address 
    revenue leakage and inefficiencies in manual collections on past due invoices.
    There area a total of 5 demands which aim to enhance visibility, reduce manual touchpoints, and streamline existing processes. 
    """)
    st.markdown("""
    ### 🚨 Problem Statement:
    - Multiple projects rooted from Collections
    - All being looked at a micro level or as individual demands; no cohesion
    - Dependency on external vendors (Highradius and Stripe)
    - Inefficient co-ordination between different stakeholders (Business, Transformation Office, IT, Product, Marketplace Ops)
    - Various moving parts and many systems involved
    """)
    st.markdown("""
    ### ✅ The Solution:
    - Centralized project management (Cheatsheet) to streamline integration, tracking, and reporting across all teams and systems
    - Unified program management approach to consolidate all the projects and view under one umbrella
    - Strategic roadmap to prioritize and synchronize projects based on overarching collections objectives
    - Leverage relationship with vendor and communicate proactively, including contingency
    - Cross-functional communication with defined RACI
    """)
    
    st.markdown("""
    ### Project Timelines: 
    """)
        # JSON data for the timeline
    # timeline_data = {
    #     "events": [
    #         {
    #             "start_date": {"year": "2024", "month": "11", "day": "4"},
    #             "end_date": {"year": "2024", "month": "11", "day": "25"},
    #             "text": {"headline": "Aging Dashboard", "text": "Development Completion and UAT"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "11", "day": "25"},
    #             "end_date": {"year": "2024", "month": "12", "day": "2"},
    #             "text": {"headline": "Aging Dashboard - Go-Live", "text": "Go-Live on 25th November"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "11", "day": "11"},
    #             "end_date": {"year": "2024", "month": "12", "day": "3"},
    #             "text": {"headline": "HRC AWS MP Enhancements", "text": "HRC Design and Development"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "12", "day": "4"},
    #             "end_date": {"year": "2024", "month": "12", "day": "18"},
    #             "text": {"headline": "HRC Enhancements - SIT & UAT", "text": "System Integration Testing and User Acceptance Testing"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "12", "day": "18"},
    #             "end_date": {"year": "2024", "month": "12", "day": "30"},
    #             "text": {"headline": "HRC Enhancements - Go-Live", "text": "Go-Live and Hypercare"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "11", "day": "11"},
    #             "end_date": {"year": "2024", "month": "12", "day": "17"},
    #             "text": {"headline": "Credit Card Ad-hoc Batch Run", "text": "Development and SIT"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "12", "day": "17"},
    #             "end_date": {"year": "2024", "month": "12", "day": "30"},
    #             "text": {"headline": "Credit Card Batch Run - Go-Live", "text": "Tentative Go-Live and Hypercare"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "11", "day": "4"},
    #             "end_date": {"year": "2024", "month": "12", "day": "5"},
    #             "text": {"headline": "DMX in HRC Phase 1", "text": "SF and HRC Design with SOW Sign-Off"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "12", "day": "6"},
    #             "end_date": {"year": "2024", "month": "1", "day": "20"},
    #             "text": {"headline": "DMX in HRC Development", "text": "Development and SIT for DMX"},
    #         },
    #         {
    #             "start_date": {"year": "2024", "month": "1", "day": "20"},
    #             "end_date": {"year": "2024", "month": "1", "day": "27"},
    #             "text": {"headline": "DMX in HRC - Go-Live", "text": "Tentative Go-Live and Hypercare"},
    #         },
    #     ]
    # }

    timeline_data = {
    "events": [
        # Aging Dashboard
        {
            "start_date": {"year": "2024", "month": "10", "day": "25"},
            "end_date": {"year": "2024", "month": "10", "day": "25"},
            "text": {"headline": "Aging Dashboard - Development Completion", "text": "Development Completion on 25th October."},
        },
        {
            "start_date": {"year": "2024", "month": "10", "day": "27"},
            "end_date": {"year": "2024", "month": "11", "day": "20"},
            "text": {"headline": "Aging Dashboard - UAT", "text": "User Acceptance Testing from 27th October to 20th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "25"},
            "end_date": {"year": "2024", "month": "11", "day": "25"},
            "text": {"headline": "Aging Dashboard - AR Executive/Marketing Dashboard Deployment", "text": "SiS Deployment for AR Executive and Marketing Dashboards on 25th November."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "13"},
            "end_date": {"year": "2024", "month": "12", "day": "13"},
            "text": {"headline": "Aging Dashboard - AR Collector Dashboard Deployment", "text": "SiS Deployment for AR Collector Dashboard on 13th December."},
        },

        # HRC Enhancements (AWS MP)
        {
            "start_date": {"year": "2024", "month": "10", "day": "8"},
            "end_date": {"year": "2024", "month": "10", "day": "25"},
            "text": {"headline": "HRC Enhancements - Snowbridge-WD SIT/UAT", "text": "SIT/UAT for Snowbridge-WD from 8th to 25th October."},
        },
        {
            "start_date": {"year": "2024", "month": "10", "day": "25"},
            "end_date": {"year": "2024", "month": "10", "day": "25"},
            "text": {"headline": "HRC Enhancements - Snowbridge-WD Deployment", "text": "Deployment completed on 25th October."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "15"},
            "end_date": {"year": "2024", "month": "11", "day": "15"},
            "text": {"headline": "HRC Enhancements - Design", "text": "Design completed on 15th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "15"},
            "end_date": {"year": "2024", "month": "11", "day": "26"},
            "text": {"headline": "HRC Enhancements - Development", "text": "Development phase from 15th to 26th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "27"},
            "end_date": {"year": "2024", "month": "12", "day": "3"},
            "text": {"headline": "HRC Enhancements - SIT", "text": "System Integration Testing from 27th November to 3rd December."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "4"},
            "end_date": {"year": "2024", "month": "12", "day": "11"},
            "text": {"headline": "HRC Enhancements - UAT", "text": "User Acceptance Testing from 4th to 11th December."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "11"},
            "end_date": {"year": "2024", "month": "12", "day": "17"},
            "text": {"headline": "HRC Enhancements - Cutover", "text": "Cutover activities from 11th to 17th December."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "18"},
            "end_date": {"year": "2024", "month": "12", "day": "18"},
            "text": {"headline": "HRC Enhancements - Go-Live", "text": "Go-Live completed on 18th December."},
        },

        # Credit Card Ad-Hoc Batch Run
        {
            "start_date": {"year": "2024", "month": "11", "day": "8"},
            "end_date": {"year": "2024", "month": "11", "day": "8"},
            "text": {"headline": "Credit Card Batch Run - Development Completion", "text": "Development completed on 8th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "11"},
            "end_date": {"year": "2024", "month": "11", "day": "18"},
            "text": {"headline": "Credit Card Batch Run - IT Testing", "text": "IT Testing in SBX environment from 11th to 18th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "18"},
            "end_date": {"year": "2024", "month": "11", "day": "19"},
            "text": {"headline": "Credit Card Batch Run - UAT Data Creation", "text": "UAT Data Creation from 18th to 19th November."},
        },
        {
            "start_date": {"year": "2024", "month": "11", "day": "25"},
            "end_date": {"year": "2024", "month": "12", "day": "11"},
            "text": {"headline": "Credit Card Batch Run - UAT", "text": "User Acceptance Testing from 25th November to 11th December."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "12"},
            "end_date": {"year": "2024", "month": "12", "day": "13"},
            "text": {"headline": "Credit Card Batch Run - Go-Live Alignment", "text": "Alignment activities from 12th to 13th December."},
        },
        {
            "start_date": {"year": "2024", "month": "12", "day": "17"},
            "end_date": {"year": "2024", "month": "12", "day": "17"},
            "text": {"headline": "Credit Card Batch Run - Go-Live", "text": "Tentative Go-Live on 17th December."},
        },

        # DMX in HRC
        {
            "start_date": {"year": "2024", "month": "12", "day": "18"},
            "end_date": {"year": "2025", "month": "1", "day": "22"},
            "text": {"headline": "DMX in HRC", "text": "Includes Design (1 week), Build (2 weeks), Testing (1 week), Cutover (1 week), and Hypercare (1 week)."},
        },
    ]
}


    # Render the timeline in the app
    timeline(timeline_data, height=800)

    # JSON data for the timeline
    timeline_data = {
        "events": [
            {"start_date": {"year": 2024, "month": 10, "day": 25},
            "end_date": {"year": 2024, "month": 10, "day": 25},
            "text": {"headline": "Aging Dashboard - Development Completion", "text": "Development Completion on 25th October."}},
            {"start_date": {"year": 2024, "month": 10, "day": 27},
            "end_date": {"year": 2024, "month": 11, "day": 20},
            "text": {"headline": "Aging Dashboard - UAT", "text": "User Acceptance Testing from 27th October to 20th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 25},
            "end_date": {"year": 2024, "month": 11, "day": 25},
            "text": {"headline": "Aging Dashboard - AR Executive/Marketing Dashboard Deployment", "text": "SiS Deployment for AR Executive and Marketing Dashboards on 25th November."}},
            {"start_date": {"year": 2024, "month": 12, "day": 13},
            "end_date": {"year": 2024, "month": 12, "day": 13},
            "text": {"headline": "Aging Dashboard - AR Collector Dashboard Deployment", "text": "SiS Deployment for AR Collector Dashboard on 13th December."}},
            {"start_date": {"year": 2024, "month": 10, "day": 8},
            "end_date": {"year": 2024, "month": 10, "day": 25},
            "text": {"headline": "HRC Enhancements - Snowbridge-WD SIT/UAT", "text": "SIT/UAT for Snowbridge-WD from 8th to 25th October."}},
            {"start_date": {"year": 2024, "month": 10, "day": 25},
            "end_date": {"year": 2024, "month": 10, "day": 25},
            "text": {"headline": "HRC Enhancements - Snowbridge-WD Deployment", "text": "Deployment completed on 25th October."}},
            {"start_date": {"year": 2024, "month": 11, "day": 15},
            "end_date": {"year": 2024, "month": 11, "day": 15},
            "text": {"headline": "HRC Enhancements - Design", "text": "Design completed on 15th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 15},
            "end_date": {"year": 2024, "month": 11, "day": 26},
            "text": {"headline": "HRC Enhancements - Development", "text": "Development phase from 15th to 26th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 27},
            "end_date": {"year": 2024, "month": 12, "day": 3},
            "text": {"headline": "HRC Enhancements - SIT", "text": "System Integration Testing from 27th November to 3rd December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 4},
            "end_date": {"year": 2024, "month": 12, "day": 11},
            "text": {"headline": "HRC Enhancements - UAT", "text": "User Acceptance Testing from 4th to 11th December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 11},
            "end_date": {"year": 2024, "month": 12, "day": 17},
            "text": {"headline": "HRC Enhancements - Cutover", "text": "Cutover activities from 11th to 17th December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 18},
            "end_date": {"year": 2024, "month": 12, "day": 18},
            "text": {"headline": "HRC Enhancements - Go-Live", "text": "Go-Live completed on 18th December."}},
            {"start_date": {"year": 2024, "month": 11, "day": 8},
            "end_date": {"year": 2024, "month": 11, "day": 8},
            "text": {"headline": "Credit Card Batch Run - Development Completion", "text": "Development completed on 8th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 11},
            "end_date": {"year": 2024, "month": 11, "day": 18},
            "text": {"headline": "Credit Card Batch Run - IT Testing", "text": "IT Testing in SBX environment from 11th to 18th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 18},
            "end_date": {"year": 2024, "month": 11, "day": 19},
            "text": {"headline": "Credit Card Batch Run - UAT Data Creation", "text": "UAT Data Creation from 18th to 19th November."}},
            {"start_date": {"year": 2024, "month": 11, "day": 25},
            "end_date": {"year": 2024, "month": 12, "day": 11},
            "text": {"headline": "Credit Card Batch Run - UAT", "text": "User Acceptance Testing from 25th November to 11th December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 12},
            "end_date": {"year": 2024, "month": 12, "day": 13},
            "text": {"headline": "Credit Card Batch Run - Go-Live Alignment", "text": "Alignment activities from 12th to 13th December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 17},
            "end_date": {"year": 2024, "month": 12, "day": 17},
            "text": {"headline": "Credit Card Batch Run - Go-Live", "text": "Tentative Go-Live on 17th December."}},
            {"start_date": {"year": 2024, "month": 12, "day": 18},
            "end_date": {"year": 2025, "month": 1, "day": 22},
            "text": {"headline": "DMX in HRC", "text": "Includes Design (1 week), Build (2 weeks), Testing (1 week), Cutover (1 week), and Hypercare (1 week)."}}
        ]
    }

    # Convert JSON to DataFrame
    rows = []
    for event in timeline_data["events"]:
        rows.append({
            "Task": event["text"]["headline"],
            "Description": event["text"]["text"],
            "Start": datetime(event["start_date"]["year"], event["start_date"]["month"], event["start_date"]["day"]),
            "End": datetime(event["end_date"]["year"], event["end_date"]["month"], event["end_date"]["day"]),
        })

    df = pd.DataFrame(rows)

    # Create a Gantt Chart using Plotly
    fig = px.timeline(
        df,
        x_start="Start",
        x_end="End",
        y="Task",
        color="Task",
        title="Project Timeline Gantt Chart",
        labels={"Task": "Projects"},
        hover_data=["Description"]
    )

    # Customize chart layout
    fig.update_layout(
        xaxis_title="Timeline",
        yaxis_title="Tasks",
        xaxis=dict(type="date"),
        height=800,
        title_x=0.5
    )

    # Display chart in Streamlit
    st.title("Project Timeline")
    st.plotly_chart(fig)
#===================
# Section 3:  💼 Why I’m the Candidate for the Job: Proven Instances
elif selected_section == " 💼 Why I’m the Candidate for the Job: Proven Instances":
    st.header(" 💼 Why I’m the Candidate for the Job: Proven Instances")
    # Add a horizontal line for separation
    st.markdown("---")
#     st.markdown("""
#     ### Unique Value Proposition and Proven Instances from Internship:
# - Able to leverage **relationship with HRC** to expedite things on DMX in HRC
# - Able to **analyse value** and was able to push back on a demand saving time and resources (On Demand/In Arrears Invoices in Draft)
# - Able to **absorb tasks and projects** (Eg, Collections program, ServiceNow Maintenance) so that the team can spend the time on new things (Eg, FY26 planning, MCD, EDP etc)
# - Helped offload responsibility of maintaing OTC portfolio project status updates and **monthly communication to business stakeholders**
# - Executed projects with **minimal supervision and involvement**
# - Identified people to be involved and **minimized the time to solution** (Eg, involved Bola in OD InArrears recon dashboard and leveraged another dashboard)
# - Able to **introduce risk management practices** and mitigation steps. Eg, Impact assessment from Invoicer 2.0 and staggered rollout plan for specific customers
# - Takes **full accountability** and does not not drop the ball
# - **Not hesitant** to step outside of PMO duties. Eg, Visualized an end-to-end process flow diagram by gathering requirements from business (DMX in HRC), created UAT test scripts for CC AdHoc Batch Run, updated BRD occassionally
# - Able to understand systems and scale quickly to **contribute to design** Eg, HRC interface setup and PGP encryption - able to contribute to the design of DMX in HRC
# - Not hesitant to escalate and push when needed. Eg, Business to sign-off on the BRD (AWS OD AdHoc Pmts), IT resource constraints for AWS OD AdHoc Payments
# - **Ready to roll** whenever required. Late night and early morning (6am) calls with India team
# - Proactively looks out to increase and share knowledge. Eg, Enrolled for SnowPro to learn more about the basics of the product, helped shared information with other members of the PMO team
# - **Challenges existing ways**. Eg, iterative testing approach on Aging Dashboard, staggered deployment for dashboard, separate SIT for AWS internal and external scope of work
# - Built relationships with peope week on week and got faster responses to consolidate OTC/NPI deck data
# - Created a CheatSheet for a consolidated view of all the collections demands
# - Able to perform **value assessment** and **evaluate ROI** of the projects to justify the implementation
# - Solved business problems. How?
# - Got the business teams, Bola and BSAs together
# - Received push back from integration team but made noise and was able to get responses and commits from them later
# - Getting everyone on board and committed to delivering the project - shared resources
# - Influenced stakeholders in key decisions thru value realization assessment (OD InArrears)
#     """)

    # Title for KPIs
    st.subheader(" ► Key Performance Indicators (KPIs)")

    # Create two columns for the KPIs content
    col1, col2 = st.columns(2)

    # KPIs: Left Column
    with col1:
        st.subheader("Collaboration and Stakeholder Management")
        st.markdown("""
        - **Leveraged relationship** with HRC to expedite deliverables on DMX in HRC
        - Not hesitant to **escalate** and push when needed. Examples:
            - Business sign-off on BRD (AWS OD AdHoc Pmts)
            - IT resource constraints for AWS OD AdHoc Payments
            - Received pushback from the integration team but **persisted** to get the responses and commitments.
        - Proactively identified and involved the right resources to **minimize the time** to solution (e.g., involved Bola in OD InArrears recon dashboard).
        - **Built relationships** week on week through coffee chats and got faster responses to consolidate OTC/NPI deck data.            
        - Helped **offload responsibility** for maintaining OTC portfolio project status updates and monthly communication to business stakeholders.
        """)

    # KPIs: Right Column
    with col2:
        st.subheader("Leadership and Execution")
        st.markdown("""
        - Executed projects with **minimal supervision** and involvement.
        - Taken **full accountability** and ensured project values are not lot in translation.
        - Able to **absorb tasks** and projects so the team can focus on strategic priorities (e.g., FY26 planning, EDP etc).
        - **Ready to roll** whenever required, including early morning and late-night calls (e.g., 6 am calls with the India team).
        """)

        st.subheader("Risk Management")
        st.markdown("""
        - Proactive **identified and mitigated risks**. Eg:
            - UAT Conflicts for AWS and CC Adhov Batch Run
            - Impact assessment for Invoicer 2.0
            - Staggered rollout plans for specific customers
        """)

        st.subheader("Process Improvement")
        st.markdown("""
        - Challenged existing ways:
            - Created a CheatSheet for a **consolidated view** of all collections demands.
            - Visualized an **end-to-end** process flow diagram (e.g., DMX in HRC).
        - **Iterative testing** approach on Aging Dashboard.
        - **Staggered deployment** for dashboards.
        - Separate SIT for AWS internal and external **scope of work**.
        """)

    # Add a horizontal line for separation
    st.markdown("---")

    # Title for OKRs
    st.header("🎯 Objectives and Key Results (OKRs)")

    # Create two columns for the OKRs content
    col3, col4 = st.columns(2)

    # OKRs: Left Column
    with col3:
        st.subheader("Strengthen Collaboration and Communication")
        st.markdown("""
        - Ensured timely updates for all OTC portfolio project statuses and monthly communications.
        - Established clear stakeholder alignment through weekly sync calls and bi-weekly status updates to minimize delays.
        - Improved response rates on project communication by actively engaging and building relationships with key stakeholders.
        """)

        st.subheader("Drive Value-Oriented Project Execution")
        st.markdown("""
        - Delivered projects independently with minimal supervision.
        - Influenced stakeholders through value realization assessments, such as evaluating cost savings or efficiency increases (e.g., OD InArrears).
        - Escalated critical decisions effectively to keep projects on track (e.g., business sign-off delays on BRD).
        """)

    # OKRs: Right Column
    with col4:
        st.subheader("Promote Process Optimization and Improvement")
        st.markdown("""
        - Created and refined process flow diagrams and UAT scripts (e.g., DMX in HRC, CC AdHoc Batch Run).
        - Applied non-standard approaches, such as parallel SIT and UAT, staggered rollouts, iterative testing, enhancment/continuous improvement bucketization.
        - Contributed to design and technical processes (e.g., HRC interface setup and PGP encryption for DMX).
        """)

        st.subheader("Build Product Knowledge")
        st.markdown("""
        - Enrolled for SnowPro certification to deepen product knowledge
        - Regularly read internal confluence pages and system flows to increase knowledge on different aspects
        """)
 #===========================
    # Data for before-and-after metrics
    impact_data = {
        "Metric": [
            "Time to Decision-Making",
            "Tasks Absorbed/Delegated",
            "Time to Solution Reduction",
            "Risk Mitigation Rate",
            "Stakeholder Alignment ",
            "Process Improvements",
        ],
        "Before": [65, 45, 50, 60, 65, 50],
        "After Onboarding": [85, 75, 85, 90, 90, 85],
    }

    # Convert to DataFrame
    df = pd.DataFrame(impact_data)

    # Create a grouped bar chart using Plotly
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df["Metric"],
        y=df["Before"],
        name="Before",
        marker_color="skyblue"
    ))

    fig.add_trace(go.Bar(
        x=df["Metric"],
        y=df["After Onboarding"],
        name="After Onboarding",
        marker_color="darkblue"
    ))

    # Customize layout
    fig.update_layout(
        title="Impact Analysis",
        xaxis_title="Metrics",
        yaxis_title="Percentage (%)",
        barmode="group",
        xaxis_tickangle=-45,
        height=600,
        legend=dict(title="Legend")
    )

    # Display the graph in Streamlit
    st.markdown("### Before-and-After Impact Metrics")
    # Display a progress bar with a label
    progress_bar = st.progress(0)  # Initialize the progress bar with 0%

    # Simulate progress updates
    for i in range(101):
        time.sleep(0.05)  # Simulate a task taking some time
        progress_bar.progress(i)  # Update the progress bar

    st.plotly_chart(fig)

    st.markdown("---")
    st.header("💥 Absence Impact")
    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Left Column: Delays and Alignment Issues
    with col1:
        st.subheader("Delays in Projects")
        st.markdown("""
        - Without my strong relationship with the vendor stakeholder, it might take longer to get their support.
        - Built relationship with integration and IT teams which helped speed up timelines and get things done faster. Building internal rapport with devs and BSAs could take time.
        - For collections specific projects involving HRC, HRC product knowledge would become a gap and dependency on external involvement would be increased. 
        """)

        st.subheader("Lack of Visbility and Alignment")
        st.markdown("""
        - Understanding the problems, scaling to foresee risks and aligning with stakeholders for future vision might take some time.
        - I ensured priorities were aligned across IT teams and reduced miscommunication.
        - Without this alignment, there’s a higher chance of missed deadlines where product is also involved or teams working on conflicting priorities.
        """)

        st.subheader("Extra Load on the Team")
        st.markdown("""
        - By taking ownership of collections projects, team's bandwidth was freed up.
        - In my absence, these initiatives where enhancements would also be coming would become an additional task, and might slow down the work and progress on other bigger projects.
        """)

    # Right Column: Process, Dependability, and Growth
    with col2:
        st.subheader("Impact to Process Improvements")
        st.markdown("""
        - Having a background in OTC, I was able to contribute very quickly (Eg, process flow diagrams and UAT scripts) and save time.
        - Without the domain knowledge, inefficiencies would arise when understanding the problem statement and the work becomes an additional task.
        """)

        # st.subheader("Dependability in Tough Times")
        # st.markdown("""
        # - I’ve consistently stepped up during emergencies, whether late-night or early-morning calls.
        # - Without me, some urgent situations might not be handled as quickly or effectively.
        # """)

        st.subheader("Missed Potential")
        st.markdown("""
        - In my absence, Snowflake would be losing a team member who genuinely enjoys working here and is motivated to contribute to continued success
        """)
#=========================

# Section 4:  🚀 Areas of Improvement and Action Plan
elif selected_section == " 🚀 Areas of Improvement and Action Plan":
    st.title("🔍 Areas of Improvement and Action Plan")
    # st.header(" 🚀 Areas of Improvement and Action Plan")
    # st.markdown("""
    # ### Growth Opportunities:
    # - Networking and visibility to leadership
    # - Better communication and updates
    # - Level Up on ownership and deliverables
    # - Enhance technical knowledge of Snowflake's core platform
    # - Increase NPI domain knowledge
    # """)

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Areas of Improvement: Left Column
    with col1:
        st.subheader("Balancing Politeness and Assertiveness")
        st.markdown("""
        - At times, my politeness is perceived as hesitancy, which may affect the driver or project execution.
        - **Improvement Plan**:
            - Consciously work on the balance between politeness and assertiveness while communicating.
            - Becoming a driver in team meetings by setting expectations and ensuring accountability.
        """)

        st.subheader("Driving Projects Instead of Being a Task Master")
        st.markdown("""
        - Shift of impression from being a task tracker to driving end-to-end projects.
        - **Improvement Plan**:
            - Developing a proactive mindset to identify potential risks and solutions early.
            - Regularly align with stakeholders to understand the bigger picture and ensure strategic alignment.
            - Focusing on outcomes rather than micromanaging individual tasks, delegating responsibility where possible.
        """)

    # Areas of Improvement: Right Column
    with col2:
        st.subheader("Hungry for More Attitude")
        st.markdown("""
        - Maintaining a strong drive to take on more responsibilities and expand areas of influence.
        - **Improvement Plan**:
            - Continuously seek out new opportunities and areas to solve problems for people.
            - Volunteering for cross-functional and miscellaneous projects that add value and gain exposure to different aspects of the business.
            - Regularly reflect on areas where value can be added, and communicate readiness to take on more.
        """)

        st.subheader("Networking and Building Relationships")
        st.markdown("""
        - Having limited visibility within IT and Enterprise Apps teams.
        - **Improvement Plan**:
            - Finding opportunities to collaborate with key members of the IT and Enterprise Apps teams to build rapport. Eg, within Sathiya's internal pod, or with Adi or with India team 
            - Actively participate in team discussions and presentations to increase visibility and recognition.
            - Showcasing achievements and learnings through hallway talks, or implicitly as part of slack channels or email communications.
        """)

    # Add a horizontal line for separation
    st.markdown("---")

    # Title for Action Plan
    st.header("🚀 Action Plan")

    # Define Action Plan data
    action_plan_data = {
        "Goal": [
            "Practice assertive communication in daily interactions",
            "Take ownership of at least one high-visibility project",
            "Begin a structured networking plan (bi-weekly 1:1s)",
            "Achieve SnowPro certification",
            "Volunteer for cross-functional projects",
        ],
        "Deadline": [
            "1 Month",
            "3 Months",
            "2 Weeks",
            "1 Week",
            "4 Months",
        ],
        "Measure of Success": [
            "Positive feedback from stakeholders",
            "Completion of project milestones",
            "Stronger relationships and faster responses",
            "Certification achieved",
            "Exposure to new business areas",
        ]
    }

    # Convert the data into a pandas DataFrame
    action_plan_df = pd.DataFrame(action_plan_data)

    # Display the Action Plan as a table
    st.dataframe(action_plan_df, use_container_width=True)

#=========================

# Section 5: Future Value Plan
elif selected_section == " 📑 Future Plan":
    st.header(" 📑 Future Plan")
    # st.markdown("""
    # ### Proposed 6-Month Roadmap:
    # 1. Lead at least 2 high-priority NPI projects
    # 2. Drive measurable improvements for business teams (Eg, product features, new SKUs)
    # 3. Go-To person for anything NPI
    # """)
    # Define custom CSS for the shadowed box in dark mode
    st.markdown(
        """
        <style>
        .shadow-container {
            background-color: #2b2b2b; /* Dark background */
            padding: 20px; /* Internal spacing */
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Stronger shadow for dark mode */
            margin-top: 20px; /* Spacing above the box */
            margin-bottom: 20px; /* Spacing below the box */
        }
        .shadow-container h3 {
            margin: 0 0 10px 0; /* Adjust spacing for the title */
            font-size: 18px; /* Adjust font size */
            color: #ffffff; /* Light text for contrast */
        }
        .shadow-container ul {
            margin: 0; /* Remove extra margin */
            padding-left: 20px; /* Proper indentation for bullet points */
            list-style: disc; /* Standard bullet points */
        }
        .shadow-container li {
            margin-bottom: 10px; /* Space between list items */
            font-size: 16px; /* Font size for list items */
            color: #dcdcdc; /* Slightly lighter text for readability */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Render the shadowed box with text
    st.markdown(
        """
        - i) Engage in at least 2 high-priority NPI projects within 2 quarters
        - ii) Drive measurable improvements for business teams (e.g., product features, new SKUs) within one quarter
        - iii) Go-To person for anything NPI within a year
    """
    )

    # st.markdown(
    #     """
    #     <div class="shadow-container">
    #         <h3> Proposed 6-Month Roadmap</h3>
    #         <ul>
    #             <li> Lead at least 2 high-priority NPI projects</li>
    #             <li> Drive measurable improvements for business teams (e.g., product features, new SKUs)</li>
    #             <li> Go-To person for anything NPI</li>
    #         </ul>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )
    st.markdown("### Roadmap:")
    roadmap_data = {
            "Phase": ["NPI Onboarding", "Initial Projects", "Process Improvement", "Results Delivery"],
            "Start Date": [
                datetime(2025, 4, 1),
                datetime(2025, 5, 1),
                datetime(2025, 7, 1),
                datetime(2025, 9, 1),
            ],
            "End Date": [
                datetime(2025, 4, 30),
                datetime(2025, 6, 30),
                datetime(2025, 8, 30),
                datetime(2025, 9, 30),
            ],
        }
    df = pd.DataFrame(roadmap_data)
    fig = px.timeline(
           df,
            x_start="Start Date",
            x_end="End Date",
            y="Phase",
            title="6-Month Roadmap",
            color="Phase",
    )   
    st.plotly_chart(fig)
    # st.markdown("### Impact Caused by My Absence:")
    # st.markdown("- Loss of momentum on key initiatives")
    # st.markdown("- Decreased team efficiency due to lack of continuity and a holistic view.")
    # st.markdown("- Increased workload, additional responsibilities for IT PMO team")
    # st.markdown("- Increased workload, additional responsibilities for IT PMO team")
    

# Section 6: Closing
elif selected_section == "Closing":
    st.header("Closing")
    st.markdown("""
    - I've demonstrated the ability to manage projects independently and planned the delivery of prejects with measurable results.
    - With your support, I'm confident that I can keep adding driving value and bring a collobarative spirit to the work.
    """)
    st.header("Thank You")
