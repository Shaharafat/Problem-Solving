if __name__ == "__main__":
  year = int(input())

  digits = set()
  while True:
    next_year = year + 1
    year = next_year

    # update set with every digit of year.
    digits.update(*list(str(next_year)))

    # if the length is 4 then all digits are distinct
    if len(digits) == 4:
      print(next_year)
      break
    else:
      digits.clear()
