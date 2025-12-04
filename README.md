# Log-Analyzer 🛡️


<br>
<h2> A simple Python-based security tool that simulates a real-world security monitoring scenario. It creates a log file with mixed normal and attack traffics , then analyzes it to identify brute force attempts based on failed login patterns through an automated log analysis.</h2>

📌 

<BR>
**1. Clone and Navigate**

<pre> ``` bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer 
</pre>
<BR>

2. Generate Logs
graph TD;
bash

python log_generator.py

Creates Server_Activity.log with 35 entries (including 10 failed attempts from attacker IP)
3. Analyze for Attacks
bash

python log_analyzer.py

Detects attacks and creates report.txt with findings
<BR>







    
<h2> Screenshots :</h2>
Homepage <br>
<img src="./imgs/Screenshot1.png"><br>
Products Section <br>
<img src="./imgs/Screenshot2.png"><br>



