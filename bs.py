from bs4 import BeautifulSoup

html = """
<!Doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Beautiful Zoup</title>
</head>
<body>
<div id="first">
    <h3> data-examples="yes">hi</h3>
    <p>more text . </p>
</div>
    <ol>
        <li class="special"> This list item is special.</li>
        <li class="special"> This list item is special.</li>
        <li class="special"> This list item is special.</li>
    </ol>
    <div>bye</div>
</body>
</html>

"""

soup = BeautifulSoup(html, "html.parser")
data = soup.body.contents[1].next_sibling

print(data)