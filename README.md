# Log-Analyzer 🛡️


<br>
<h1> A simple Python-based security tool that simulates a real-world security monitoring scenario. It creates a log file with mixed normal and attack traffics , then analyzes it to identify brute force attempts based on failed login patterns through an automated log analysis.</h1>
<BR>

<h2> - How to run : </h2>
<h2> 1. Clone and Navigate </h2>
<pre> bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer 
</pre>

<BR>
<h2>2. Generate Logs </h2>
<pre>
bash
python log_generator.py
</pre>
Creates Server_Activity.log with 35 entries (including 10 failed attempts from attacker IP)
<BR>
<h2> 3. Analyze for Attacks</h2>
<pre>
bash
python log_analyzer.py
</pre>
Detects attacks and creates report.txt with findings
<BR>


<h2> - How it works :</h2>h

<b> [Log Generator]</b> → <b> [Log Analyzer] </b> →  <b>[Attack Detector]  </b> → <b> [Report Generator] </b> 
-create log files            -contain mixed traffic   -parse the logs               -summary result 


    
<h2> Screenshots :</h2>
Homepage <br>
<img src="./imgs/Screenshot1.png"><br>
Products Section <br>
<img src="./imgs/Screenshot2.png"><br>



