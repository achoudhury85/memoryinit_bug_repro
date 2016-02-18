import re
memory_initializer_pattern = '/\* memory initializer \*/ allocate\(\[([\d, ]*)\], "i8", ALLOC_NONE, ([\d+Runtime\.GLOBAL_BASEH]+)\);'
final='test_file.txt'

def repl(n):
  print "In Repl"

src = re.sub(memory_initializer_pattern, repl, open(final).read(), count=1)

