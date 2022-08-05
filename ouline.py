#import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json
import re

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'

    # Complete the missing part of this function here
    response = requests.get(url)
    print(response.status_code) # Print status code
    soup = BeautifulSoup(response.content, 'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    array = []
    for job in JobDetails:
       jobTitle = job.find('h2', class_='card__job-title').text.strip()
       company = job.find('div', class_='card__job-empname-label').text.strip()
       description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
       jobDetailsjson = {
           "Title": jobTitle,
           "Company": company,
           "Description": description
       }
       # Add jobDetailsjson to that array
       array.append(jobDetailsjson)
    return array


#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search:")
    role = input()
    # Complete the missing part of this function here
    print("Enter location you want to search:")
    location = input()

    # Print the job search results
    results = getJobList(role, location)
    print(results)
    

if __name__ == '__main__':
    main()
