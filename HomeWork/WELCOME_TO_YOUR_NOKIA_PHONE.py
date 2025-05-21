print("WELCOME TO YOUR NOKIA PHONE")
print("LIST OF MENU FUNTIONS")
print("""
MENU 
	1. Phone book.
	2. Massages.
	3. Chat.
	4. Call register.
	5. Tones.
	6. Settings.
	7. Call divert.
	8. Games.
	9. Calculator.
	10. Remainders.
	11. Clocks.
	12. Profiles.
	13. SIM services.
""")
number = int(input('Enter any number from 1 to 13 to pick a MENU'))
match number:
		case 1:
			print ('PHONEBOOK')
			print("""
			1. Search.
			2. Services Nos.
			3. Add name.
			4. Erase.
			5. Edit.
			6. Assign tone.
			7. Send b'card.
			8. Options.
			9. Speed dials.
			10. Voice tags.

		""")
			number1 = int(input('Enter any number from 1 to 10 to pick a phone'))
			match number1:
				case 1:
					print ('SEARCH')
				case 2:
					print ('SERVICE NOS')
				case 3:
					print ('ADD NAME')
				case 4:
					print ('ERASE')
				case 5:
					print ('EDIT')
				case 6:
					print ('ASSIGN TONE')
				case 7:
					print ("SEND B'CARD")
				case 8:
					print ('OPTIONS')
					print("""
					1. Type of view.
					2. Memory status.

					""")
					number1 = int(input('Enter any number from 1 or 2 to pick a OPTION'))
					match number1:
						case 1:
							print ('TYPE OF VIEW')
						case 2:
							print ('MEMORY STATUS')
				case 9:
					print ('TYPE OF VIEW')
				case 10:
					print ('MEMORY SATAUS')

				
		case 2:
			print ('MESSAGES')
			print("""
			1. Write massages.
			2. Inbox.
			3. Outbox.
			4. Picture massages.
			5. Templates.
			6. Smileys.
			7. Message settings.
			8. Info service.
			9. Voice mailbox number.
			10.Service command editor.

		""")
			number1 = int(input('Enter any number from 1 to 10 to pick a MASSEGE'))
			match number1:
				case 1:
					print ('WRITE MASSEGES')
				case 2:
					print ('INBOX')
				case 3:
					print ('OUTBOX')
				case 4:
					print ('PICTURE MASSAGES')
				case 5:
					print ('TEMPLATES')
				case 6:
					print ('SMILEYS')
				case 7:
					print ('MESSAGE_SETTING')
					print("""
					1. Set 1.
					2. Common.

					""")
					number1 = int(input('Enter any number from 1 or 2 to pick a MESSAGE SETTING'))
					match number1:
						case 1:
							print ('SET 1')
							print("""
							1. Message center number.
							2. Messages sent as.
							3. Message vaildity.

							""")
							number1 = int(input('Enter any number from 1 or 3 to pick a SET 1'))
							match number1:
								case 1:
									print ('MESSAGE CENTER NUMBER')
				
								case 2:
									print ('MESSAGES SENT AS')
	
								case 3:
									print ('MESSAGE VAILDITY')


						case 2:
							print ('COMMON')
							print("""
							1. Delivery reports.
							2. Reply via same centre.
							3. character support.

							""")
							number1 = int(input('Enter any number from 1 or 3 to pick a COMMON'))
							match number1:
								case 1:
									print ('DELIVERY REPORTS')
				
								case 2:
									print ('REPLY VIA SAME CENTRE')
	
								case 3:
									print ('CHARACTER SUPPORT')

				case 8:
					print ('INFO SERVICE')
				case 9:
					print ('VOICE MAILBOX NUMBER')
				case 10:
					print ('SERVICE COMMAND EDITOR')


		case 3:
			print ('CHAT')

		case 4:
			print ('CALLREGISTER')
			print("""
			1. Missed calls.
			2. Received calls.
			3. Dialled numbers.
			4. Erase recent call lists.
			5. Show call duration.
			6. Show call costs.
			7. Call cost settings.
			8. Prepaid credit.
			""")
			number1 = int(input('Enter any number from 1 to 10 to pick a CALL REGISTER'))
			match number1:
				case 1:
					print ('MISSED CALLS')
				case 2:
					print ('RECEIVED CALLS')
				case 3:
					print ('DIALLED NUMBERS')
				case 4:
					print ('ERASE RECENT CALL LISTS')
				case 5:
					print ('SHOW CALL DURATION')
					print("""
					1. Last call duration.
					2. All calls'duration.
					3. Received calls'duration.
					4. Dialled calls'duration.
					5. Clear timers.
					""")
					number1 = int(input('Enter any number from 1 or 3 to pick a SHOW CALL DURATION'))
					match number1:
						case 1:
							print ('LAST CALL DURATION')
						case 2:
							print ('ALL CALLS DURATION')
						case 3:
							print ("RECEIVED CALL'S DURATION")
						case 4:
							print ('DIALLED CALLS DURATION')
						case 5:
							print ('CLEAR TIMERS')
						
				case 6:
					print ('SHOW CALL COSTS')
					print("""
					1. Last call cost.
					2. All call's cost.
					3. Clear counters.
					""")
					number1 = int(input('Enter any number from 1 or 3 to pick a SHOW CALL COSTS'))
					match number1:
						case 1:
							print ('LAST CALL COST')
						case 2:
							print ('ALL CALLS COST')
						case 3:
							print ('CLEAR COUNTERS')
						

				case 7:
					print ('CALL COST SETTINGS')
					print("""
					1. Call cost limit.
					2. Show costs in.
					""")
					number1 = int(input('Enter any number from 1 or 3 to pick a CALL COST SETTING'))
					match number1:
						case 1:
							print ('CALL COST LIMITS')
						case 2:
							print ('SHOW COST IN')
						
		

				case 8:
					print ('PREPAID CREDIT')


		case 5:
			print ('TONES')
			print("""
			1. Ringing tone.
			2. Ringing volume.
			3. Incoming call alert.
			4. Composer.
			5. Message alert tone.
			6. Keypad tones.
			7. Warning and game tones.
			8. Vibrating alert.
			9. Screen saver.

			""")
			number1 = int(input('Enter any number from 1 to 10 to pick a TONES'))
			match number1:
				case 1:
					print ('RINGING TONE')
				case 2:
					print ('RINGING VOLUME')
				case 3:
					print ('INCOMING CALL ALERT')
				case 4:
					print ('COMPOSER')
				case 5:
					print ('MESSAGE ALERT TONE')
				case 6:
					print ('KEYPAD TONES')
				case 7:
					print ('WARNING AND GAME TONES')
				case 8:
					print ('VIBRATING ALERT')
				case 9:
					print ('SCREEN SAVER')


		case 6:
			print ('SETTINGS')
			print("""
			1. Call Settings.
			2. Phone settings.
			3. Security settings.
			4. Restore factory settings.

			""")
			number1 = int(input('Enter any number from 1 to 10 to pick a SETTING'))
			match number1:
				case 1:
					print ('CALL SETTINGS')
					print("""
					1. Automatic redial.
					2. Speed dialling.
					3. Call waiting options.
					4. Own number sending.
					5. Phone line in use.
					6. Automatic answer.
					""")
					number1 = int(input('Enter any number from 1 or 3 to pick a OPTION'))
					match number1:
						case 1:
							print ('AUTOMATIC REDIAL')
						case 2:
							print ('SPEED DIALLING')
						case 3:
							print ('CALL WAITING OPTIONS')
						case 4:
							print ('OWN NUMBER SENDING')
						case 5:
							print ('PHONE LINE IN USE')
						case 6:
							print ('AUTHOMATIC ANSWER')


				case 2:
					print ('PHONE SETTINGS')
					print("""
					1. Language.
					2. Cell info display.
					3. Welcome note.
					4. Network selection.
					5. Lights.
					6. Confirm SIM service actions.
					""")
					number1 = int(input('Enter any number from 1 or 3 to pick a OPTION'))
					match number1:
						case 1:
							print ('LANGUAGE')
						case 2:
							print ('CALL INFO DISPLAY')
						case 3:
							print ('WELCOME NOTE')
						case 4:
							print ('NETWORK SELECTION')
						case 5:
							print ('LIGHTS')
						case 6:
							print ('CONFIRM SIM SERVICE ACTIONS')


				case 3:
					print ('SECURITY SETTINGS')
					print("""
					1. PIN code request.
					2. Call barring service.
					3. Fixed dialling.
					4. Closed user group.
					5. Phone security.
					6. Change access codes.
					""")
					number1 = int(input('Enter any number from 1 to 6 to pick a OPTION'))
					match number1:
						case 1:
							print ('PIN CODE REQUEST')
						case 2:
							print ('CALL BARRING SERVICE')
						case 3:
							print ('FIXED DIALLING')
						case 4:
							print ('CLOSED USER GROUP')
						case 5:
							print ('PHONE SECURITY')
						case 6:
							print ('CHANGE ACCESS CODES')

				case 4:
					print ('RESTORE FACTORY SETTINGS')


		case 7:
			print ('CALL DIVERT')

		case 8:
			print ('GAMES')

		case 9:
			print ('CALCULATOR')

		case 10:
			print ('REMAINDERS')

		case 11:
			print ('CLOCKS')
			print("""
			1. Alarm clock.
			2. Clock settings.
			3. Date setting.
			4. Stopwatch.
			5. Countdown timer.
			6. Auto update of date and time.

			""")
			number1 = int(input('Enter any number from 1 to 10 to pick a TONES'))
			match number1:
				case 1:
					print ('ALARM CLOCK')
				case 2:
					print ('CLOCK SETTINGS')
				case 3:
					print ('DATE SETTING')
				case 4:
					print ('STOPWATCH')
				case 5:
					print ('COUNTDOWN TIMER')
				case 6:
					print ('AUTO UPDATE OF DATE AND TIME')
				

		case 12:
			print ('PROFILES')

		case 13:
			print ('SIM SERVICES')







































































