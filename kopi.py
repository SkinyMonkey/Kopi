from pyrser import grammar, meta
import time

Kopi = grammar.from_file('./grammar/kopi.pw', entry='Root')

if __name__ == '__main__':
  from pprint import pprint
  kopi = Kopi()

  @meta.hook(Kopi)
  def dump(self):
      print('HERE')
      return True

  @meta.hook(Kopi)
  def pause(self):
      print('Pause ------------')
      time.sleep(5)
      return True

  test =\
  """
  a = 1 + 1
  """

  res = kopi.parse(test)
