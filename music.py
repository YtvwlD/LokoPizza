from threading import Thread
from wave import open as waveOpen
from audioop import add
from subprocess import Popen, PIPE

class Music(Thread):
	def __init__(self, what):
		self.what = what
		Thread.__init__(self)
		self.scheduled = None
		self.pa = Popen(["pacat", "--latency-msec=1000", "--volume=60000", "--client=LokoPizza"], stdin=PIPE, stdout=None, stderr=None)
	
	def run(self):
		if self.what != "None":
			wave = waveOpen("bgm_mouthmoney.wav", "rb")
			self.keeprunning = True
			while(self.keeprunning):
				reses = []
				for _ in range(128):
					if self.scheduled and self.what != "bgm":
						read0 = wave.readframes(4)
						scheduled = self.scheduled
						read1 = scheduled.readframes(4)
						if not read1:
							self.scheduled = None
							read1 = None
					else:
						read0 = wave.readframes(256)
						read1 = None
					if not read0:
						wave.rewind()
					try:
						res = add(read0, read1, 4)
					except:
						res = read0
					if res:
						reses.append(res)
				if reses:
					res = "".join(reses)
					self.pa.stdin.write(res)
	
	def reset(self):
		self.wave = None
	
	def play(self, filename):
		wave = waveOpen(filename, "rb")
		self.scheduled = wave
	
	def explosion(self):
		self.play("explosion.wav")
	
	def train(self):
		if self.what == "train":
			self.play("train.wav")
		elif self.what == "NootNoot":
			self.play("NootNoot.wav")
