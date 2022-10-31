'''
import subprocess


subprocess.run("git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
subprocess.run("git bisect run python manage.py test")
subprocess.run("git bisect reset")

#subprocess.run("pwd")
'''
import os

os.system("git bisect start")
os.system("git bisect bad c1a4be04b972b6c17db242fc37752ad517c29402")
os.system("git bisect good e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")