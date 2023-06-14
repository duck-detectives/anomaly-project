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
program_id | ID of program | 1 = , 2 = , 3 = Data Science, 4 = ?

# Steps to Reproduce

Run through the notebook using your own credentials for acquiring the data from the Codeup SQL database.

# Initial Hypotheses

# Project Planning 

# Acquire

- Acquire dataset from Codeup SQL database
- Save data as a local .csv file

# Prepare

- Remove duplicate columns (id)
- Remove unnecessary columns (created_at, updated_at, deleted_at)
- Remove confounding columns (slack)
- Concatenate date and time
- Convert date, time, start_date, and end_date to datatype datetime64
- Set datetime to index
- Convert cohort_id to datatype integer

# Explore

# Conclusion

# Recommendations

# Next Steps

