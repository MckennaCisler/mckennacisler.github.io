#!/usr/bin/env python
# Script to print JSON Resume file in format easily copyable to online posting sites.
# This script was written with LinkedIn formatting in mind.
import json

FILENAME = "resume.json"
LIST_SEPERATOR = "\n - "

def print_resume(resume):
    print_work(resume["work"])
    print_projects(resume["projects"])

def print_header(name):
    print("\n\n================================================")
    print(name)
    print("================================================\n\n")

def print_work(work_list):
    print_header("Work")
    for work in work_list:
        print("Title: %s" % work["position"])
        print("Company: %s" % work["company"])
        print(get_date_str(work))

        bullets = get_list_str(work["highlights"])
        # TODO: clean URL
        print("Description:\n%s\n\n%s\n%s" % (bullets, work["website"], work["summary"]))
        print("\n")

def print_projects(projects):
    print_header("Projects")
    for project in projects:
        print("Project name: %s" % project["name"])
        print(get_date_str(project))
        print("Project URL: %s" % project["url"])

        bullets = get_list_str(project["highlights"])
        # TODO: clean URL
        print("Description:\n%s%s" % (project["description"], bullets))
        print("\n")

def get_list_str(list):
    return LIST_SEPERATOR + LIST_SEPERATOR.join(list)

def get_date_str(obj):
    return "Dates: %s -> %s" % (obj["startDate"], obj["endDate"] if hasattr(obj, "endDate") else "Present")

def main():
    with open(FILENAME, "r") as f:
        resume = json.load(f)
        print_resume(resume)

if __name__ == "__main__":
    main()
