from threading import Thread
from wave import open as waveOpen
from audioop import add
from subprocess import Popen, PIPE

class Music(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.scheduled = []
		self.pa = Popen(["pacat", "--latency-msec=200", "--volume=60000", "--client=LokoPizza"], stdin=PIPE, stdout=None, stderr=None)
	
	def run(self):
		wave = waveOpen("bgm_mouthmoney.wav", "rb")
		self.keeprunning = True
		while(self.keeprunning):
			read0 = wave.readframes(4)
			if not read0:
				wave.rewind()
				read0 = wave.readframes(4)
			if self.scheduled:
				scheduled = self.scheduled[0]
				read1 = scheduled.readframes(4)
				if not read1:
					self.scheduled.remove(scheduled)
					read1 = None
			else:
				read1 = None
			try:
				res = add(read0, read1, 4)
			except:
				res = read0
			if res:
				self.pa.stdin.write(res)
				#self.pa.stdin.flush()
	
	def play(self, filename):
		wave = waveOpen(filename, "rb")
		self.scheduled.append(wave)
