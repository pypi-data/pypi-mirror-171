class UncleEngineer:
	





	def __init__(self):
		self.name = 'ลุงวิศวกร สอนคํานาน'
		self.page = 'https://www.facebook.com/uncleEngineer'

	def show_name(self):
		print('สวัสดีฉันชื่อตู่ {}'.format(self.name))

	def show_youtube(self):
		print('https://www.youtube.com/c/UncleEngineer')

	def about(self):
		text = """
		-------------------------------------------
		สัสดีจ้าา นี่คือนายกเอง เป็นผู้ดูแลเพจ 'ลุงวิศวกร สอนคํานาน'
		สามารถติดตามเพจลุงได้ ท่านจะได้รับความความรู้จากเรา
		-------------------------------------------"""		
		print(text)

	def show_art(self):
		text = """
		            ,----------------,              ,---------,
		        ,-----------------------,          ,"        ,"|
		      ,"                      ,"|        ,"        ,"  |
		     +-----------------------+  |      ,"        ,"    |
		     |  .-----------------.  |  |     +---------+      |
		     |  |                 |  |  |     | -==----'|      |
		     |  |  I LOVE         |  |  |     |         |      |
		     |  | python          |  |  |/----|`---=    |      |
		     |  |  by chun        |  |  |   ,/|==== ooo |      ;
		     |  |                 |  |  |  // |(((( [33]|    ,"
		     |  `-----------------'  |," .;'| |((((     |  ,"
		     +-----------------------+  ;;  | |         |,"     Credit: Kevin Lam-
		        /_)______________(_/  //'   | +---------+
		   ___________________________/___  `,
		  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
		 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
		/_==__==========__==_ooo__ooo=_/'   /___________,"
		`-----------------------------'

		"""	
		print(text)

	def dice(self):
		dice_list = ['😃','😄','😁','😅','🤣']	
		first = random.choice(dice_list)
		second = random.choice(dice_list)
		print('คุณทอยเต๋าได้: {} {}'.format(first.second))


if __name__ == '__main__':
	uncle = UncleEngineer()
	uncle.show_name()
	uncle.show_youtube()
	uncle.about()
	uncle.show_art()			