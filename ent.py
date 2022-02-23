from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from pynput.keyboard import Key, Controller
from time import sleep
from datetime import datetime
import pyautogui as p
import os

# https://www.youtube.com/watch?v=Fdu81T9GgMA&t=3s
#https://www.youtube.com/channel/UCHGEA5g4iFDdBognYNWCJbA/videos // https://www.youtube.com/watch?v=fLWZZGDaSCU


keyboard = Controller()

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\MicroGOD\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument('--profile-directory=Profile 3')
options.add_argument("start-maximized")
options.add_argument('--disable-notifications')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

timeTable = [("21-05-11 12:45","21-05-11 14:25","collab","https://rktvxscsyc.univh2c.ma/mod/collaborate/view.php?id=7741"),
      ("21-05-21 10:15","21-05-21 11:55","bbb","https://rktvxscsyc.univh2c.ma/mod/bigbluebuttonbn/view.php?id=7775")]

#timeTable = [("21-03-28 18:55","21-03-28 18:56","collab","https://rktvxscsyc.univh2c.ma/mod/collaborate/view.php?id=7714")] collab ended

"""
timeTable = [("21-01-17 21:38","21-01-17 18:05","bbb","https://rktvxscsyc.univh2c.ma/mod/bigbluebuttonbn/view.php?id=6278"),
      ("21-01-17 18:07","21-01-17 18:08","meet","https://meet.google.com/"),
      ("21-01-17 20:27","21-01-17 21:27","zoom","2660939933","WllEdnVWQTF3QzhWV3pRcjZHQkxEQT09"),
      ("21-01-17 20:27","21-01-17 21:27","collab","https://rktvxscsyc.univh2c.ma/mod/collaborate/view.php?id=7741")]
"""

def now():
  rightNow = datetime.now().strftime("%y-%m-%d %H:%M") # 21-01-17 17:24
  return rightNow

def login(driver):
  username = "USERNAME"
  password = "PASSWORD"
  url = "https://rktvxscsyc.univh2c.ma/my/"
  driver.get(url)
  usernameInput = driver.find_element_by_id("username").send_keys(username)
  passwordInput = driver.find_element_by_id("password").send_keys(password)
  enter = driver.find_element_by_name("submit").click()

def blue(url,driver,end):
  driver.get(url)
  while True:
    if end == now():
      return False
      break
    else:
      try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='join_button_input']")))
        Burl = driver.find_element_by_id("join_button_input").get_attribute("onclick")
        Burl = Burl.split("'")[1]
        driver.get(Burl)
        WebDriverWait(driver, 99).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]'))).click() # Audio Only
        return True
        break
      except:
        driver.get(url)

def collab(url, driver,end):
  driver.get(url)
  while True:
    if end == now():
      return False
      break
    else:
      try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-success']")))
        colabUrl = driver.find_element_by_xpath("//a[@class='btn btn-success']").get_attribute("href")
        driver.get(colabUrl)
        return True
        break
      except:
        driver.get(url)


def meet(url,driver):
  driver.get(url)
  # dismiss //*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span
  WebDriverWait(driver, 99).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span'))).click()
  # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg'))).click()
  # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg'))).click()
  WebDriverWait(driver, 99).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span'))).click() # Join 
  # first noVideo //*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg
  # first mute //*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg
  # ask to join //*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span
  # join        //*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span
  # mute //*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[1]/div/div/div/span/span/div/div[1]/div/svg
  # noVideo //*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[3]/div/div/span/span/div/div/svg

def s(time=1):
  sleep(time)

def ifLogo(logo):
  while True:
    if p.locateOnScreen("logos/{}.png".format(logo)) != None:
      break

def zoom(zoomId,zoomPass):
  join = (813,445)
  writeBox = (948,479)
  noAudio = (801,581)
  noVideo = (801,611)
  joinCall = (987,651)
  passCode = (951,480)
  passJoin = (977,651)
  os.startfile(r"C:\Users\MicroGOD\AppData\Roaming\Zoom\bin\Zoom.exe")
  #  ,"zoomLogoHidden"
  ifLogo("zoomLogo")
  p.getWindowsWithTitle("Zoom")[0].maximize()
  p.click(join)
  ifLogo("joinLogo")
  p.click(writeBox)
  p.typewrite(zoomId)
  p.click(noAudio)
  p.click(noVideo)
  p.click(joinCall)
  ifLogo("passLogo")
  p.click(passCode)
  p.typewrite(zoomPass)
  p.click(passJoin)

def recording(sessionEnd):
  keyboard.press(Key.alt_l)
  keyboard.press(Key.f9)
  keyboard.release(Key.f9)
  keyboard.release(Key.alt_l)
  while True:
    s()
    if now() == sessionEnd:
      print(now())
      break
    else:
      continue
  keyboard.press(Key.alt_l)
  keyboard.press(Key.f9)
  keyboard.release(Key.f9)
  keyboard.release(Key.alt_l)


def main():
  while True:
    s()
    for i in timeTable:
      if now() == i[0]:
        print(now())
        if i[2] == 'bbb':
          driver = webdriver.Chrome(options=options)
          login(driver)
          isProf = blue(i[3],driver,i[1])
          if isProf == True:
            recording(i[1])
          driver.close()
        elif i[2] == 'collab':
          driver = webdriver.Chrome(options=options)
          login(driver)
          isProf = collab(i[3], driver,i[1])
          if isProf == True:
            recording(i[1])
          driver.close()
        elif i[2] == 'zoom':
          zoom(i[3],i[4])
          recording(i[1])
        elif i[2] == 'meet':
          driver = webdriver.Chrome(options=options)
          meet(i[3],driver)
          recording(i[1])
          driver.close()
        else:
          print("Something is wrong please check your table !!!!")

if __name__ == '__main__':
  main()