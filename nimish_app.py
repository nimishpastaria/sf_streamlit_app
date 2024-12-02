import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import io
from datetime import datetime

# Setting up the title and introduction
st.title("My Story at Snowflake: Building a Case for a Permanent Role")

# Navigation sidebar
st.sidebar.title("Sections")
sections = [
    "Who is Nimish?",
    "Case Study: The Collections Initiatives",
    "Why I’m the Candidate for the Job",
    "Areas of Improvement and Action Plan",
    "The Value Plan",
    "Closing"
]
selected_section = st.sidebar.radio("Select a section to navigate:", sections)

# Section 1: Who is Nimish?
if selected_section == "Who is Nimish?":
    st.header("Who is Nimish?")
    st.markdown("""
    - Experienced professional with over **4 years of experience** in project management and cloud implementations. 
    - Currently pursuing Master’s in Business Analytics and Project Management at the University of Connecticut (UCONN).
    - Previously worked as an OTC senior consultant for **HighRadius Technologies**, designed and implemented OTC Cash Application and Credit Management solutions for enterprise customers.
    - Fast forward to now, has been driving the FY25 collections initiatives at Snowflake.
    - Primary KPI is to ensure the delivery of value for all the FY25 IT implementation related to Snowflake collections.
    """)
    st.markdown("### My Projects at a Glance:")
    projects = {
        "Demand": ["Collections Aging Dashboard", "HRC Enhancement - AWS MP", "Credit Card AdHoc Batch Run", "DMX in HRC Phase 1", "OD/InArrears Invoices in Draft", "AWS CashApp OD AdHoc Payments"],
        "Stage": ["Deployed", "Under UAT", "Under UAT", "Under Design", "Under POC", "Under Development"],
        "Status": ["Green", "Green", "Green", "Amber", "Amber", "Green"],
    }
    df = pd.DataFrame(projects)
    st.table(df)
    st.image("https://drive.google.com/file/d/1DjFQqd3dPq4wU7jOSHH1DBkwpZldHgTa/view?usp=sharing", caption="First Day", use_column_width=True)

    

# Section 2: Case Study: The Collections Initiatives
elif selected_section == "Case Study: The Collections Initiatives":
    st.header("Case Study: The Collections Initiatives")
    st.markdown("""
    ### Projects Summary:
    The collections initiatives holistically address revenue leakage and inefficiencies in manual collections on past due invoices.
    There area a total of 5 demands which aim to enhance visibility, reduce manual touchpoints, and streamline existing processes. 
    """)
    st.markdown("""
    ### Problem Statement:
    - Multiple projects rooted from Collections
    - All being looked at a micro level or as individual demands; no cohesion
    - Dependency on external vendors (Highradius and Stripe)
    - Inefficient co-ordination between different stakeholders (Business, Transformation Office, IT, Product, Marketplace Ops)
    - Various moving parts and many systems involved
    """)
    st.markdown("""
    ### The Solution:
    - Unified program management approach to consolidate all the projects and view under one umbrella
    - Strategic roadmap to prioritize and synchronize projects based on overarching business objectives
    - Leverage relationship with vendor and communicate proactively, including contingency
    - Cross-functional communication plan with defined RACI
    - Centralized project management (Cheatsheet) to streamline integration, tracking, and reporting across all teams and systems
    """)
    st.markdown("""
    ### Project Timelines: 
    """)
    st.image("path/to/your/image.png", caption="Timeline Overview", use_column_width=True)
    #             # Define the data for the Gantt chart
    # data = {
    #     "Project": [
    #         "Aging Dashboard",
    #         "Aging Dashboard",
    #         "Aging Dashboard",
    #         "HRC AWS MP Enhancements",
    #         "HRC AWS MP Enhancements",
    #         "HRC AWS MP Enhancements",
    #         "HRC AWS MP Enhancements",
    #         "HRC AWS MP Enhancements",
    #         "Credit Card Ad-hoc Batch Run",
    #         "Credit Card Ad-hoc Batch Run",
    #         "Credit Card Ad-hoc Batch Run",
    #         "DMX in HRC",
    #         "DMX in HRC",
    #         "DMX in HRC",
    #     ],
    #     "Phase": [
    #         "UAT",
    #         "Go-Live",
    #         "Hypercare",
    #         "HRC Design",
    #         "Development",
    #         "SIT / Data Prep",
    #         "UAT",
    #         "Hypercare",
    #         "Development",
    #         "SIT / Data Prep",
    #         "Go-Live",
    #         "SF and HRC Design",
    #         "Development",
    #         "SIT",
    #     ],
    #     "Start": [
    #         "2023-11-04", "2023-11-25", "2023-12-02",
    #         "2023-11-11", "2023-11-18", "2023-11-27", "2023-12-04", "2023-12-18",
    #         "2023-11-11", "2023-11-18", "2023-12-17",
    #         "2023-11-04", "2023-12-06", "2023-12-20",
    #     ],
    #     "Finish": [
    #         "2023-11-25", "2023-12-02", "2023-12-09",
    #         "2023-11-18", "2023-11-27", "2023-12-04", "2023-12-11", "2023-12-30",
    #         "2023-11-18", "2023-11-25", "2023-12-30",
    #         "2023-12-05", "2024-01-06", "2024-01-13",
    #     ],
    # }
    
    # # Create a DataFrame
    # df = pd.DataFrame(data)
    
    # # Convert Start and Finish columns to datetime
    # df["Start"] = pd.to_datetime(df["Start"])
    # df["Finish"] = pd.to_datetime(df["Finish"])
    
    # # Ensure project order as specified
    # project_order = [
    #     "DMX in HRC",
    #     "Credit Card Ad-hoc Batch Run",
    #     "HRC AWS MP Enhancements",
    #     "Aging Dashboard",
        
    # ]
    # df["Project"] = pd.Categorical(df["Project"], categories=project_order, ordered=True)
    
    # # Create the Gantt chart using Plotly
    # fig = px.timeline(
    #     df,
    #     x_start="Start",
    #     x_end="Finish",
    #     y="Project",
    #     color="Phase",
    #     title="Consolidate Timeline View",
    #     text="Phase",
    #     labels={"Phase": "Project Phase", "Project": "Projects"},
    #     template="plotly_white"
    # )
    
    # # Update layout and text alignment
    # fig.update_traces(
    #     marker=dict(line=dict(width=0.5, color="black")),
    #     textposition="auto"  # Align text in the center of the blocks
    # )
    # fig.update_layout(
    #     xaxis_title="Timeline",
    #     yaxis_title="Projects",
    #     showlegend=True,
    #     height=700,
    #     margin=dict(l=50, r=50, t=50, b=50),
    #     xaxis=dict(tickformat="%b %d"),
    #     title_x=0.5,
    # )
    
    # # Render the Gantt chart in Streamlit
    # st.plotly_chart(fig)

# Section 3: Why I’m the Candidate for the Job
elif selected_section == "Why I’m the Candidate for the Job":
    st.header("Why I’m the Candidate for the Job")
    st.markdown("""
    ### Unique Value Proposition and Proven Instances from Internship:
- Able to leverage **relationship with HRC** to expedite things on DMX in HRC
- Able to **analyse value** and was able to push back on a demand saving time and resources (On Demand/In Arrears Invoices in Draft)
- Able to **absorb tasks and projects** (Eg, Collections program, ServiceNow Maintenance) so that the team can spend the time on new things (Eg, FY26 planning, MCD, EDP etc)
- Helped offload responsibility of maintaing OTC portfolio project status updates and **monthly communication to business stakeholders**
- Executed projects with **minimal supervision and involvement**
- Identified people to be involved and **minimized the time to solution** (Eg, involved Bola in OD InArrears recon dashboard and leveraged another dashboard)
- Able to **introduce risk management practices** and mitigation steps. Eg, Impact assessment from Invoicer 2.0 and staggered rollout plan for specific customers
- Takes **full accountability** and does not not drop the ball
- **Not hesitant** to step outside of PMO duties. Eg, Visualized an end-to-end process flow diagram by gathering requirements from business (DMX in HRC), created UAT test scripts for CC AdHoc Batch Run, updated BRD occassionally
- Able to understand systems and scale quickly to **contribute to design** Eg, HRC interface setup and PGP encryption - able to contribute to the design of DMX in HRC
- Not hesitant to escalate and push when needed. Eg, Business to sign-off on the BRD (AWS OD AdHoc Pmts), IT resource constraints for AWS OD AdHoc Payments
- **Ready to roll** whenever required. Late night and early morning (6am) calls with India team
- Proactively looks out to increase and share knowledge. Eg, Enrolled for SnowPro to learn more about the basics of the product, helped shared information with other members of the PMO team
- **Challenges existing ways**. Eg, iterative testing approach on Aging Dashboard, staggered deployment for dashboard, separate SIT for AWS internal and external scope of work
- Built relationships with peope week on week and got faster responses to consolidate OTC/NPI deck data
- Created a CheatSheet for a consolidated view of all the collections demands
- Able to perform **value assessment** and **evaluate ROI** of the projects to justify the implementation
- Solved business problems. How?
- Got the business teams, Bola and BSAs together
- Received push back from integration team but made noise and was able to get responses and commits from them later
- Getting everyone on board and committed to delivering the project - shared resources
- Influenced stakeholders in key decisions thru value realization assessment (OD InArrears)
    """)
    st.markdown("### Before-and-After Impact:")
    impact_data = {
        "Metric": ["Project Execution Rate", "Team Efficiency", "Task Overlaps"],
        "Before Internship": [70, 60, 40],
        "After Internship": [90, 85, 10],
    }
    df = pd.DataFrame(impact_data)
    st.line_chart(df.set_index("Metric"))

# Section 4: Areas of Improvement and Action Plan
elif selected_section == "Areas of Improvement and Action Plan":
    st.header("Areas of Improvement and Action Plan")
    st.markdown("""
    ### Growth Opportunities:
    - Networking and visibility to leadership
    - Better communication and updates
    - Level Up on ownership and deliverables
    - Enhance technical knowledge of Snowflake's core platform
    - Increase NPI domain knowledge
    """)
    st.markdown("### Action Plan:")
    action_plan = {
        "Goal": ["Frequent Updates to Leaderhip", "Learn about end-to-end NPI deployments ", "Complete SnowPro Certification"],
        "Deadline": ["Every Month", "3 Months", "2 Weeks"],
        "Measure of Success": ["Recall Value", "Knowledge Tests", "Certification Achieved"],
    }
    df = pd.DataFrame(action_plan)
    st.table(df)

    st.markdown("### Readiness Checklist:")
    readiness = {
        "Skill": ["Stakeholder Management", "NPI Domain Knowledge", "Snowflake Fundamentals", "Hungry for more attitude"],
        "Confidence Level (1-10)": [9, 8, 9, 10],
    }
    # Generate the checklist
    for skill, confidence in zip(readiness["Skill"], readiness["Confidence Level (1-10)"]):
        st.checkbox(f"{skill} (Confidence Level: {confidence}/10)", value=False)

# Section 5: The Value Plan
elif selected_section == "The Value Plan":
    st.header("The Value Plan")
    st.markdown("""
    ### Proposed 6-Month Roadmap:
    1. Lead at least 2 high-priority NPI projects
    2. Drive measurable improvements for business teams (Eg, product features, new SKUs)
    3. Go-To person for anything NPI
    """)
    st.markdown("### Impact Caused by My Absence:")
    st.markdown("- Loss of momentum on key initiatives")
    st.markdown("- Decreased team efficiency due to lack of continuity and a holistic view.")
    st.markdown("- Increased workload, additional responsibilities for IT PMO team")
    st.markdown("- Increased workload, additional responsibilities for IT PMO team")

    st.markdown("### Roadmap Visualization:")
    roadmap_data = {
        "Phase": ["Onboarding", "Initial Projects", "Process Improvement", "Results Delivery"],
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

# Section 6: Closing
elif selected_section == "Closing":
    st.header("Closing")
    st.markdown("""
    ### Final Pitch:
    - I've demonstrated the ability to manage projects independently, have collaborated effectively across relevant teams, and planned delivery of prejects with measurable results.
    - With your support, I'm confident that I can continue driving value and lead NPI initiatives to success.
    """)
    st.markdown("#### Contact:")
    st.markdown("- Email: nimish.pastaria@snowflake.com")
    st.markdown("- LinkedIn: [Your LinkedIn Profile](#)")