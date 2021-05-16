from bs4 import BeautifulSoup
import requests
import lxml     #parser
import time

print('Write some skill which you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index, job in enumerate(jobs):      #enum allows to iterate over the index of the jobs list
        published_date = job.find('span', class_='sim-posted').span.text
        # print(published_date)
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        # print(company_name)
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        # print(skills)
        more_info = job.header.h2.a['href']

        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()} \n")
                f.write(f"Required Skills: {skills.strip()} \n")
                f.write(f"Published Date: {published_date} \n")
                f.write(f"More Info: {more_info}")
            print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)