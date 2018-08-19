sd='/*sadsd*/  /*asdsda*/'

import re

begin_cooment = re.compile('/\*.*?')
end_comment = re.compile('\*/.*?')


resd=end_comment.findall(sd)

print(len(resd))