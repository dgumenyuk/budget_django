import subprocess


#subprocess.run("git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
#subprocess.run("git bisect run python manage.py test")
#subprocess.run("git bisect reset")

subprocess.run("git bisect start")
subprocess.run("git bisect bad HEAD")
subprocess.run("git bisect good e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
subprocess.run("git bisect reset")