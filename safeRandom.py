import random
import string
import sqlite3

class PropertyId:
  def __init__(self,dbName):
    self.conn = sqlite3.connect(dbName)
    self.cur = self.conn.cursor()
    self.createdB()
    
  def createdB(self):
    self.cur.execute("CREATE TABLE if not exists proId (hashvalue VARCHAR NOT NULL, CONSTRAINT constraint_name UNIQUE(hashvalue) )")
    self.conn.commit()

    
  def close(self):
    self.cur.close()
    self.conn.close()
    
  def genSerialNumber(self,numDigits):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(numDigits))


  def checkID(self,id): 
    t = (id,)
    self.cur.execute("SELECT EXISTS(SELECT 1 FROM proId WHERE hashvalue=?)",t)
    return self.cur.fetchone()[0] == 1

  def addID(self,id): 
    t = (id,)
    self.cur.execute("INSERT INTO proId VALUES (?)",t)
    self.conn.commit()
  
  def safeId(self,numDigits):
    textid = "NO ID!"
    keeptrying=True
    while keeptrying:
      textid=self.genSerialNumber(numDigits)
      keeptrying=self.checkID(textid)
      if keeptrying == False:
        self.addID(textid)
        

    return textid
  