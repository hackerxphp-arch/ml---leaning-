# ml---leaning-
this is my first Git Repository
<br>
Author - Saurabh Singh

import pandas as pd
<br>
df = pd .read _csv('train.csv)
<br>
df . head()

from pandas profilling import profileReport
prof = profileReport(df)
prof.to_file(output_file = 'output.html')
