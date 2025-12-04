# Log-Analyzer 🛡️


<br>
<h2> A simple Python-based security tool that simulates a real-world security monitoring scenario. It creates a log file with mixed normal and attack traffics , then analyzes it to identify brute force attempts based on failed login patterns through an automated log analysis.</h2>

📌 

<BR>
**1. Clone and Navigate**
```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
<BR>
2. Generate Logs
bash

python log_generator.py

Creates Server_Activity.log with 35 entries (including 10 failed attempts from attacker IP)
3. Analyze for Attacks
bash

python log_analyzer.py

Detects attacks and creates report.txt with findings
<BR>
<H2>How it works :</H2> 

graph TD;
    A[Log Generator] -->|Creates| B(Server_Activity.log);
    B -->|Read by| C[Log Analyzer];
    C -->|Parses & Counts| D{Detection Logic};
    D -- Count < 5 --> E[Normal Traffic];
    D -- Count >= 5 --> F[> Trigger Alert <];
    F -->|Writes to| G[report.txt];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#f96,stroke:#333,stroke-width:2px
    style G fill:#9f9,stroke:#333,stroke-width:2px                                  
<h2> Features:</h2>
<br>
- Smooth scrolling between sections  <br>
- Navigation bar for quick access  <br>
- Sections: services, products, contact, and reviews  <br>
- "Back to top" arrow for easy navigation  <br>
<h2> Screenshots :</h2>
Homepage <br>
<img src="./imgs/Screenshot1.png"><br>
Products Section <br>
<img src="./imgs/Screenshot2.png"><br>
<h2> More information:</h2>
This project focuses on creating a smooth and modern browsing experience for an e-commerce landing page.  


