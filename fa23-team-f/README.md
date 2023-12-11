# Police Overtime - Team F
## About the Project

The Boston Police Department has a budget of over $400 million dollars, so this project is an analysis of how this money is spent. Namely, our analysis is centered around overtime spending and the relationship between total time worked and overtime hours. However, overtime pay is just one category of BPD spending. We have analyzed the earnings, overtime,  operating budget, field activity, and crime datasets to determine how money is used within the Boston Police Department. Additionally, to further analyze these trends we looked at datasets for race and demographics, police watchlists, complaints, and discipline. All of these datasets can be found under the data folder in the repository. 

We focused on answering three main questions: Identifying financial excess in BPD Spending, Characterizing Wasteful Overtime Practices, and Filling in Narratives around waste and Misconduct by Individual Police Officers. Through our analysis of these questions, we decided on an extension question that focuses on the relationship between the Boston Police Department's spending and Community safety. 

## Datasets

#### Crime Incident 
The Crime Incident data was not provided to us and was found on The City of Boston's website. We found this dataset useful when answering our Extension Question. In order to use this we had to convert the location (latitude, longitude) to a zipcode format. 

#### Demographic 
This dataset was provided to us, however, it contains limited information about the demographics of the BPD, split by rank into the intersections of race and gender. While there are entries for several years spanning back, until 2022, the sets provided are only screenshots that we can’t make models of, so we are limited to using 2022 and 2023 demographic data. Despite this, we used this data to help give us insights as we analyzed trends in other datasets while answering the key questions.

#### Earnings 
This data was provided to us and contained information about the Boston City Employees' Earnings which was used to help answer our first question. The datasets ranged from 2011-2022, and we analyzed trends in different periods of time: all of the data (2011-2022), the last decade (2012-2022), and recent years (2021-2022).
The datasets contain pay information for each employee, broken up into injury, overtime, regular, retro, Quinn, and detail pay. Additionally, the total pay for each employee is provided as well as their job title and department. To focus on the pay of the Boston Police Department we had to filter this data to only contain their employees. Additionally, we had to process the columns relating to pay to be floating point numbers so we could perform computations on the data. 

#### Field Activity 
This dataset was provided to us and contains detailed information about specific cases of arrests/scenes, both for the suspect in question and the officer who responded. Along with the location of arrest and supervising officer. We used this data to help answer our extension question. To preprocess the data set we had to account for the ways that the format of the tables changed. Between the first data from 2012 and now there have been 4 different schemas that had a variety of table names along with data. We also had to clean the data of any NaN values as well as incorrect datatypes.  

#### Operating Budget 
This dataset was not provided to us and was found on the Boston.gov website. It provides information about the proposed budget for 2024 and the budgets for 2021-2023. This dataset can help us analyze how the budget has changed over time. We first had to replace any missing values with NaN. Additionally, the expense columns had to be formatted to floating point numbers so we could perform computations. Lastly, to look at the budget for the Boston Police Department, we filtered out other departments and only looked at the data relating to the BPD.  

#### Overtime 
Within the Overtime folder you will find both court overtime data as well as Overtime pay data. The Court Overtime data  has annual records of officers requesting overtime pay when they appear in court. We have analyzed the number of records for each year to get a better understanding of overtime court appearance for the last decade. This data has STARTTIME and ENDTIME which could be used to calculate hours worked by officers.
The overtime pay dataset ranges from 2012 to 2022. It provides records of officers requesting overtime pay and the address where the overtime took place. We have analyzed the number of records for each year to get a better understanding of overtime for the last decade and the discrepancy between ‘Hours Worked’ and ‘Hours Paid’. 

#### Watchlists and Complaints
These datasets were not provided to us but required to answer the third question. They provided information about officers who are on the Suffolk County Watchlist, been disciplined for overtime abuse or misconduct, or have complaint records. To use these datasets we had to convert the format of the officer name in each dataset into the same format and remove duplicate values for complaints and salaries. Also calculating the number of years which an officer collected overtime during. 


## Getting Started

Our code can be found under the Notebooks folder which contains 9 notebooks we used for our analysis. In order to run these please make sure you have the following libraries installed:
 - Matplotlib
 - Pandas
 - USZipcode
 - Time
 - Numpy
 - CSV
 - Sklearn
 - Matplotlib_venn

To answer the first question of identifying financial excess we utilized the three Earnings Data notebooks as well as the Operating Budget Notebook. Our analysis for the second question relating to wasteful overtime spending can be found in the Overtime Notebook. The analysis for filling in narratives around waste and misconduct by individual police officers can be found in the Incidents and Complaints Notebook as well as the Watchlists Complaints and Overtime Notebook. Our extension analysis is all located in the Extension Question notebook. Additional analysis of field and demographic data can be found in the Field and Demographic Data notebook. 



