# ResuME
ResuME Pitch

  Introducing the ultimate job search solution - our website! Looking for a job can be a daunting and time-consuming task, but we're here to make it easier for you. Our website is designed to simplify the job search process, so you can find the right job for you with just a few clicks.

  Gone are the days of sifting through endless job postings on LinkedIn and other websites. With our interactive, easy-to-use platform, you can simply drag and drop your resume and find job listings that are actually relevant to you. Our goal is to make the job search process as stress-free as possible, so you can focus on finding your dream job.

  What sets us apart from other job search websites is our personalized approach. By the end of this semester, we aim to have our project to the point where users can enter their resume and see personalized results in real time. This means that you'll no longer have to spend hours searching for jobs that may not even be a good fit for you. Instead, our website will do the heavy lifting for you, presenting you with job opportunities that match your skills and experience.

  So, if you're tired of endlessly scrolling through job postings with no luck, give our website a try. We're confident that our personalized approach and easy-to-use platform will help you find the job you've been searching for.

Description
Drag and drop resumes
	This program is going to have a pretty simple user interface that allows you to attach a 
	text document (and other versions such as pdf down the line) and submit it
Create database as we collect resumes
The submitted resumes will then be filtered into our database that will use an ML that will eventually group them together by keywords that apply to similar jobs.

Finds jobs that match keywords in your resume
We will implement a web scraper with BeatifulSoup that goes through job boards and looks for the keywords that it pulls from your resume and matches it to jobs that you would be a good fit for. This way, jobs that you could apply for will be much more accessible as you wouldn’t have to just type in something like “Software Engineering job” and filter through a plethora of results that might not be relevant to your previous experience. 


Stack
  Frontend
    React.js
    Flask
    CSS
    HTML
  Backend
    Python (boto3)
    AWS Personalize API
  Deployment
    Flat file storage (AWS S3 Bucket)
    AWS Personalize


Organization
  All code will be maintained in a GitHub repository

Rough Timeline
  Late January
    Have stack set up with basic front end
    Mid February
    Have basic functionality set up
    Drag and drop feature
    Progress on backend
    Progress on UI
  End of March
    Have text parsing functioning
    Improved UI/UX
    Minimized bugs
    Backend capable of generating searches
  End of April
    Cleaned up front end and back end
    Capable of finding links quickly
    Completed backend that parses resumes effectively and continuously updates database
  Early May
    Finalized website
    Presentation writeup and rehearsal
    Stress test and final debugging

