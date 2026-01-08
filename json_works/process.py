from json import load
file_path="json_works\\students.json"
fr=open(file_path,"r",encoding="utf-8")
data=load(fr)
for st in data:
    pass#print(st.get("name"))

course_dj=[n.get("name") for n in data if n.get("course")=="django"]
print(course_dj)