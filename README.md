# SmartIT-Flow

## Project Goals & Target Audience

Welcome to Smart IT flow. Smart IT Flow is an IT issue tracking system and is aimed at IT staff and administrators responsible for managing and resolving IT issues in a form of a ticketing system. The ticketing system will enhance communication and collaboration among team members, making it easier to work together and with end users. We will prioritise transparency and visibility, ensuring that stakeholders and management alike have a clear view of the status of IT issues. 

## Smart IT Flow Data Modelling & Planning 

<hr> 

### Issue Table 

This table will serve as the primary core of the system, and will contain all the information related to IT issues being tracked. 

 ![SmartITFlowDataModelling-Issue-Table](https://user-images.githubusercontent.com/114010857/229239351-97b6cb3b-87dd-4b24-b7f1-20df7999edb6.png)
 
The Issue_ID will serve as a unique identifier for each issue, while the Issue_Description field allows for a detailed description of the issue. The Priority_Level and Category fields will help to classify and prioritise issues. The Contact_Number field will be implemented to allow for easy communication with the end user who reported the issue. The Date_Created and Due_Date fields will help with scheduling and monitoring of issue resolution timelines. Added fields such as status will be an important aspect of the system as it will indicate the current stage of the issue resolution while Resolution_Time will help to measure efficiency and response time. By including Assigned_Technician it will allow for efficient assignment of issues to IT staff, while Resolution_Notes will allow for detailed tracking of issue resolution steps and outcomes.  
 
 <hr> 
 
 ### Technician Table 
 
This table will provide information about IT staff responsible for resolving issues. 
 
 ![SmartITFlowDataModelling-Technician-Table](https://user-images.githubusercontent.com/114010857/229239950-5089a9bd-e354-4dc4-aa7d-45f47118933f.png)
 
Technician_ID will serve as an unique identifier, while First_Name and Last_Name will provide basic identification information. The email and phone_number fields will allow for easy communication with the technician, while the Status field will indicate the Technician's availability or current workload.
 
 <hr>
 
 ### Category Table
 
 This table will allow for efficient categorization and organisation of IT issues. 

 ![SmartITFlowDataModelling-Category-Table](https://user-images.githubusercontent.com/114010857/229240230-91ec919b-75e6-48b2-89ad-526a50ba1d95.png)
 
 The Category_ID will serve as a unique identifier while Category_Name will provide a descriptive label for each category.
 
 <hr>
 
 ### Priority Table
 
 This table will allow for efficient prioritisation of IT issues.
 
 ![SmartITFlowDataModelling-Priority-Table](https://user-images.githubusercontent.com/114010857/229240558-3af337c8-22b1-4ff2-9867-4242947333eb.png)
 
 Priority_ID will serve as a unique identifier, while Priority_Name will provide a descriptive label for each priority level.
 
 <hr>
 
 ## Requirements
