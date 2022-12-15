from flask import Flask, render_template, request, redirect, send_file
from extractor.Jobp import extractor_plannet
from job import save_to_file
app= Flask("J_P")
db={}
@app.route("/")
def Home():
    return render_template('pl_home.html')

@app.route("/pl_search")
def Search():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect ('/')
    if keyword in db:
      pls=db[keyword]
    else:
        pls = extractor_plannet(keyword)
        db[keyword]=pls
    return render_template('pl_search.html', keyword = keyword, pls=pls)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
      return redirect("/")
    if keyword not in db:
      return redirect(f"/pl_search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv",mimetype='text/csv',as_attachment=True)

app.run('127.0.0.1')