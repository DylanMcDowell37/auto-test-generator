import random

#List of the questions and answers 
questions = [
        '''(1) A security analyst needs to make a recommendation for restricting access to certain segments of the network using only data-link layer security. Which of the following controls will the analyst MOST likely recommend?
                A. MAC
                B. ACL
                C. BPDU
                D. ARP ''',
 
        '''(2) Which of the following describes the BEST approach for deploying application patches?
                A. Apply the patches to systems in a testing environment then to systems in a staging environment, and finally to production systems.
                B. Test the patches in a staging environment, develop against them in the development environment, andthen apply them to the production systems
                C. Test the patches m a test environment apply them to the production systems and then apply them to a staging environment
                D. Apply the patches to the production systems apply them in a staging environment, and then test all of them in a testing environment''',
 
        '''(3) An organization that is located in a flood zone is MOST likely to document the concerns associated with the restoration of IT operation in a:
                A. business continuity plan
                B. communications plan.
                C. disaster recovery plan.
                D. continuity of operations plan''',
        '''(4)An organization is concerned that is hosted web servers are not running the most updated version of the software. Which of the following would work BEST to help identify potential vulnerabilities?
                A. Hping3 –s comptia, org –p 80
                B. Nc -1 –v comptia, org –p 80
                C. nmp comptia, org –p 80 –aV
                D. nslookup –port=80 comtia.org ''',
        '''(5)A security engineer needs to enhance MFA access to sensitive areas in a building. A key card and fingerprint scan are already in use. Which of the following would add another factor of authentication?
                A. Hard token
                B. Retina scan
                C. SMS text
                D. Keypad PIN''',
        '''(6)A commercial cyber-threat intelligence organization observes IoCs across a variety of unrelated customers. Prior to releasing specific threat intelligence to other paid subscribers, the organization is MOST likely obligated by contracts to:
                A. perform attribution to specific APTs and nation-state actors.
                B. anonymize any PII that is observed within the IoC data.
                C. add metadata to track the utilization of threat intelligence reports.
                D. assist companies with impact assessments based on the observed data. ''',
                 '''(7)Which of the following are the MOST likely vectors for the unauthorized inclusion of vulnerable code in a software company’s final software releases? (Select TWO.)
                A. Unsecure protocols
                B. Use of penetration-testing utilities
                C. Weak passwords
                D. Included third-party libraries
                E. Vendors/supply chain
                F. Outdated anti-malware software
                 ''',
        '''(8)A financial organization has adopted a new secure, encrypted document-sharing application to help with its customer loan process. Some important PII needs to be shared across this new platform, but it is getting blocked by the DLP systems. Which of the following actions will BEST allow the PII to be shared with the secure application without compromising the organization’s security posture?
                A. Configure the DLP policies to allow all PII
                B. Configure the firewall to allow all ports that are used by this application
                C. Configure the antivirus software to allow the application
                D. Configure the DLP policies to whitelist this application with the specific PII
                E. Configure the application to encrypt the PII
                  ''',
        '''(9)After a ransomware attack a forensics company needs to review a cryptocurrency transaction between the victim and the attacker. Which of the following will the company MOST likely review to trace this transaction?
                A. The public ledger
                B. The NetFlow data
                C. A checksum
                D. The event log
                  ''',
        '''(10)A network engineer is troubleshooting wireless network connectivity issues that were reported by users. The issues are occurring only in the section of the building that is closest to the parking lot. Users are intermittently experiencing slow speeds when accessing websites and are unable to connect to network drives. The issues appear to increase when laptop users return desks after using their devices in other areas of the building. There have also been reports of users being required to enter their credentials on web pages in order to gain access to them. Which of the following is the MOST likely cause of this issue?
                A. An external access point is engaging in an evil-twin attack.
                B. The signal on the WAP needs to be increased in that section of the building.
                C. The certificates have expired on the devices and need to be reinstalled.
                D. The users in that section of the building are on a VLAN that is being blocked by the firewall.
                  ''',
        '''(11)A remote user recently took a two-week vacation abroad and brought along a corporate-owned laptop. Upon returning to work, the user has been unable to connect the laptop to the VPN. Which of the following is the MOST likely reason for the user’s inability to connect the laptop to the VPN?
                A. Due to foreign travel, the user’s laptop was isolated from the network.
                B. The user’s laptop was quarantined because it missed the latest path update.
                C. The VPN client was blacklisted.
                D. The user’s account was put on a legal hold.
                  ''',
        '''(12)Several employees return to work the day after attending an industry trade show. That same day, the security manager notices several malware alerts coming from each of the employee’s workstations. The security manager investigates but finds no signs of an attack on the perimeter firewall or the NIDS. Which of the following is MOST likely causing the malware alerts?
                A. A worm that has propagated itself across the intranet, which was initiated by presentation media
                B. A fileless virus that is contained on a vCard that is attempting to execute an attack
                C. A Trojan that has passed through and executed malicious code on the hosts
                D. A USB flash drive that is trying to run malicious code but is being blocked by the host firewall
                  ''',
        '''(13)When used at the design stage, which of the following improves the efficiency, accuracy, and speed of a database?
                A. Tokenization
                B. Data masking
                C. Normalization
                D. Obfuscation
                  ''',
 
        '''(14)A smart switch has the ability to monitor electrical levels and shut off power to a building in the event of power surge or other fault situation. The switch was installed on a wired network in a hospital and is monitored by the facilities department via a cloud application. The security administrator isolated the switch on a separate VLAN and set up a patch routine. Which of the following steps should also be taken to harden the smart switch?
                A. Set up an air gap for the switch.
                B. Change the default password for the switch.
                C. Place the switch In a Faraday cage.
                D. Install a cable lock on the switch
                  ''',
 
        '''(15)A network technician is installing a guest wireless network at a coffee shop. When a customer purchases an Item, the password for the wireless network is printed on the recent so the customer can log in. Which of the following will the technician MOST likely configure to provide the highest level of security with the least amount of overhead?
                A. WPA-EAP
                B. WEP-TKIP
                C. WPA-PSK
                D. WPS-PIN
                  ''',
        '''(16)A security analyst needs to be proactive in understand the types of attacks that could potentially target the company's execute. Which of the following intelligence sources should to security analyst review?
                A. Vulnerability feeds
                B. Trusted automated exchange of indicator information
                C. Structured threat information expression
                D. Industry information-sharing and collaboration groups
                  ''',
        '''(17)A company recently set up an e-commerce portal to sell its product online. The company wants to start accepting credit cards for payment, which requires compliance with a security standard. Which of the following standards must the company comply with before accepting credit cards on its e-commerce platform?
                A. PCI DSS
                B. ISO 22301
                C. ISO 27001
                D. NIST CSF
                  ''',
     
        '''(18)Joe, a user at a company, clicked an email link led to a website that infected his workstation. Joe, was connected to the network, and the virus spread to the network shares. The protective measures failed to stop this virus, and It has continues to evade detection. Which of the following should administrator implement to protect the environment from this malware?
                A. Install a definition-based antivirus.
                B. Implement an IDS/IPS
                C. Implement a heuristic behavior-detection solution.
                D. Implement CASB to protect the network shares.
                  ''',
        '''(19)A network administrator would like to configure a site-to-site VPN utilizing iPSec. The administrator wants the tunnel to be established with data integrity encryption, authentication and anti- replay functions Which of the following should the administrator use when configuring the VPN?
                A. AH
                B. EDR
                C. ESP
                D. DNSSEC
                  ''',
        '''(20)A system administrator needs to implement an access control scheme that will allow an object’s access policy be determined by its owner. Which of the following access control schemes BEST fits the requirements?
                A. Role-based access control
                B. Discretionary access control
                C. Mandatory access control
                D. Attribute-based access control
                  ''',
       
        '''(21)To reduce costs and overhead, an organization wants to move from an on-premises email solution to a cloud-based email solution. At this time, no other services will be moving. Which of the following cloud models would BEST meet the needs of the organization?
                A. MaaS
                B. laaS
                C. SaaS
                D. PaaS
                  ''',
       
        '''(22)Which of the following is MOST likely to outline the roles and responsibilities of data controllers and data processors?
                A. SSAE SOC 2
                B. PCI DSS
                C. GDPR
                D. ISO 31000
                  ''',
        '''(23)Which of the following organizational policies are MOST likely to detect fraud that is being conducted by existing employees? (Select TWO).
                A. Offboarding
                B. Mandatory vacation
                C. Job rotation
                D. Background checks
                E. Separation of duties
                F. Acceptable use
                 ''',
       
        '''(24)A security analyst needs to complete an assessment. The analyst is logged into a server and must use native tools to map services running on it to the server's listening ports. Which of the following tools can BEST accomplish this talk?
                A. Netcat
                B. Netstat
                C. Nmap
                D. Nessus
                 ''',
        '''(25)Which of the following is a team of people dedicated testing the effectiveness of organizational security programs by emulating the techniques of potential attackers?
                A. Red team
                B. While team
                C. Blue team
                D. Purple team
                 ''',
        '''(26)A company uses wireless tor all laptops and keeps a very detailed record of its assets, along with a comprehensive list of devices that are authorized to be on the wireless network. The Chief Information Officer (CIO) is concerned about a script kiddie potentially using an unauthorized device to brute force the wireless PSK
           and obtain access to the internal network. Which of the following should the company implement to BEST prevent this from occurring?
                A. A BPDU guard
                B. WPA-EAP
                C. IP filtering
                D. A WIDS
                  ''',
       
        '''(27)The following is an administrative control that would be MOST effective to reduce the occurrence of malware execution?
                A. Security awareness training
                B. Frequency of NIDS updates
                C. Change control procedures
                D. EDR reporting cycle
                  ''',
        '''(28)A security manager for a retailer needs to reduce the scope of a project to comply with PCI DSS. The PCI data is located in different offices than where credit cards are accepted. All the offices are connected via MPLS back to the primary datacenter. Which of the following should the security manager implement to achieve the objective?
                A. Segmentation
                B. Containment
                C. Geofencing
                D. Isolation
                  ''',
        '''(29)A security engineer needs to Implement the following requirements:
                • All Layer 2 switches should leverage Active Directory tor authentication.
                • All Layer 2 switches should use local fallback authentication If Active Directory Is offline.
                • All Layer 2 switches are not the same and are manufactured by several vendors.
                Which of the following actions should the engineer take to meet these requirements? (Select TWO).
                A. Implement RADIUS.
                B. Configure AAA on the switch with local login as secondary.
                C. Configure port security on the switch with the secondary login method.
                D. Implement TACACS+
                E. Enable the local firewall on the Active Directory server.
                F. Implement a DHCP server.
                 ''',
       
        '''(30)An organization's RPO for a critical system is two hours. The system is used Monday through Friday, from 9:00 am to 5:00 pm. Currently, the organization performs a full backup every Saturday that takes four hours to complete. Which of the following additional backup implementations would be the BEST way for the analyst to meet the business requirements?
                A. Incremental backups Monday through Friday at 6:00 p.m and differential backups hourly
                B. Full backups Monday through Friday at 6:00 p.m and incremental backups hourly.
                C. incremental backups Monday through Friday at 6:00 p.m and full backups hourly.
                D. Full backups Monday through Friday at 6:00 p.m and differential backups hourly.
                  ''',
        '''(31)A company wants to deploy PKI on its Internet-facing website. The applications that are currently deployed are:
                >www.company.com (main website)
                >contactus.company.com (for locating a nearby location)
                >quotes.company.com (for requesting a price quote)
               
                The company wants to purchase one SSL certificate that will work for all the existing applications and any future applications that follow the same naming conventions, such as store.company.com. Which of the following certificate types would BEST meet the requirements?
                A. SAN
                B. Wildcard
                C. Extended validation
                D. Self-signed
                 ''',
        '''(32)Which of the following would be BEST to establish between organizations to define the responsibilities of each party outline the key deliverables and include monetary penalties for breaches to manage third-party risk?
                A. An ARO
                B. An MOU
                C. An SLA
                D. A BPA
                  ''',
       
        '''(33)Which of the following algorithms has the SMALLEST key size?
                A. DES
                B. Twofish
                C. RSA
                D. AES
                  ''',
        '''(34)A university with remote campuses, which all use different service providers, loses Internet connectivity across all locations. After a few minutes, Internet and VoIP services are restored, only to go offline again at random intervals, typically within four minutes of services being restored. Outages continue throughout the day, impacting all inbound and outbound connections and services. Services that are limited to the local LAN or WiFi network are not impacted, but all WAN and VoIP services are affected.
                Later that day, the edge-router manufacturer releases a CVE outlining the ability of an attacker to exploit the SIP protocol handling on devices, leading to resource exhaustion and system reloads. Which of the following BEST describe this type of attack? (Choose two.)
                A. DoS
                B. SSL stripping
                C. Memory leak
                D. Race condition
                E. Shimming
                F. Refactoring
                  ''',
        '''(35)An employee has been charged with fraud and is suspected of using corporate assets. As authorities collect evidence, and to preserve the admissibility of the evidence, which of the following forensic techniques should be used?
                A. Order of volatility
                B. Data recovery
                C. Chain of custody
                D. Non-repudiation
                  ''',
        '''(36)An organization with a low tolerance for user inconvenience wants to protect laptop hard drives against loss or data theft. Which of the following would be the MOST acceptable?
                A. SED
                B. HSM
                C. DLP
                D. TPM
                  ''',
        '''(37)A well-known organization has been experiencing attacks from APIs. The organization is concerned that custom malware is being created and emailed into the company or installed on USB sticks that are dropped in parking lots. Which of the following is the BEST defense against this scenario?
                A. Configuring signature-based antivirus io update every 30 minutes
                B. Enforcing S/MIME for email and automatically encrypting USB drives upon insertion.
                C. Implementing application execution in a sandbox for unknown software.
                D. Fuzzing new files for vulnerabilities if they are not digitally signed
                 ''',
        '''(38)An organization’s help desk is flooded with phone calls from users stating they can no longer access certain websites. The help desk escalates the issue to the security team, as these websites were accessible the previous day. The security analysts run the following command: ipconfig /flushdns, but the issue persists. Finally, an analyst changes the DNS server for an impacted machine, and the issue goes away. Which of the following attacks MOST likely occurred on the original DNS server?
                A. DNS cache poisoning
                B. Domain hijacking
                C. Distributed denial-of-service
                D. DNS tunneling
                  ''',
 
        '''(39)An organization has a growing workforce that is mostly driven by additions to the sales department. Each newly hired salesperson relies on a mobile device to conduct business. The Chief Information Officer (CIO) is wondering it the organization may need to scale down just as quickly as it scaled up. The ClO is also concerned about the organization's security and customer privacy. Which of the following would be BEST to address the ClO’s concerns?
                A. Disallow new hires from using mobile devices for six months
                B. Select four devices for the sales department to use in a CYOD model
                C. Implement BYOD for the sates department while leveraging the MDM
                D. Deploy mobile devices using the COPE methodology
                  ''',
        '''(40)A host was infected with malware. During the incident response, Joe, a user, reported that he did not receive any emails with links, but he had been browsing the Internet all day. Which of the following would MOST likely show where the malware originated?
                A. The DNS logs
                B. The web server logs
                C. The SIP traffic logs
                D. The SNMP logs
                  ''']
answers = ["a", "a", "c", "c", "b", "b", "ad", "d", "a", "a", "a", "a", "c", "b", "a", "d", "a", "c", "c", "b", "d", "c", "bc", "b", "a", "b", "a", "a", "ab", "a", "b", "b", "b", "ad", "c", "a", "c", "b", "c", "a"]
#List of numbers from 0  to the length of the question list
number = list(range(len(questions)))
#Welcome message to the user with the option to start the quiz
print("Welcome to the Quiz!")
playing = input("Are you ready to begin?(yes or no) ").lower()
if playing != "yes":
    quit()

while True:
        #Randomly shuffle the list of numbers and set score to 0
        score = 0
        random.shuffle(number)
        #Loop through the list of the shuffled numbers and print the question at the index of the number
        for i in range(len(questions)):
                print(questions[number[i]])
                answer = input("Answer: ").lower()
                #compare the answer to the correct answer and add 1 to the score if the answer is correct
                if answer == answers[number[i]]:
                        print("Correct!")
                        score += 1
                        continue
                else: 
                        print("Incorrect the correct answer was:", answers[number[i]].capitalize())
        #Print the score and ask the user if they want to play again
        print("You got", score, "out of", len(questions), "correct!")
        playagain = input("Play again?(yes or no) ").lower()
        if playagain != "yes":
                quit()
        else:
                continue                
   

   
