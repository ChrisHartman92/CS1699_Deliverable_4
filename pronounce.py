#!/usr/bin/env python
import string

def pronounce_year(year):
  pronounce=''
  if year[0]=='2':
    if year[2]=='0':
      if year[3]=='1':
        pronounce='two-thousand and '
      else:
        pronounce='two-thousand '
    else:
      pronounce='twenty-'
  elif year[0]=='1':
    if year[1]=='9':
      pronounce='nineteen '
    elif year[1]=='8':
      pronounce='eighteen '
    elif year[1]=='7':
      pronounce='seventeen '
    elif year[1]=='6':
      pronounce='sixteen '
    elif year[1]=='5':
      pronounce='fifteen '
    elif year[1]=='4':
      pronounce='fourteen '
    elif year[1]=='3':
      pronounce='thirteen '
    elif year[1]=='2':
      pronounce='twelve '
    elif year[1]=='1':
      pronounce='eleven '
    elif year[1]=='0':
      pronounce='ten '
  if year[2]=='9':
    pronounce+='ninety-'
  elif year[2]=='8':
    pronounce+='eighty-'
  elif year[2]=='7':
    pronounce+='seventy-'
  elif year[2]=='6':
    pronounce+='sixty-'
  elif year[2]=='5':
    pronounce+='fifty-'
  elif year[2]=='4':
    pronounce+='fourty-'
  elif year[2]=='3':
    pronounce+='thirty-'
  elif year[2]=='2':
    pronounce+='twenty-'
  elif year[2]=='1':
    if year[3]=='9':
      pronounce+='nineteen'
    elif year[3]=='8':
      pronounce+='eighteen'
    elif year[3]=='7':
      pronounce+='seventeen'
    elif year[3]=='6':
      pronounce+='sixteen'
    elif year[3]=='5':
      pronounce+='fifteen'
    elif year[3]=='4':
      pronounce+='fourteen'
    elif year[3]=='3':
      pronounce+='thirteen'
    elif year[3]=='2':
      pronounce+='twelve'
    elif year[3]=='1':
      pronounce+='eleven'
    elif year[3]=='0':
      pronounce+='ten'
    return pronounce
  if year[3]=='9':
    pronounce+='nine'
  elif year[3]=='8':
    pronounce+='eight'
  elif year[3]=='7':
    pronounce+='seven'
  elif year[3]=='6':
    pronounce+='six'
  elif year[3]=='5':
    pronounce+='five'
  elif year[3]=='4':
    pronounce+='four'
  elif year[3]=='3':
    pronounce+='three'
  elif year[3]=='2':
    pronounce+='two'
  elif year[3]=='1':
    pronounce+='one'
  elif year[3]=='0':
    pronounce=pronounce[0:len(pronounce)-1]
  return pronounce

def pronounce_day(day):
  pronounce=''
  if len(day)==2:
    if day[0]=='1':
      if day[1]=='9':
        pronounce='Nineteenth'
      elif day[1]=='8':
        pronounce='Eighteenth'
      elif day[1]=='7':
        pronounce='Seventeenth'
      elif day[1]=='6':
        pronounce='Sixteenth'
      elif day[1]=='5':
        pronounce='Fifteenth'
      elif day[1]=='4':
        pronounce='Fourteenth'
      elif day[1]=='3':
        pronounce='Thirteenth'
      elif day[1]=='2':
        pronounce='Twelfth'
      elif day[1]=='1':
        pronounce='Eleventh'
      elif day[1]=='0':
        pronounce='Tenth'
      return pronounce
    if day[0]=='3':
      pronounce='Thirty-'
      if day[1]=='0':
        pronounce='Thirtieth'
        return pronounce
    elif day[0]=='2':
      pronounce='Twenty-'
      if day[1]=='0':
        pronounce='Twentieth'
        return pronounce
    if day[1]=='9':
      pronounce+='ninth'
    if day[1]=='8':
      pronounce+='eighth'
    if day[1]=='7':
      pronounce+='seventh'
    if day[1]=='6':
      pronounce+='sixth'
    if day[1]=='5':
      pronounce+='fifth'
    if day[1]=='4':
      pronounce+='fourth'
    if day[1]=='3':
      pronounce+='third'
    if day[1]=='2':
      pronounce+='second'
    if day[1]=='1':
      pronounce+='first'
  else:
    if day=='9':
      pronounce='Ninth'
    if day=='8':
      pronounce='Eighth'
    if day=='7':
      pronounce='Seventh'
    if day=='6':
      pronounce='Sixth'
    if day=='5':
      pronounce='Fifth'
    if day=='4':
      pronounce='Fourth'
    if day=='3':
      pronounce='Third'
    if day=='2':
      pronounce='Second'
    if day=='1':
      pronounce='First'
  return pronounce
  
