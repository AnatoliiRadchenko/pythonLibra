class Libra:
  def pressEnter(self):
    _input = 1 
    while _input!='': _input=input('press Enter')
  def __init__(self,debug=False):
    self.isDebug=debug
    globals()["subprocess"] = __import__("subprocess")

  def debug(self,msg):
    if(self.isDebug): print(': '+msg)
  def su(self):
    self.debug('su')
    subprocess.run(["sh", "-c", "sudo -v"])
  def importModule(self,name):
    try:
        globals()[name] = __import__(name)  # Tentativo di importare il modulo
    except ImportError:
        self.debug("Il modulo 'requests' non è installato. Installo automaticamente...")
        #from subprocess import call
        self.su()
        result = subprocess.run(["sh", "-c", "sudo dnf install -y pip || sudo apt install pip -y"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        result = subprocess.run(["sh", "-c", "pip install "+name],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        globals()[name] = __import__(name)
