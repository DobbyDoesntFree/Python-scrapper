from flask import Flask, render_template, request,redirect, send_file
from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.file import save_to_file

# request

app = Flask("JobScrapper")

#use folder name templates literally for Flask understand path to rendering
#templates folder's path must be same with this folder level of this file exsists
#set router. @ decorator only impact right below of the line

c_db = {}

@app.route("/") 
def home():
    print(request.args)
    return  render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword") # "keyword" is name of html form
    if keyword == None:
        return redirect("/")
    if keyword in c_db:
        jobs = c_db[keyword]
    else:
        indeed = extract_wwr_jobs(keyword)
        wwr = extract_indeed_jobs(keyword)
        jobs = indeed + wwr # use {% PYTHON_CODE %}
        c_db[keyword] = jobs # save to dict array
    return  render_template("search.html", keyword=keyword, jobs=jobs) #use "{{##}}"  for use variable

@app.route("/export")
def export():
    keyword = request.args.get("keyword") # "keyword" is name of html form
    if keyword == None:
        return redirect("/")
    if keyword not in c_db:
        return redirect(f"/search?keword={keyword}") # if key value dosen't exists in db, generate automatically
    save_to_file(keyword, c_db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run(port=5002)
