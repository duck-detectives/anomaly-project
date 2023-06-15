# Project Description

This project looks at the access logs of Codeup students across different cohorts to isolate anomalies in user access to certain parts of the Codeup curriculum. Our defined task is to answer five specific questions asked from a hypothetical stakeholder to prepare them for a meeting.

# Project Goals

To answer five of the following eight questions:

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?

# Data Dictionary

Column Name | Description | Key
--- | --- | --- 
date | Date that the path in the entry was accessed | datetime64
time | Time within date that the path in the entry was accessed | datetime64
path | Filepath within Codeup website that the user visited | string
user_id | Numeric ID of given user | int
cohort_id | Numeric ID of given cohort | int
ip | IP address of user | string
name | Name of cohort | string
start_date | Start date of cohort | datetime64
end_date | End date of cohort | datetime64
program_id | ID of program | 1 = Web Dev, 2 = Web Dev, 3 = Data Science

# Steps to Reproduce

Run through the notebook using your own credentials for acquiring the data from the Codeup SQL database.

# Initial Hypotheses

Web Development students will have more hits overall to filepaths than Data Science students.

Students overall access the curriculum more often during their tenure at Codeup than after their graduation.

# Project Planning 

# Acquire

- Acquire dataset from Codeup SQL database
- Save data as a local .csv file
- Initial data frame contains 847,330 rows and 15 columns

# Prepare

- Dropped columns not needed
    - id, slack, created at, updated at, deleted at
- Set index to date_time
    - dropped initial date and time columns after they were combined to date_time
- Updated dtypes for cohort_id (int), start/end dates (datetime64)
- Dropped rows containing ('/', 'toc', 'search/search_index.json')
    - These rows are landing pages and not lesson pages
- Dropped rows where program_id == 4 since there were only 4 entries and therefore not a full-fledged program yet.
- Dropped rows where name == 'Staff', since we are not interested in the frequency of staff visits to the curriculum.
- After prep, data frame has 690,916 rows and 8 columns

# Explore

- Addressed each of the 8 questions individually that was asked by our superior. Created visualizations where necessary.

# Conclusion

- Overall, Web Dev students hit the curriculum more often, and even had access to Data Science material. 
- Data Science cohorts, on the other hand, did not have access to Web Dev material.
- Web Dev students accessed the same material both during their cohort and after their graduation.
- Data Science students reviewed MySQL moreso after graduation than during their time at Codeup.
- At least speaking for Data Science students, the least accessed materials are those that are covered towards the end of the curriculum.

# Recommendations

- Get together with the Data Engineers in order to clean up the data and remove unnecessary information.
