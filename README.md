# Log-Analyzer 🛡️



 A simple Python-based security tool that simulates a real-world security monitoring scenario. It creates a log file with mixed normal and attack traffics , then analyzes it to identify brute force attempts based on failed login patterns through an automated log analysis. 

<br>
<br>
<h2>How to run :  </h2>
<b> 1. Clone and Navigate </b>
<pre>bash
git clone https://github.com/Ghaliah1/Python-Log-Analyzer.git
cd log-analyzer 
</pre>
<BR>
<b>2. Generate Logs </b>
<pre>
bash
python log_generator.py
</pre>
Creates Server_Activity.log with 35 entries (including 10 failed attempts from attacker IP)
<br>
<BR>
<br>
<b> 3. Analyze for Attacks</b>
<pre>
bash
python log_analyzer.py
</pre>
Detects attacks and creates report.txt with findings 

<br>
<br>

<br>
 <h2> <b> - How it works : </b></h2>
 <img src=".\assets\Project_Design.png"><br>   
<br>             



 <H2> - Screenshots :  </H2>

 <h3> The generated logs: </h3>
 <img src=".\assets\Logs.png"><br>
<h3> The output:</h3><br>
 <img src=".\assets\Output.png"><br>
<h3> The report: </h3> <br>
 <img src=".\assets\Report.png"><br>
<br>



<h2> 💡  - What I learned: </h2>
    
   -  Regular expressions for parsing
  
   - Automating security monitoring tasks
     
   -  Log analysis and pattern recognition
     
   -  Brute force attack identification
     
   -  Security incident reporting
