from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
        return super().do_GET()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Personal Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        nav {
            display: flex;
            justify-content: center;
            background-color: #333;
        }

        nav a {
            color: white;
            text-decoration: none;
            padding: 0.75rem 1.5rem;
        }

        nav a:hover {
            background-color: #575757;
        }

        main {
            padding: 2rem;
            text-align: center;
        }

        section {
            margin: 2rem 0;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        .container {
            max-width: 800px;
            margin: auto;
        }

        img {
            max-width: 100%;
            height: auto;
            border-radius: 50%;
        }
    </style>
</head>

<body>
    <header>
        <h1>Welcome to My Personal Website</h1>
        <p>A place to share who I am and what I do</p>
    </header>

    <nav>
        <a href=\"#about\">About Me</a>
        <a href=\"#portfolio\">Portfolio</a>
        <a href=\"#contact\">Contact</a>
    </nav>

    <main>
        <div class=\"container\">
            <section id=\"about\">
                <h2>About Me</h2>
                <img src=\"profile.jpg\" alt=\"My Photo\">
                <p>Hi! I'm [Your Name], a [Your Profession]. I love [your hobbies/interests]. This website showcases some of my work and allows you to get in touch with me.</p>
            </section>

            <section id=\"portfolio\">
                <h2>Portfolio</h2>
                <p>Here are some projects I've worked on:</p>
                <ul>
                    <li><a href=\"#\">Project 1</a> - Description</li>
                    <li><a href=\"#\">Project 2</a> - Description</li>
                    <li><a href=\"#\">Project 3</a> - Description</li>
                </ul>
            </section>

            <section id=\"contact\">
                <h2>Contact</h2>
                <p>If you'd like to get in touch, feel free to reach out:</p>
                <ul>
                    <li>Email: <a href=\"mailto:yourname@example.com\">yourname@example.com</a></li>
                    <li>LinkedIn: <a href=\"#\">Your LinkedIn Profile</a></li>
                    <li>GitHub: <a href=\"#\">Your GitHub Profile</a></li>
                </ul>
            </section>
        </div>
    </main>

    <footer>
        <p>&copy; 2025 [Your Name]. All rights reserved.</p>
    </footer>
</body>

</html>
"""

# Write the HTML content to an index.html file
with open("index.html", "w") as file:
    file.write(HTML_CONTENT)

# Start the HTTP server
if __name__ == "__main__":
    with HTTPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
