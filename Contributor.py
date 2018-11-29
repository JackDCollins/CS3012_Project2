import requests



def doContributors(g,c,repo) :

    middle = ""
    for user in repo.get_contributors():
        print(dir(user.bio))
        #User Image
        img_data = requests.get(user.avatar_url).content
        with open('imgs/'+user.login + '.jpg', 'wb') as handler:
            handler.write(img_data)

        middle += """

            <img src="imgs/""" + user.login + """.jpg" style="width:250px;height:250px;"> </img>
            <br>
            <a href="https://github.com/""" + user.login + """" class="h2">""" + user.login + """<h2>
            <br>
            """






    top= """ <!DOCTYPE html>
    <html>
       <head>
         <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">


         <style>
         #header {
             background-color:#4F7CAC;
             color:white;
             text-align:center;
             padding:5px;
         }
         #nav {
             line-height:30px;
             background-color:#eeeeee;
             height:1750px;
             width:175px;
             float:left;
             padding:5px;
         }
         #section {
             width:1000;
             text-align:center;
             padding:10px;
         }
         #footer {
             background-color:#4F7CAC;
             color:white;
             clear:both;
             text-align:center;
             padding:5px;
         }
            body {
            font-family: 'Open Sans', sans-serif;
            }
             .bar {
                fill: #4F7CAC;
             }
             .label {
             font-size: 20px;
             fill: #000;
             }

             .highlight {
                fill: #3C474B;
             }

             .val {
               font-size: 20px;
               fill: #000;
             }

             .title {
                fill: black;
                font-size: 40px
                text-align: center
             }
          </style>
          <script src = "https://d3js.org/d3.v4.min.js"></script>
          <title> Animated bar chart </title>
       </head>

       <body>
         <div id="header">
            <h1>GIT Repositry Analysis</h1>
        </div>
        <div id="nav">
      <a href="index.html">Homepage<a>
        <br>
      <a href="page2.html">Commits<a>
        <br>
      <a href="page3.html">Code Chrun/Lines of Code<a>
        <br>
      <a href="Contributors.html">Contributors<a>
      </div>
      <div id="section">
        """


    bottom = """
    <div>

        </div>
        <div id="footer">

          Jack Donal Collins
    </div>
       </body>
    </html>"""

    Html_file= open("Contributors.html","w")
    Html_file.write(top + middle + bottom)
    Html_file.close()
