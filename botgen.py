__author__ = "@ansanbinoy"

from core.main import banner
from core.main import colour
import os, sys, argparse
import requests
import shutil, time

os.system("clear")

class BotGen:
	def __init__(self):
		banner()
		parser = argparse.ArgumentParser()
		parser.add_argument("--genarate", dest = 'token',
				help="Your bot token.")
		self.args = parser.parse_args()
		if not self.args.token:
			sys.exit(parser.print_help())

		else:
			self.token = self.args.token
		self.requirements = """emoji
python-telegram-bot
"""
		self.check_token()
		self.build()

	def check_token(self):
		url = f"https://api.telegram.org/bot{self.token}/getUpdates"
		try:
			print (f"{colour('B')}[+] {colour('G')}Checking API token is valid or not.{colour('NON')}")
			time.sleep(0.5)
			x = requests.get(url)

		except Exception as e:
			sys.exit(f"{colour('B')}[!] {colour('R')}Something Wrong!.\n{colour('B')}[!] {colour('R')}Please check your internet connection!.{colour('NON')}")

		if str(x) != '<Response [200]>':
			sys.exit(f"{colour('B')}[!] {colour('R')}Please provide a valid API token!.{colour('NON')}")
		else:
			pass

	def mkdir(self):
		files = os.listdir()
		if 'Your_Bot' in files:
			shutil.rmtree('Your_Bot')
			os.mkdir('Your_Bot')
		else:
			os.mkdir('Your_Bot')

	def build(self):
		try:
			botsc = list()
			self.mkdir()
			print (f"{colour('B')}[+] {colour('G')}Generating Bot script.{colour('NON')}")
			time.sleep(1)
			with open('core/echobot.py') as bot:
				with open('Your_Bot/echobot.py',"w+") as botf:
					for i in bot:
						i = i.rstrip()
						botf.write(i + os.linesep)

			with open("core/credential.json") as crjs:
				with open('Your_Bot/credential.json',"w+") as crds:
					for i in crjs:
						i = i.rstrip()
						if "<token>" in i:
							crds.write(i.replace("<token>", self.token) + os.linesep)
						else:
							crds.write(i + os.linesep)

			with open("Your_Bot/requirements.txt",'w+') as req:
				req.write(self.requirements)
		except Exception as e:
			sys.exit(f"{colour('B')}[!] {e}!.{colour('NON')}")

		except:
			sys.exit(f"{colour('B')}[!] {colour('R')}Something went Wrong!.{colour('NON')}")

		else:
			time.sleep(1)
			print (f"{colour('B')}[+] {colour('G')}Your bot files are successfully saved on {colour('Y')}{os.getcwd()}{colour('NON')}")


if __name__ == '__main__':
	BotGen()
