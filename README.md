# Log-Analyzer 🛡️


<br>
 A simple Python-based security tool that simulates a real-world security monitoring scenario. It creates a log file with mixed normal and attack traffics , then analyzes it to identify brute force attempts based on failed login patterns through an automated log analysis. <br>

 


<h2><b>- How to run : </b> </h2>
<h2> 1. Clone and Navigate </h2>
<pre>bash
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
Detects attacks and creates report.txt with findings <br>



<br> <h2> <b> - How it works : </b></h2>
<pre> <b> [Log Generator]</b> → <b> [Server_Activity.log] </b> → <b> [Log Analyzer] </b> → <b> [Generated report] </b>     </pre>      <br>             



<br> <H2> <b> - Screenshots : </b> </H2>
<br>
 <h1> The generated logs </h1> <br>
 <img src="..\assets\Logs.png"><br>
<h1> The output</h1> <br>
 <img src=".\assets\Output.png"><br>
<h1> The report </h1> <br>
 <img src=".\assets\Report.png"><br>
<br>



<h2> <b>💡  - What I learned: </b></h2>
    
   -  Regular expressions for parsing
  
   - Automating security monitoring tasks
     
   -  Log analysis and pattern recognition
     
   -  Brute force attack identification
     
   -  Security incident reporting
