import requests
import flask

app = flask.Flask(__name__)
mods = ["The_Mad_Punter", "kat-coder"]
famous = ["griffpatch", "Will_Wam", "ScratchCat", "ScratchTeam"]


#Main
@app.route('/')
def main():
    return """<head>
<title>Scratch Achievements</title>
<link rel=\"icon\" type=\"image/x-icon\" href=\"https://i.ibb.co/THfpyZz/costume4-12.png\">
<link rel= "stylesheet" type= "text/css" href= "/static/sheet.css">
</head>
<a href=\"/\"><img src=\"https://i.ibb.co/THfpyZz/costume4-12.png\" alt=\"costume2-6\" border=\"0\"></a><br />
<h1>Scratch Achievements</h1>
Welcome to Scratch Achievements!<br>
This is a place to find a list of things you've achieved on Scratch.
To look for a user, go to this website, but with url /user/[username here].<br>
Try mine: <a href=\"/user/The_Mad_Punter\">My Profile</a></h3><br><br><h3>User lookup:</h3>
<input type="text" id="text" />
<input type="button" id="btn" value="Search" onClick="javascript: window.open('/user/' + document.getElementById('text').value);" /><br>
Note: Slow to load some users.<br><br>
</a>


<h3>Featured Users:</h3>
<a href="/user/griffpatch"><img src="https://uploads.scratch.mit.edu/get_image/user/1882674_60x60.png"></a>
<a href="/user/Will_Wam"><img src="https://uploads.scratch.mit.edu/get_image/user/3051823_60x60.png"></a>
<a href="/user/ScratchCat"><img src="https://cdn2.scratch.mit.edu/get_image/user/15883188_60x60.png"></a>
<a href="/user/ScratchTeam"><img src="https://cdn2.scratch.mit.edu/get_image/user/119198_60x60.png"></a>
 <a href="/user/GentleX"><img src="https://cdn2.scratch.mit.edu/get_image/user/84082058_48x48.png"></a><br> 
<h5>Add to the list - contact The_Mad_Punter on Scratch!</h5>

"""


#User
@app.route('/user/<user>')
def user(user):
    global mods, famous
    achievements = 0
    finalText = """<head>
<title>Scratch Achievements</title>
<link rel=\"icon\" type=\"image/x-icon\" href=\"https://i.ibb.co/THfpyZz/costume4-12.png\">
<link rel= "stylesheet" type= "text/css" href= "/static/sheet.css">

</head>
"""
    finalText = finalText + f"<a href=\"/\">Back</a><a href=\"/\"><img src=\"https://i.ibb.co/THfpyZz/costume4-12.png\" alt=\"costume2-6\" border=\"0\"></a><br /><h1>Scratch User {user}</h1>"
    finalText = finalText + "<img src=\"" + requests.get(
        f"https://cors.9gr.repl.co/api.scratch.mit.edu/users/{user}/").json(
        )["profile"]["images"]["90x90"] + "\" width=90 height=90></img><br>"
    finalText = finalText + "<a href=\"https://scratch.mit.edu/users/" + user + "\">Scratch Profile</a><br><br>"
    user = user
    done = False
    offset = 0
    page = 1
    projects = []
    while done == False:
        with requests.get(
                f"https://cors.9gr.repl.co/api.scratch.mit.edu/users/{user}/projects?offset={offset}"
        ) as request:
            projects.extend(request.json())
            if (len(request.json()) != 20):
                done = True
            else:
                offset += 20
                page += 1
    print("Project count: " + str(len(projects)))
    finalText = finalText + "Project Count: " + str(len(projects)) + "<br>"

    ##    done = False
    ##    offset = 0
    ##    page = 1
    ##    followers = []
    ##    while done == False:
    ##        with requests.get(f"https://api.scratch.mit.edu/users/{user}/followers?offset={offset}") as request:
    ##            followers.extend(request.json())
    ##            if (len(request.json()) != 20):
    ##                done = True
    ##            elif offset > 10000:
    ##                done = True
    ##            else:
    ##                offset += 20
    ##                page += 1
    try:
        followers = requests.get(
            f"https://scratchdb.lefty.one/v3/user/info/{ user }").json(
            )["statistics"]["followers"]
        print("Follower count: " + str(followers))
    except:
        followers = 0
    try:
        following = requests.get(
            f"https://scratchdb.lefty.one/v3/user/info/{ user }").json(
            )["statistics"]["following"]
        print("Following count: " + str(following))
    except:
        following = 0
    try:
        posts = requests.get(
            f"https://scratchdb.lefty.one/v2/forum/user/info/{user}").json(
            )["counts"]["total"]["count"]
        finalText = finalText + "Posts: " + str(posts) + "<br>"
    except:
        posts = 0
    try:
        atPosts = requests.get(
            f"https://scratchdb.lefty.one/v2/forum/user/info/{user}").json(
            )["counts"]["Advanced Topics"]["count"]
        finalText = finalText + "AT Posts: " + str(atPosts) + "<br>"
    except:
        atPosts = 0
    print()
    finalText = finalText + "Following Count: " + str(following) + "<br>"
    finalText = finalText + "Follower Count: " + str(
        followers) + "<br><h3>Achievements</h3> "

    #Here are the achievements...
    if followers > 0:
        finalText = finalText + "1 Follower<br>"
        achievements += 1
    if followers > 9:
        finalText = finalText + "10 Followers<br>"
        achievements += 1

    if followers > 19:
        finalText = finalText + "20 Followers<br>"
        achievements += 1
    if followers > 49:
        finalText = finalText + "50 Followers<br>"
        achievements += 1
    if followers > 99:
        finalText = finalText + "100 Followers<br>"
        achievements += 1
    if followers > 199:
        finalText = finalText + "200 Followers<br>"
        achievements += 1
    if followers > 499:
        finalText = finalText + "500 Followers<br>"
        achievements += 1
    if followers > 999:
        finalText = finalText + "1000 Followers<br>"
        achievements += 1
    if followers > 1999:
        finalText = finalText + "2000 Followers<br>"
        achievements += 1
    if followers > 4999:
        finalText = finalText + "5000 Followers<br>"
        achievements += 1
    if followers > 9999:
        finalText = finalText + "10000 Followers<br>"
        achievements += 1
    if followers > 19999:
        finalText = finalText + "20000 Followers<br>"
        achievements += 1
    if followers > 59999:
        finalText = finalText + "50000 Followers<br>"
        achievements += 1
    if followers > 99999:
        finalText = finalText + "100000 Followers<br>"
        achievements += 1
    if followers > 999999:
        finalText = finalText + "1 Million Followers<br>"
        achievements += 1
    if len(projects) > 0:
        finalText = finalText + "1 Project<br>"
        achievements += 1
    if len(projects) > 9:
        finalText = finalText + "10 Projects<br>"
        achievements += 1
    if len(projects) > 19:
        finalText = finalText + "20 Projects<br>"
        achievements += 1
    if len(projects) > 49:
        finalText = finalText + "50 Projects<br>"
        achievements += 1
    if len(projects) > 99:
        finalText = finalText + "100 Projects<br>"
        achievements += 1
    if len(projects) > 199:
        finalText = finalText + "200 Projects<br>"
        achievements += 1
    if len(projects) > 499:
        finalText = finalText + "500 Projects<br>"
        achievements += 1
    if posts > 0:
        finalText = finalText + "1 Forum Post<br>"
        achievements += 1
    if posts > 4:
        finalText = finalText + "5 Forum Posts<br>"
        achievements += 1
    if posts > 9:
        finalText = finalText + "10 Forum Posts<br>"
        achievements += 1
    if posts > 19:
        finalText = finalText + "20 Forum Posts<br>"
        achievements += 1
    if posts > 49:
        finalText = finalText + "50 Forum Posts<br>"
        achievements += 1
    if posts > 99:
        finalText = finalText + "100 Forum Posts<br>"
        achievements += 1
    if posts > 499:
        finalText = finalText + "500 Forum Posts<br>"
        achievements += 1
    if posts > 999:
        finalText = finalText + "1000 Forum Posts<br>"
        achievements += 1
    if posts > 1999:
        finalText = finalText + "2000 Forum Posts<br>"
        achievements += 1
    if posts > 4999:
        finalText = finalText + "5000 Forum Posts<br>"
        achievements += 1
    if posts > 9999:
        finalText = finalText + "10000 Forum Posts<br>"
        achievements += 1
    if following > 0:
        finalText = finalText + "Following 1 Person<br>"
        achievements += 1
    if following > 9:
        finalText = finalText + "Following 10 People<br>"
        achievements += 1
    if following > 19:
        finalText = finalText + "Following 20 People<br>"
        achievements += 1
    if following > 49:
        finalText = finalText + "Following 50 People<br>"
        achievements += 1
    if following > 99:
        finalText = finalText + "Following 100 People<br>"
        achievements += 1
    if following > 499:
        finalText = finalText + "Following 500 People<br>"
        achievements += 1
    finalText = finalText + "<h3>Special Achievements</h3>"
    if atPosts > 0:
        finalText = finalText + "Not So Advanced<br>"
        achievements += 1
    if atPosts > 49:
        finalText = finalText + "AT-er<br>"
        achievements += 1
    if atPosts > 99:
        finalText = finalText + "Really Advanced<br>"
        achievements += 1
    if atPosts > 999:
        finalText = finalText + "AT Forum Helper<br>"
        achievements += 1
    if user in mods:
        finalText = finalText + "Scratch Achievements Mod<br>"

    if user == "The_Mad_Punter":
        finalText = finalText + "Scratch Achievements Creator<br>"

    if user in famous:
        finalText = finalText + "Featured Scratcher :)<br>"

    print(str(achievements))
    finalText = finalText + '<br><br><br><img src="https://i.ibb.co/7K3cjG0/costume6-3.png" alt="costume6-3" border="0">'
    if achievements > 4:
        finalText = finalText + '<img src="https://i.ibb.co/pLq9P4T/costume7-10.png" alt="costume7-10" border="0">'
    if achievements > 9:
        finalText = finalText + '<img src="https://i.ibb.co/s3vHm8Q/costume8-2.png" alt="costume8-2" border="0">'
    if achievements > 24:
        finalText = finalText + '<img src="https://i.ibb.co/RH71CX1/costume9-5.png" alt="costume9-5" border="0">'

    return finalText


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return """<head>
<title>404 Error</title>
<link rel=\"icon\" type=\"image/x-icon\" href=\"https://i.ibb.co/THfpyZz/costume4-12.png"></a>
<link rel= "stylesheet" type= "text/css" href= "/static/sheet.css">
</head>
<a href=\"/\"><img src=\"https://i.ibb.co/THfpyZz/costume4-12.png\" alt=\"costume2-6\" border=\"0\"></a><br />
<h1>404 Error</h1>
<h3>This is not the page you are looking for. <a href="/">Go Home</a></h3>
""", 404


@app.errorhandler(500)
def server_error(e):
    # note that we set the 500 status explicitly
    return """<head>
<title>500 Error</title>
<link rel=\"icon\" type=\"image/x-icon\" href=\"https://i.ibb.co/THfpyZz/costume4-12.png"></a>
<link rel= "stylesheet" type= "text/css" href= "/static/sheet.css">
</head>
<a href=\"/\"><img src=\"https://i.ibb.co/THfpyZz/costume4-12.png\" alt=\"costume2-6\" border=\"0\"></a><br />
<h1>500 Error</h1>
<h3>Either the code in the server is buggy here, or you are going to a nonexistent Scratcher's achievements page. <a href="/">Go Home</a></h3>
""", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
