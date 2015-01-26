from threading import Thread
from wave import open as waveOpen
from audioop import add
from subprocess import Popen, PIPE

try:
	from subprocess import DEVNULL
except ImportError: #Python 2.7
	DEVNULL = open("/dev/null")

class Music(Thread):
	def __init__(self, what, soundout):
		self.what = what
		Thread.__init__(self)
		if self.what == "None":
			return
		self.scheduled = None
		if soundout == "pulse":
			self.soundout = Popen(["pacat", "--latency-msec=1000", "--client=LokoPizza"], stdin=PIPE, stdout=DEVNULL, stderr=DEVNULL)
		elif soundout == "alsa":
			self.soundout = Popen(["aplay", "-t", "wav", "-f", "cd", "-"], stdin=PIPE, stdout=DEVNULL, stderr=DEVNULL)
	
	def run(self):
		if self.what != "None":
			bgm = waveOpen("bgm_mouthmoney.wav", "rb")
			self.keeprunning = True
			reses = []
			while(self.keeprunning):
				if len(reses) >= 128: #TODO
					#Abspielen
					self.soundout.stdin.write(b"".join(reses))
					reses = []
				if self.scheduled and self.what != "bgm":
					scheduled = self.scheduled
					read0 = bgm.readframes(4)
					if not read0:
						bgm.rewind()
						continue
					read1 = scheduled.readframes(4)
					if not read1:
						self.scheduled = None
						reses.append(read0)
						continue
					try:
						reses.append(add(read0, read1, 4))
					except:
						pass #really?
				else:
					read = bgm.readframes(256)
					if not read:
						bgm.rewind()
						continue
					reses.append(read)
	
	def reset(self):
		self.scheduled = None
	
	def play(self, filename):
		self.scheduled = waveOpen(filename, "rb")
	
	def explosion(self):
		self.play("explosion.wav")
	
	def train(self):
		if self.what == "train":
			self.play("train.wav")
		elif self.what == "NootNoot":
			self.play("NootNoot.wav")
